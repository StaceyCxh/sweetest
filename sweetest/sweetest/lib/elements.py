from sweetest.lib.log import logger
from sweetest.globals import g


def have_elem(page, element):
    ele = element.split('#')

    if len(ele) >= 2:
        _el = ele[0] + '#'
    else:
        _el = element
    # 如果有<>,说明元素是变量，则不判断
    if '<' in _el:
        return '', '通用' + '^' + element
    # 在元素定位表中查询
    elem = page + '^' + _el
    if g.elements.get(elem, ''):
        return g.elements[elem]['custom'], page + '^' + element
    else:
        # 查不到就在通用里查,还是查不到就报错
        elem = '通用' + '^' + _el
        if g.elements.get(elem, ''):
            return g.elements[elem]['custom'], '通用' + '^' + element
        else:
            logger.warning('Page:%s element:%s is not exist' %
                            (page, element))
            return '', element


def get_elem(element, flag=False):
    ele = element.split('#')
    # #号后面的值，即用户输入的变量
    _v = []
    # 支持多个变量替代，但是顺序要对应
    if len(ele) >= 2:
        _el = ele[0] + '#'
        _v = ele[1:]
    else:
        _el = element
    el = g.elements.get(_el, '')
    if not el:
        if flag:
            return _el, ''
        return _el, element.split('#', 1)[-1]
    value = el['value']
    for v in _v:
        value = value.replace('#', v, 1)
    return el, value
