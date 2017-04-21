def fibonacci():
     a, b = 0, 1
     while True:
         yield b
         a, b = b, a + b

if __name__ == '__main__':
     fib = fibonacci()
     print fib.next()
     print fib.next()
     print fib.next()
     print [fib.next() for i in range(10)]
