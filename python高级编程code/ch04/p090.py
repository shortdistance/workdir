class DB(object):
    is_connected = False
    has_cache = False


database = DB()
print database.has_cache

if database.is_connected:
    print "That's a powerful class"
else:
    print "No wonder..."
