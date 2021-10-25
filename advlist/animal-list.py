#!/usr/bin/env python3

def main():

    # create a list called animals
    animals = ["Fox","Fly","Ant","Bee","Cod","Cat","Dog","Yak","Cow","Hen","Koi","Hog","Jay","Kit"]
    x = range(animals.__len__())
    for n in x:
        print(animals[n],' ',end='')
    

main()