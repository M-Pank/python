import sys
args = sys.argv


a = open(args[1])
sphere = a.read()
result = sphere.split("center: [")[1].split("]")[0]
center = list(result.split(", "))
center = map(int, center)
center = list(center)

result = sphere.split("radius: ")[1].split("}")[0]
import re

radius  = re.findall("\d+\.\d+", result)
if len(radius) == 0:
    radius = re.search(r'\d+', result).group()
radius = float(*radius)

result = sphere.split("line: {[")[1].split("]")[0]
l1 = list(result.split(", "))
l1 = map(float, l1)
l1 = list(l1)

result = sphere.split("], [")[1].split("]")[0]
l2 = list(result.split(", "))
l2 = map(float, l2)
l2 = list(l2)






def sphere_line_intersection(l1, l2, sp, r):

    def square(f):
        return f * f
    from math import sqrt


    p1 = p2 = None

    a = square(l2[0] - l1[0]) + square(l2[1] - l1[1]) + square(l2[2] - l1[2])
    b = 2.0 * ((l2[0] - l1[0]) * (l1[0] - sp[0]) +
               (l2[1] - l1[1]) * (l1[1] - sp[1]) +
               (l2[2] - l1[2]) * (l1[2] - sp[2]))

    c = (square(sp[0]) + square(sp[1]) + square(sp[2]) + square(l1[0]) +
            square(l1[1]) + square(l1[2]) -
            2.0 * (sp[0] * l1[0] + sp[1] * l1[1] + sp[2] * l1[2]) - square(r))

    i = b * b - 4.0 * a * c

    if i < 0.0:
        print("Коллизий не найдено")
    elif i == 0.0:
        p[0] = 1.0

        mu = -b / (2.0 * a)
        p1 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )
        print(p1[0], p1[1], p1[2], sep="\n")
    elif i > 0.0:
        mu = (-b + sqrt(i)) / (2.0 * a)
        p1 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

        mu = (-b - sqrt(i)) / (2.0 * a)
        p2 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

        print(p1[0], p1[1], p1[2], p2[0], p1[1], p2[2], sep="\n")

sphere_line_intersection(l1, l2, center, radius)

