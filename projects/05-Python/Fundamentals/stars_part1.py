def draw_stars(x):
    stars = ""
    for item in x:
        for i in range(0, item):
            stars += "*"
        print(stars)
        stars = ""


x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)
