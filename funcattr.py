#!/usr/bin/python2

def foo():
    return True

def bar():
    'bar() does not do much'
    return True

foo.__doc__ = 'foo() does not do much'
foo.tester = '''
if foo():
    print 'passed'
else:
    print 'failed'
'''

for eachattr in dir():
    obj = eval(eachattr)
    if isinstance(obj,type(foo)):
        if hasattr(obj,'__doc__'):
            print '\nFunction "%s" has a doc
            string :\n\t%s' % (eachattr,obj.__doc__)
        if hasattr(obj,'tester'):
            print 'Function "%s" has a tester ....executing ' % eachAttr
            exec obj.tester

        else:
            print 'Function "%s" has no tester....skip
            ping ' % eachattr
    else:
        print '"%s" is not a function ' % eachattr


