def my_generator():
    try:
        yield 'something' 
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print "ok let's clean"
        
gen = my_generator()
gen.next()

gen.throw(ValueError('mean mean mean'))

gen.close()

gen.next()
