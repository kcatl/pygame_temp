def minmax(test,*args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res = arg 
    return res

def lessthan(x,y): return x < y
def grterthan(x,y):return x > y

print minmax(lessthan,4,3,2,1,3,2)
print minmax(grterthan,4,3,2,1,2,3)
