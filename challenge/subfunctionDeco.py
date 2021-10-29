
def smarter_homerfunc(func):
    def inner(food="salad"):
        print('In the smarter function:',end='')
        if food != "salad":
            print(f"Everyone likes {food}")
        else:
            func(food)
    return inner