import requests
from injson import check
from sweetest.globals import g
from sweetest.lib.elements import get_elem
from sweetest.lib.log import logger
from sweetest.lib.utility import json2dict


class Http:

    def __init__(self, step):
        # 获取 baseurl
        el, baseurl = get_elem(step['page'] + '-' + 'baseurl', True)
        if not baseurl:
            self.baseurl = ''
        else:
            if not baseurl.endswith('/'):
                baseurl += '/'
            self.baseurl = baseurl

        self.r = requests.Session()
        # 获取 headers
        el, self.headers_get = get_elem(step['page'] + '-' + 'headers_get', True)
        el, self.headers_post = get_elem(step['page'] + '-' + 'headers_post', True)


def get(step):
    request('get', step)


def post(step):
    request('post', step)


def put(step):
    request('put', step)


def patch(step):
    request('patch', step)


def delete(step):
    request('delete', step)


def options(step):
    request('options', step)


def request(kw, step):
    element = step['element']
    el, url = get_elem(element)
    if url.startswith('/'):
        url = url[1:]

    data = step['data']
    _data = {}
    _data['headers'] = json2dict(data.pop('headers', '{}'))
    if data.get('cookies'):
        data['cookies'] = json2dict(data['cookies'])
    if kw == 'get':
        _data['params'] = json2dict(data.pop('params', '{}')) or json2dict(data.pop('data', '{}'))
    elif kw == 'post':
        _data['data'] = json2dict(data.pop('data', '{}'))
        _data['json'] = json2dict(data.pop('json', '{}'))
        _data['files'] = eval(data.pop('files', 'None'))
    elif kw in ('put', 'patch'):
        _data['data'] = json2dict(data.pop('data', '{}'))

    for k in data:
        for s in ('{', '[', 'False', 'True'):
            if s in data[k]:
                try:
                    data[k] = eval(data[k])
                except Exception as exception:
                    logger.warning('Try eval data fail: %s' %data[k])
                break
    expected = step['expected']
    expected['status_code'] = expected.get('status_code', None)
    expected['text'] = expected.get('text', None)
    expected['json'] = json2dict(expected.get('json', '{}'))
    expected['cookies'] = json2dict(expected.get('cookies', '{}'))
    expected['headers'] = json2dict(expected.get('headers', '{}'))

    if not g.http.get(step['page']):
        g.http[step['page']] = Http(step)
    http = g.http[step['page']]

    if kw == 'post':
        if http.headers_post:
            http.r.headers.update(eval(http.headers_post))
    else:
        if http.headers_get:
            http.r.headers.update(eval(http.headers_get))

    logger.info('URL: %s' % http.baseurl + url)

    # 处理 before_send
    before_send = data.pop('before_send', '')
    if before_send:
        _data, data = before_send(_data, data)
    else:
        _data, data = before_send(_data, data)

    if _data['headers']:
        for k in [x for x in _data['headers']]:
            if not _data['headers'][k]:
                del http.r.headers[k]
                del _data['headers'][k]
        http.r.headers.update(_data['headers'])

    if kw == 'get':
        r = getattr(http.r, kw)(http.baseurl + url,
                                params=_data['params'], **data)
    elif kw == 'post':
        r = getattr(http.r, kw)(http.baseurl + url,
            data=_data['data'], json=_data['json'], files=_data['files'], **data)
    elif kw in ('put', 'patch'):
        r = getattr(http.r, kw)(http.baseurl + url,
            data=_data['data'], **data)
    elif kw in ('delete', 'options'):
        r = getattr(http.r, kw)(http.baseurl + url, **data)

    logger.info('status_code: %s' % repr(r.status_code))
    try: # json 响应
        logger.info('response json: %s' % repr(r.json()))
    except: # 其他响应
        logger.info('response text: %s' % repr(r.text))

    response = {'status_code': r.status_code, 'headers':r.headers,
                '_cookies': r.cookies, 'content': r.content, 'text': r.text}

    try:
        response['cookies'] = requests.utils.dict_from_cookiejar(r.cookies)
    except:
         response['cookies'] = r.cookies

    try:
        j = r.json()
        response['json'] = j
    except:
        response['json'] = {}

    # 处理 after_receive
    after_receive = expected.pop('after_receive', '')
    if after_receive:
        response = after_receive(response)
    else:
        response = after_receive(response)

    if expected['status_code']:
        assert str(expected['status_code']) == str(response['status_code'])

    if expected['text']:
        if expected['text'].startswith('*'):
            assert expected['text'][1:] in response['text']
        else:
            assert expected['text'] == response['text']

    if expected['headers']:
        result = check(expected['headers'], response['headers'])
        if result['result']:
            step['remark'] += str(result['result'])
        logger.info('headers check result: %s' % result)
        assert result['code'] == 0

    if expected['cookies']:
        logger.info('response cookies: %s' % response['cookies'])
        result = check(expected['cookies'], response['cookies'])
        if result['result']:
            step['remark'] += str(result['result'])
        logger.info('cookies check result: %s' % result)
        assert result['code'] == 0

    if expected['json']:
        result = check(expected['json'], response['json'])
        if result['result']:
            step['remark'] += str(result['result'])
        logger.info('json check result: %s' % result)
        assert result['code'] == 0

    output = step['output']
    # if output:
    #     logger.info('output: %s' % repr(output))

    for k, v in output.items():
        if v == 'status_code':
            g.var[k] = response['status_code']
            logger.info('%s: %s' %(k, repr(g.var[k])))
        elif v == 'text':
            g.var[k] = response['text']
            logger.info('%s: %s' %(k, repr(g.var[k])))
        elif k == 'json':
            sub = json2dict(output.get('json', '{}'))
            result = check(sub, response['json'])
            # logger.info('Compare json result: %s' % result)
            g.var = dict(g.var, **result['var'])
            logger.info('json var: %s' %(repr(result['var'])))
        elif k == 'cookies':
            sub = json2dict(output.get('cookies', '{}'))
            result = check(sub, response['cookies'])
            # logger.info('Compare json result: %s' % result)
            g.var = dict(g.var, **result['var'])
            logger.info('cookies var: %s' %(repr(result['var'])))


def before_send(data, kwargs):
    '''
    data: dict，格式如下：
        {'headers':{},
         'params': {},
         'data': {},
         'json': {},
         'files': 'file path'
        }

    kwargs: dict，其他参数
    '''
    # handle the request here

    return data, kwargs


def after_receive(response):
    '''
    response: dict, 格式如下：
    {'status_code': 200,
     'headers': {},
     '_cookies': '',  # 原始内容
     'cookies': {},   # dict 格式
     'content': b'',
     'text': '',
     'json': {}
     }
    '''
    # handle the response here

    return response