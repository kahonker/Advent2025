from itertools import combinations
from shapely.geometry import Polygon
with open("input9", "r") as f:
    data = list(map(lambda i: tuple(map(lambda j: int(j), i.split(","))), f.read().split("\n")))

print(data)

outer_poly = Polygon(data)

# vertical_sides = set([])
# horizontal_sides = set([])
#
#
# def check_sides(sides):
#     checking_vertical_point1 = False
#     checking_vertical_point2 = False
#     checking_horizontal_point1 = False
#     checking_horizontal_point2 = False
#     for side1 in sides:
#         # for side2 in vertical_sides | horizontal_sides:
#         # 	if side2[0][0] <= side1[0][0] <= side1[1][0] <= side2[1][0] and side2[0][1] <= side1[0][1] <= side1[1][1] <= side2[1][1]:
#         # 		return True
#         for side2 in vertical_sides:
#             if side2[0][1] <= side1[0][1] <= side2[1][1]:
#                 checking_vertical_point1 = True
#             if side2[0][1] <= side1[1][1] <= side2[1][1]:
#                 checking_vertical_point2 = True
#             if checking_vertical_point1 and checking_vertical_point2: break
#         for side2 in horizontal_sides:
#             if side2[0][0] <= side1[0][0] <= side2[1][0]:
#                 checking_horizontal_point1 = True
#             if side2[0][0] <= side1[1][0] <= side2[1][0]:
#                 checking_horizontal_point2 = True
#             if checking_horizontal_point1 and checking_horizontal_point2: break
#         if checking_horizontal_point1 and checking_horizontal_point2 and checking_vertical_point1 and checking_vertical_point2: return True
#     return False
#
# def check_inside(sides):
#     return_set = set([])
#     for side1 in sides:
#         for side2 in vertical_sides | horizontal_sides:
#             if side2[0][0] <= side1[0][0] <= side1[1][0] <= side2[1][0] and side2[0][1] <= side1[0][1] <= side1[1][1] <= side2[1][1]:
#                 return_set.add(side1)
#
#     return return_set
#
# def check_rectangle(coord1, coord2):
#     sides: set = set([])
#     sides.add(tuple(sorted((coord1, (coord2[0], coord1[1])), key=lambda i: i[0])))
#     sides.add(tuple(sorted((coord1, (coord1[0], coord2[1])), key=lambda i: i[0])))
#     sides.add(tuple(sorted((coord2, (coord1[0], coord2[1])), key=lambda i: i[0])))
#     sides.add(tuple(sorted((coord2, (coord2[0], coord1[1])), key=lambda i: i[0])))
#     if (9,5) in [coord1, coord2] and (2,3) in [coord1, coord2]: print(check_inside(sides))
#     if len(sides) < 4:
#         print("check1")
#         return False
#     # elif len(sides & vertical_sides & horizontal_sides) >= 3: return True
#     elif len(check_inside(sides)) <= 1:
#         return False
#     else: return check_sides((sides - vertical_sides) - horizontal_sides)
#
# def get_area(item0, item2):
#     x = abs(item0[0] - item2[0]) + 1
#     y = abs(item0[1] - item2[1]) + 1
#     return x * y
#
# for i in range(0, len(data), 2):
#     side = tuple(sorted((data[i], data[i+1]), key=lambda j: j[0]))
#     horizontal_sides.add(side)
#
# for i in range(1, len(data), 2):
#     side = tuple(sorted((data[i], data[(i+1) % (len(data) -1)]), key=lambda j: j[0]))
#     vertical_sides.add(side)
#
# print(vertical_sides)
# print(horizontal_sides)

def get_area(item0, item2):
    x = abs(item0[0] - item2[0]) + 1
    y = abs(item0[1] - item2[1]) + 1
    return x * y

def check_rectangle(coord1, coord2):
    sides = []
    sides.append(coord1)
    sides.append((coord2[0], coord1[1]))
    sides.append(coord2,)
    sides.append((coord1[0], coord2[1]))
    print(sides)
    inner_poly = Polygon(sides)
    return outer_poly.contains(inner_poly)

biggest = 0

for i in combinations(data, 2):
    if check_rectangle(i[0], i[1]):
        area = get_area(i[0], i[1])
        if area > biggest:
            print(i)
            biggest = area


print(biggest)