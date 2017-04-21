# -*-coding:utf-8-*-
import numpy as np

# help(np)

a = np.arange(15).reshape(5, 3)
print a
print a.ravel()  # 数组元素摊开
print a[0][2]  # 打印第一行第三列的数组元素
print a[0, 0]  # 打印第一行，第一列的数组元素
print a[:, 1]  # 打印二维数组的第二列
print a[1, :]  # 打印二数组的第二行
print a.shape  # 数组的形状
print a.ndim  # 数组的维度
print a.dtype.name  # 数组元素的类型
print a.itemsize  # 存储数组的字节数
print a.size  # 数组的长度
print type(a)  # 数组元素的类型
print '~~~~~~~~~~~~~~'
print a.flags  # Information about the memory layout of the array.
print a.strides  # Tuple of bytes to step in each dimension when traversing an array.
print a.data  # Python buffer object pointing to the start of the array’s data.
print a.nbytes  # Total bytes consumed by the elements of the array.
print a.base  # Base object if memory is from some other object.
print a.tolist()

b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print b.resize((5, 3))
print b.ravel()
b.reshape(3, 5)

print '~~~~~~~c~~~~~'
c = np.loadtxt('mydata.txt', dtype='float', delimiter=' ', usecols=(0,1,4))
print c