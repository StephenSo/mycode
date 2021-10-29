
def sub(a,b):
    print(a-b)

# function <-- block of code

def smart_sub(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)

    return inner

sub(6,10)

sub = smart_sub(sub)
sub(6,10)
