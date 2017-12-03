import os
import smtplib
import unittest
#HTMLTestRunner是基于unittest框架的一个扩展,可以自己在网上自行下载
import time
from email.header import Header

from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f=open(path,'rb')#具体的内容
    mail_body = f.read()#读取html文件的内容作为邮件的正文
    f.close()

    #要想发邮件,要把二进制的内容转为MIME格式
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("自动化测试报告",'utf-8')
    #如果想用客户端软件或者自己写代码登陆邮箱,很多类型的邮箱需要单独设置一个客户端授权码,为了邮箱安全着想
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = '253711752@qq.com'
    #发送邮件的手动步骤:1.打开登陆页面,链接邮箱服务器,想要链接服务器,首先要搞清楚网络传输协议,http,https,ftp,socket
    #发邮件的协议,一般有三种,查看你的邮箱支持那种协议,126支持pop3,smtp,imap,选择一种传输协议,用来发邮件,smtp
    smtp = smtplib.SMTP()#实例化一个SMTP类的对象
    smtp.connect('smtp.126.com')#链接126邮箱的服务器的地址

    # 2.登陆邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    # 3.发送邮件
    #注意msg是MIME类型,需要转成string类型才能发送出去
    smtp.sendmail('bwftest126@126.com','253711752@qq.com',msg.as_string())
    # 4.退出邮箱
    smtp.quit()
    print('email has sent out!')


if __name__ == '__main__':
    #strftime()通过这个方法可以定义时间格式
    #Y year年
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./day5','*Test.py')
    #unittest.TextTestRunner()文本测试用例运行器
    #现在用html 的测试用例运行器,html的测试用例运行器最终会生成一个html格式的测试报告,
    base_path=os.path.dirname(__file__)
    path=base_path + '/report/report'+now+'.html'
    file = open(path,'wb')
    HTMLTestRunner(stream=file, title="海盗商城的测试报告", description="测试环境:window server 2008 + Chrome").run(suite)
    file.close()
    #我们要把html报告作为邮件正文,发送邮件
    send_mail(path)
    #这时生成的测试报告,只显示类名和方法名,只能给专业人士看,应该把相关的手动测试用例的标题加到我们的测试报告中,自动化测试用例是从手工测试用例中挑出来的,手工用例怎么写我们就怎么编码,所以我们的代码里应该可以体现手工测试用例的标题
    #新的测试报告会覆盖原来的测试报告,如果想把所有的测试报告保存起来怎么做,加一个时间戳,按照当前时间计算一个数字,把数字作为文件名的一部分,就避免了文件名重复的问题,
    #现在我们的html格式的测试报告生成了,发邮件提醒
