import sys
from pathlib import Path
import smtplib
import poplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from sweetest.globals import g
from sweetest.config import mail_server, mail_port, mail_username, mail_password, mail_receiver, mail_subject, pop3_server, pop3_port
from sweetest.lib.log import logger
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


class Mail(object):
    def __init__(self):
        super(Mail, self).__init__()
        self.msg = None
        self.server = None
        self.mail()
        if mail_username.find('gmail') != -1:
            self.authTLS()
        else:
            self.authSSL()

    def mail(self):
        '''
        定义邮件对象，包括内容和附件
        :return: 邮件对象
        '''
        # 定义带附件的邮件对象
        msg = MIMEMultipart()
        msg['Subject'] = mail_subject
        msg['From'] = mail_username
        msg['To'] = ','.join(mail_receiver.split(';'))

        # 邮件内容
        fp1 = open(Path('htmlreport/image1.png'), 'rb')
        image1 = MIMEImage(fp1.read())
        image1.add_header('Content-ID', '<image1>')
        fp1.close()
        fp2 = open(Path('htmlreport/image2.png'), 'rb')
        image2 = MIMEImage(fp2.read())
        image2.add_header('Content-ID', '<image2>')
        fp2.close()

        # 附件
        att1 = self.makeAttr(g.htmlreport_file, "Testing Report.html")
        att2 = self.makeAttr(g.report_file, "Testing Report.xlsx")

        # 邮件正文
        htm = '''
        <html>
            <head></head>
            <body>
                <br><img src='cid:image1'></br>
                <br><img src='cid:image2'></br>
            </body>
        </html>
        '''
        html = MIMEText(htm, 'html', _charset='utf-8')

        # msg.attach(Body1)
        msg.attach(image1)
        msg.attach(image2)
        msg.attach(html)
        msg.attach(att1)
        msg.attach(att2)

        self.msg = msg.as_string()

    def makeAttr(self, file, filename):
        report = open(file, 'rb')
        body = report.read()
        attr = MIMEText(body, 'base64', 'utf-8')
        attr['Content-Type'] = "application/octet-stream"
        attr['Content-Disposition'] = 'attachment;filename="' + filename + '"'
        report.close()
        return attr

    def authSSL(self):
        '''
        SSL连接方式的验证
        :return:smtp实例
        '''
        s = smtplib.SMTP_SSL(mail_server, mail_port)
        try:
            s.login(mail_username, mail_password)
        except:
            logger.error("验证失败！")
            sys.exit(1)
        self.server = s

    def authTLS(self):
        '''
        TLS连接方式的验证
        :return:smtp实例
        '''
        s = smtplib.SMTP()
        s.connect(mail_server, mail_port)

        code = s.ehlo()[0]
        usesesmtp = 1
        if not (200 <= code <= 299):
            usesesmtp = 0
            code = s.helo()[0]
            if not (200 <= code <= 299):
                raise smtplib.SMTPHeloError(code, resp)

        if usesesmtp and s.has_extn('starttls'):
            s.starttls()
            code = s.ehlo()[0]
            if not (200 <= code <= 299):
                sys.exit(5)
        if s.has_extn('auth'):
            try:
                s.login(mail_username, mail_password)
            except:
                logger.error("验证失败！")
                sys.exit(1)
        self.server = s

    def sendmail(self):
        '''
        发送邮件
        '''
        try:
            self.server.sendmail(mail_username, mail_receiver, self.msg)
            self.server.quit()
        except:
            logger.info("***邮件没有发送成功！***")
            sys.exit(1)
        else:
            logger.info("***邮件发送成功！***")


class Pop3(object):
    def __init__(self):
        super(Pop3, self).__init__()
        self.server = poplib.POP3(pop3_server)

    def conn(self):
        self.server.user(mail_username)
        self.server.pass_(mail_password)

    def exit(self):
        self.server.quit()

    def retrmail(self):
        '''
        获取最新一份邮件
        '''
        self.conn()
        resp, mails, octets = self.server.list()
        resp, lines, octets = self.server.retr(len(mails))
        self.exit()
        return lines

    def decodemail(self, lines):
        '''
        邮件解码
        '''
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        return msg

    def retrline(self, lines, n):
        '''
        获取邮件第n行的内容
        :param lines: 邮件内容
        :param n: 行数
        :return: 返回第n行的内容内容
        '''
        line = lines[n].decode('utf-8')
        logger.info(line)
        return line









