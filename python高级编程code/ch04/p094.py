def fuzzy_thing(**kw):
    if 'do_this' in kw:
        print 'ok i did'
    if 'do_that' in kw:
        print 'that is done'
    print 'errr... ok'

fuzzy_thing()

fuzzy_thing(do_this=1)

fuzzy_thing(do_that=1)

fuzzy_thing(hahahahaha=1)
