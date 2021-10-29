import subfunctionDeco

@subfunctionDeco.smarter_homerfunc
def homer(food="salad"):
    print('From the original function:',end='')
    print(f"No one likes {food}")

homer()
#homer = smarter_homerfunc(homer)
homer('Beer')
homer()
homer('Pie')
homer('salad')


