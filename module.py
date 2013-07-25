# a module that list the namespaces of other modules

verbose = 1

def listing(module):
    if verbose:
        print "-" * 30
        print "name:",module.__name__,"file:",module.__file__
        print "-" * 30
    
    count = 0

    for attr in module.__dict__keys():
        print "%20d" %(count,attr),
        if attr[0:2] ==  "__":
           print "<bulit-in name>"
        else:
            print getattr(module,attr)
        count = count + 1

    if verbose:
        print "-" * 30
        print module.__name__ , "has %d names" % count
        print "-" * 30

if __name__ == "__main__":
    import mydir
    listing (mydir)

