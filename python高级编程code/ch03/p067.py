# 1- looking for definition

'''
if hasattr(MyClass, 'attribute'):
    attribute = MyClass.attribute
    AttributeClass = attribute.__class__

    # 2 - does attribute definition has a setter ?    
    if hasattr(AttributeClass, '__set__'):
        # let's use it
        AttributeClass.__set__(attribute, instance, value)
        return
# 3 - regular way
instance_of.__dict__['attribute'] = value
print instance_of.__dict__

'''
