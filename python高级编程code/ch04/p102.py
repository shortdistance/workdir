import warnings
class SomeClass(object):            # version 1.5
    def run_script(self, script, context):
        warnings.warn(("'run_script' will be replaced "
                       "by 'run' in version 2"), 
                      DeprecationWarning)
        return self.run(script, context)
    def run(self, script, context=None):
        print 'doing the work'

SomeClass().run_script('a script', {})
