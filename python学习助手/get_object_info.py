# !/usr/bin/python
# coding=utf-8

# Python -V:Python 2.6
# filename:get_object_info.py

__author__ = 'Tattoo'
__date__ = '2013.07.09'

import en_2_zh

SPLITE_LENGTH = 60
SPLITE_CHAR = '*'


def _my_print(title, text, is_none_prompt=False):
    if is_none_prompt is False and (text is None or text.strip() is ''):
        return

    width = len(title)
    half_width = (SPLITE_LENGTH - width) / 2
    # print SPLITE_CHAR*half_width + text + SPLITE_CHAR * half_width
    print os.linesep + SPLITE_CHAR * half_width + title + SPLITE_CHAR * half_width
    print text
    # print SPLITE_CHAR * SPLITE_LENGTH + "\n\n"


def _get_doc(cls):
    try:
        return cls.__doc__
    except:
        return ''


def _get_name(cls):
    try:
        return cls.__name__
    except:
        return ''


def _get_dict(cls):
    try:
        return str(cls.__dict__)
    except:
        return ''


def _get_module(cls):
    try:
        return cls.__module__
    except:
        return ''


def _get_base(cls):
    try:
        return cls.__base__
    except:
        return ''


def _do_import_module(cls_str):
    try:
        return __import__(cls_str)
    except ImportError:
        return None


def _do_import_attr(cls_str, attr_str):
    try:
        module = __import__(cls_str, globals(), locals(), [attr_str], -1)
        # object = _temp.object
        return module
        # return __import__(attr_str, cls_str)#, fromlist=[attr_str])
    except:
        return None


def _get_file(cls):
    try:
        return cls.__file__
    except:
        return ''


def _print_cls_info(cls):
    # text = dir(my_cls)
    # print text
    print('这是一个模块')
    _my_print("模块名称列表dir(" + str(cls) + "):", ', '.join(dir(cls)))
    doc = _get_doc(cls)
    # _my_print("文档__doc__:" + doc)
    _my_print("文档__doc__翻译:", en_2_zh.get_translate_mix_text(doc))
    _my_print("名称__name__:", _get_name(cls))
    _my_print("字典属性：__dict__:", _get_dict(cls))
    _my_print("模块__module__:", _get_module(cls))
    _my_print("__base__:", _get_base(cls))
    _my_print("__file__:", _get_file(cls))


def _print_attr_info(attr):
    print attr
    print dir(attr)
    print('这是一个属性')
    _my_print("模块名称列表dir(" + str(attr) + "):", ', '.join(dir(attr)))
    doc = _get_doc(attr)
    # _my_print("文档__doc__:" + doc)
    _my_print("文档__doc__翻译:", en_2_zh.get_translate_mix_text(doc))
    _my_print("名称__name__:", _get_name(attr))
    _my_print("字典属性：__dict__:", _get_dict(attr))
    _my_print("模块__module__:", _get_module(attr))
    _my_print("__base__:", _get_base(attr))
    _my_print("__file__:", _get_file(attr))


def get_class_info(cls):
    _my_print('cls = ' + cls, cls)
    # print dir(cls)
    # my_cls = __import__(cls)
    my_cls = _do_import_module(cls)
    if my_cls is not None:
        _print_cls_info(my_cls)
    else:
        index = cls.rindex('.')
        cls2 = cls[:index]
        attr = cls[(index + 1):]
        my_cls2 = _do_import_attr(cls2, attr)
        print()
        if my_cls2 is not None and attr is not None:
            print str(my_cls2)
            _print_attr_info(my_cls2.__dict__[attr])
        else:
            print '无法导入此模块'


def test_doc():
    text = '''
        __stdin__ -- the original stdin; don't touch!  
        __stdout__ -- the original stdout; don't touch!  
        __stderr__ -- the original stderr; don't touch!  
        __displayhook__ -- the original displayhook; don't touch!  
        __excepthook__ -- the original excepthook; don't touch!  
          
        Functions:  
          
        displayhook() -- print an object to the screen, and save it in __builtin__._  
        excepthook() -- print an exception and its traceback to sys.stderr  
        exc_info() -- return thread-safe information about the current exception  
        exc_clear() -- clear the exception state for the current thread  
        '''
    import sys

    print en_2_zh.test(_get_doc(sys))


import sys, os

if __name__ == "__main__":
    #cls = sys.argv[1]
    cls = 'sys'
    get_class_info(cls)

    # test_doc()
