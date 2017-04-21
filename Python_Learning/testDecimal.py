#-*-coding:utf-8-*-
import decimal

d1 = decimal.Decimal(1)
print d1

print d1.adjusted()


# -*- coding:UTF-8 -*-
import decimal
decimal.getcontext().prec=1000 #
a=decimal.Decimal(3)**decimal.Decimal(123323)
b=decimal.Decimal('0.13')**decimal.Decimal('324325')
print('\t{}\n*\n\t{}\n=\n\t{}'.format(a,b,a*b))

print('\t\n*\n\t{}\n=\n\t{}  {}'.format(123,'1234','hello world'))


print decimal.getcontext