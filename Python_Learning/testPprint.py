#-*-coding:utf-8-*-
import pprint

data = {
'123':"this is a string", '124':[1, 2, 3, 4], '125':("more tuples",
1.0, 2.3, 4.5), '126':"this is yet another string"
}

p = pprint.PrettyPrinter()
p.pprint(data)