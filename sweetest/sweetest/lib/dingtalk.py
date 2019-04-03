import json
import requests
from sweetest.lib.log import logger
from sweetest.globals import g
from sweetest.config import webhook, title
from sweetest.lib.utility import isNotNull


try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError


class DingTalk(object):
    '''
    钉钉机器人类，可以发送markdown
    '''

    def __init__(self):
        super(DingTalk, self).__init__()
        self.webhook = webhook
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}

    def send_markdown(self):
        """
        markdown类型
        :param title: 首屏会话透出的展示内容
        :param text: markdown格式的消息内容
        :return: 返回消息发送结果
        """
        text = '# ** 自动化测试报告 **\n ' + \
               '* 开始执行时间：' + '**' + g.results['beginTime'] + '**' + ' ;\n' + \
               '* 测试用例总数：' + '**' + str(g.results['testAll']) + '**' + ' ;\n' + \
               '* 测试通过：' + '**' + str(g.results['testPass']) + '**' + ' ;\n' + \
               '* 测试失败：' + '**' + str(g.results['testFail']) + '**' + ' ;\n' + \
               '* 测试跳过：' + '**' + str(g.results['testSkip']) + '**' + ' ;\n' + \
               '* 运行时间：' + '**' + str(g.results['totalTime']) + '**' + ' 。 \n' + \
               '> ![自动化](http://www.11506.com/uploadfile/2018/1024/20181024102305336.jpg)\n'

        if isNotNull(title) and isNotNull(text):
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": title,
                    "text": text
                },
                "at": {}
            }

            logger.info("markdown类型：%s" % data)
            return self.post(data)
        else:
            logger.error("markdown类型中消息标题或内容不能为空！")
            raise ValueError("markdown类型中消息标题或内容不能为空！")

    def post(self, data):
        """
        发送消息（内容UTF-8编码）
        :param data: 消息数据（字典）
        :return: 返回发送结果
        """
        post_data = json.dumps(data)
        try:
            response = requests.post(self.webhook, headers=self.headers, data=post_data)
        except requests.exceptions.HTTPError as exc:
            logger.error("消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logger.error("消息发送失败，HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logger.error("消息发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logger.error("消息发送失败, Request Exception!")
            raise
        else:
            try:
                result = response.json()
            except JSONDecodeError:
                logger.error("服务器响应异常，状态码：%s，响应内容：%s" % (response.status_code, response.text))
                return {'errcode': 500, 'errmsg': '服务器响应异常'}
            else:
                logger.debug('发送结果：%s' % result)
                if result['errcode']:
                    error_data = {"msgtype": "text", "text": {"content": "钉钉机器人消息发送失败，原因：%s" % result['errmsg']},
                                  "at": {"isAtAll": True}}
                    logger.error("消息发送失败，自动通知：%s" % error_data)
                    requests.post(self.webhook, headers=self.headers, data=json.dumps(error_data))
                return result
