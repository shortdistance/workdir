# 1- looking for definition

'''
if hasattr(MyClass, 'attribute'):
    attribute = MyClass.attribute
    AttributeClass = attribute.__class__

    # 2 - does attribute definition have a getter ?    
    readable = hasattr(AttributeClass, '__get__')

    # 3 - does attribute definition have a setter,
    #     or 'attribute' is not found in __dict__
    writable = (hasattr(AttributeClass, '__set__') or 'attribute' not in instance.__dict__)

    if readable and writable:
        # 4 - call the descriptor 
        return AttributeClass.__get__(attribute, instance, MyClass)

# 5 - regular access with __dict__
return instance.__dict__['attribute']

'''