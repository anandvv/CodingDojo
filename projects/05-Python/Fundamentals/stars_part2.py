from types import *

def draw_stars(x):
    stars = ""
    for item in x:
        # print type(item)
        if type(item) is IntType:
            for i in range(0, item):
                stars += "*"
            print(stars)
            stars = ""
        elif type(item) is StringType:
            for i in range(0, len(item)):
                stars += item[0].lower()
            print(stars)
            stars = ""


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
