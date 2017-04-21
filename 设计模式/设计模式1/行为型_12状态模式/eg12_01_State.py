# -*-coding:utf-8 -*-
import random

__author__ = 'raychang'


class IState:
    def convertState(self, context, mode):
        pass

    def save(self, context):
        pass

    def modify(self, context):
        pass

    def add(self, context):
        pass

    def view(self, context):
        pass


class Context:
    PREVIEW_MODE = 0
    EDIT_MODE = 1

    def changeState(self, state):
        self.state = state

    def doWork(self, mode):
        print u'======================='
        self.state.convertState(self, mode)
        self.state.add(self)
        self.state.save(self)
        self.state.modify(self)
        self.state.view(self)
        print u'======================='


class PreviewState(IState):
    def convertState(self, context, mode):
        if mode == context.EDIT_MODE:
            context.changeState(EditState())

    def save(self, context):
        print u'预览模式不支持【保存】...'

    def modify(self, context):
        print u'预览模式不支持【修改】...'

    def add(self, context):
        print u'预览模式不支持【新增】...'

    def view(self, context):
        print u'预览模式【查看】...'


class EditState(IState):
    def convertState(self, context, mode):
        if mode == context.PREVIEW_MODE:
            context.changeState(PreviewState())

    def save(self, context):
        print u'编辑模式【保存】...'

    def modify(self, context):
        print u'编辑模式【修改】...'

    def add(self, context):
        print u'编辑模式【新增】...'

    def view(self, context):
        print u'编辑模式【查看】...'


if __name__ == '__main__':
    context = Context()
    context.changeState(EditState())
    for i in xrange(1, 10):
        r = random.randint(0, 1)
        print u'当前模式:%s' % (u'预览模式' if r == 0 else u'编辑模式')
        context.doWork(r)
