#-*-coding:utf-8-*-

import math

print math.__name__
print math.__package__
print math.e
print math.pi
print math.acos(-1.0)  #������print math.acosh(10000)
print math.asin(1)     #������
print math.asinh(0)  
print math.atan(100000)
print "hypot", "=>", math.hypot(3.0, 4.0)
print "sqrt", "=>", math.sqrt(100)
print "pow", "=>", math.pow(2,10)
print "ceil",'=>', math.ceil(3.14)
print "floor", '=>', math.floor(4.12)
print "copysign",'=>', math.copysign(123,232)
print "fabs",'=>', math.fabs(-100)
print "factorial",'=>', math.factorial(3)
print "fmod",'=>',math.fmod(3,4)
print "trunc", '=>', math.trunc(12.334)

print "ceil", '=>', math.ceil(-4)
print "copysign", '=>',  math.copysign(1.0, -0.0)
print "fabs", '=>',  math.fabs(-1.1)

print "math.frexp(x)", '=>',math.frexp(1.7323)
print "math.fsum(iterable)", '=>',math.fsum([1,3,5,6,8])
print "math.isinf(x)", '=>',math.isinf(5)
print "math.gamma", '=>',math.gamma(10)


print "math.isnan(x)", '=>',math.isnan(1.0)
print "math.ldexp(x, i)", '=>',math.ldexp(3, 2)
print "math.modf(x)", '=>',math.modf(3.1415)
print "math.trunc(x)", '=>',math.trunc(3.1415)
print "math.exp(x)", '=>',math.exp(2)
print "math.expm1(x)", '=>',math.expm1(2)
print "math.log(x[, base])", '=>',math.log(4,2)
print "math.log1p(x)", '=>',math.log1p(2)
print "math.log10(x)", '=>',math.log10(2)
print "math.pow(x, y)", '=>',math.pow(2, 3)
print "math.sqrt(x)", '=>',math.sqrt(4)
print "math.acos(x)", '=>',math.acos(1)
print "math.asin(x)", '=>',math.asin(1)
print "math.atan(x)", '=>',math.atan(1)
print "math.atan2(y, x)", '=>',math.atan2(1, 2)
print "math.cos(x)", '=>',math.cos(1)
print "math.hypot(x, y)", '=>',math.hypot(3, 4)
print "math.sin(x)", '=>',math.sin(1)
print "math.tan(x)", '=>',math.tan(1)
print "math.degrees(x)", '=>',math.degrees(1)
print "math.radians(x)", '=>',math.radians(1)

math.isnan(x) => False
math.ldexp(x, i) => 12.0
math.modf(x) => (0.14150000000000018, 3.0)
math.trunc(x) => 3
math.exp(x) => 7.38905609893
math.expm1(x) => 6.38905609893
math.log(x[, base]) => 2.0
math.log1p(x) => 1.09861228867
math.log10(x) => 0.301029995664
math.pow(x, y) => 8.0
math.sqrt(x) => 2.0
math.acos(x) => 0.0
math.asin(x) => 1.57079632679
math.atan(x) => 0.785398163397
math.atan2(y, x) => 0.463647609001
math.cos(x) => 0.540302305868
math.hypot(x, y) => 5.0
math.sin(x) => 0.841470984808
math.tan(x) => 1.55740772465
math.degrees(x) => 57.2957795131
math.radians(x) => 0.0174532925199


print "math.erf(x)", '=>',math.erf(1)
print "math.erfc(x)", '=>',math.erfc(1)
print "math.gamma(x)", '=>',math.gamma(20)
print "math.lgamma(x)", '=>',math.lgamma(20)
print "math.pi", '=>',math.pi
print "math.e", '=>',math.e
