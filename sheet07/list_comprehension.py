import random
import math
import matplotlib.pyplot as plt

def generate_random_point_in_square(length):
    """
    Generate a random point in a square of a given side length centered around the origin with the sides aligned with x- and y-axis.
    """
    return tuple([length*random.uniform(-0.5, 0.5), length*random.uniform(-0.5, 0.5)])

def distance(p1, p2):
    """
    Measures the Euclidean distance between the points p1 and p2 in 2D.
    """

    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)


def point_in_circle(p, center=[0,0], radius=None):
    """
    Checks if the provided point p lies in a circle of a given radius around the provided center.
    """
    length = distance(center, p)

    if length <= radius:

        print("liegt im Bereich")
        return True
    else:
        print("leigt nicht im Bereich")
        return False
i= 1
full_list_of_points = []

while i < 1000:

    full_list_of_points.append(generate_random_point_in_square(2.0))
    i = i+1

filtered_list_of_points = []

while i <= len(full_list_of_points):

    if point_in_circle(full_list_of_points[i]) == True:
        filtered_list_of_points.append(full_list_of_points[i])
        i = i+1
    else:
        i =i+1

print(len(filtered_list_of_points)/(len(full_list_of_points)-len(filtered_list_of_points)))
# TODO: Generate separate lists of the x- and y-values of full_list_of_points and filtered_list_of_points
x_values_full = 
y_values_full = 

x_values_filtered =
y_values_filtered =

plt.scatter(x_values_full, y_values_full)
plt.scatter(x_values_filtered, y_values_filtered)
plt.show()
