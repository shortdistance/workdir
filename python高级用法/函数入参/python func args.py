__author__ = 'Raychang'


def fun_var_args_kwargs(farg, *args, **kwargs ):
    for value in args:
        print "another arg:", value

    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

    print farg

ll = [ 1,3,3,23,None,'23','hello world']
dd = dict(user='zhangleid', age=10, score='100')
fun_var_args_kwargs(100, *ll, **dd)
