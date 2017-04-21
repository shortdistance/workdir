# -*- encoding=utf-8 -*-


class Receiver:
    def readMail(self, message):
        print u'收件人读取信件: %s' % message


class IPost:
    def sendMail(self,message):
        pass

class Post(IPost):
    def __init__(self, receiver):
        self.receiver = receiver

    def sendMail(self,message):
        print u'邮局将信件发送给收件人...'
        self.receiver.readMail(message)

class Invoker:
    def setPost(self, post):
        self.post = post

    def postMail(self,message):
        print u'发信人投送信件给邮局...'
        self.post.sendMail(message)

if __name__ == '__main__':
    receiver = Receiver()
    post = Post(receiver)
    invoker = Invoker()
    invoker.setPost(post)
    message = u'你好,好久不见,最近工作忙吗??'
    invoker.postMail(message)