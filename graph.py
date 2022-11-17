import matplotlib.pyplot

# draw a graph for the given data
points = []

morePoints = True
while morePoints:
    x = input("Enter x: ")
    if x == "":
        morePoints = False
    y = input("Enter y: ")
    if y == "":
        morePoints = False
    if morePoints:
        points.append((float(x), float(y)))
    

matplotlib.pyplot.plot([x for x, y in points], [y for x, y in points])
matplotlib.pyplot.show()
