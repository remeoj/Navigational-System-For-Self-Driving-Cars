import time
import tkinter as tk
from rc_driver_helper import *
from model import NeuralNetwork


def create_map(grid1):
    for i in range(0, 7):
        inner_map = []
        # map.append(i)
        for j in range(0, 7):
            if (i == 0 or i == 6) and (j % 2 == 0):
                inner_map.append(3)
            elif (2 <= i <= 4) and (j % 2 == 0):
                inner_map.append(3)
            else:
                inner_map.append(0)
        grid1.append(inner_map)


def print_map(grid1):
    # Simple print out function for 2D array
    for r in grid1:
        for c in r:
            print(c, end=" ")
        print()
    print()


# Function to move a car on the grid vertically
def vert_direction(path1, vertical_pos, horizontal_pos, vertDirection):
    # Moves car to proper Y direction
    # distanceY = distanceY - 1
    if vertDirection:
        vertical_pos = vertical_pos - 1  # Moves car up grid
        path1.append([vertical_pos, horizontal_pos])
    else:
        vertical_pos = vertical_pos + 1  # Moves car down grid
        path1.append([vertical_pos, horizontal_pos])
    return vertical_pos


# Function to move a car on the grid horizontally
def horiz_direction(path1, vertical_pos, horizontal_pos, horizDirection):
    # Moves car to proper Y direction
    # Boolean to check for center of the grid
    if horizDirection:
        horizontal_pos = horizontal_pos - 1  # Moves car left grid
        path1.append([vertical_pos, horizontal_pos])
    else:
        horizontal_pos = horizontal_pos + 1  # Moves car right grid
        path1.append([vertical_pos, horizontal_pos])
    return horizontal_pos


# Function to create path for car
def car_path(car_x, car_y, grid_var, distance_y, distance_x, intersection_bool,
             vertDirection, horizDirection, obstacle):
    path = []
    route_pos_x = car_x
    route_pos_y = car_y

    # The following lines create the path that the car is going to traverse
    # Initial movement from starting place
    if car_y == 0 or car_y == len(grid_var) - 1:
        route_pos_y = vert_direction(path, route_pos_y, route_pos_x, vertDirection)
        distance_y = distance_y - 1
    else:
        route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, horizDirection)
        distance_x = distance_x - 1

    if intersection_bool and car_x == obstacle[1] and car_x == 1:
        for i in range(2):
            route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, False)
            # distance_x = distance_x - 1
    elif intersection_bool and car_x == obstacle[1] and car_x == 3:
        for i in range(2):
            route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, horizDirection)
            # distance_x = distance_x - 1
    elif intersection_bool and car_x == obstacle[1] and car_x == 5:
        for i in range(2):
            route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, True)
            # distance_x = distance_x - 1
    elif intersection_bool:
        while distance_x > 1 or distance_y > 0:
                # Moves car to proper X direction
                if distance_x > 1:
                    distance_x = distance_x - 1  # Decrements total horizontal distance that needs to be traversed
                    route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, horizDirection)
                    continue
                # Moves car to proper Y direction
                if distance_y > 0:  # Stops car on the inner 6x6  grid
                    distance_y = distance_y - 1  # Decrements total vertical distance that needs to be traversed
                    route_pos_y = vert_direction(path, route_pos_y, route_pos_x, vertDirection)
                    continue

    # Following movements of the car after starting place
    if destinationY == 0 or destinationY == len(grid_var) - 1:  # In this case, the destination is either at the top or bottom of the grid
        while distance_x > 0 or distance_y > 1:
                # Moves car to proper Y direction
                if distance_y > 1:
                    distance_y = distance_y - 1
                    route_pos_y = vert_direction(path, route_pos_y, route_pos_x, vertDirection)
                    continue
                # Moves car to proper X direction
                if distance_x > 0:
                    distance_x = distance_x - 1
                    route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, horizDirection)
                    continue

        if intersection_bool and car_x == obstacle[1] and car_x == 1:
            for i in range(2):
                route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, True)
        elif intersection_bool and car_x == obstacle[1] and car_x == 3:
            for i in range(2):
                route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, horizDirection)
        elif intersection_bool and car_x == obstacle[1] and car_x == 5:
            for i in range(2):
                route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, False)
        vert_direction(path, route_pos_y, route_pos_x, vertDirection)  # Moves car up or down to the destination

    else:  # In this case, the destination is either at the left or right of the grid
        while distance_x > 1 or distance_y > 0:
                # Moves car to proper Y direction
                if distance_y > 0:  # Stops car on the inner 6x6  grid
                    distance_y = distance_y - 1  # Decrements total vertical distance that needs to be traversed
                    route_pos_y = vert_direction(path, route_pos_y, route_pos_x, vertDirection)
                    continue
                # Moves car to proper X direction
                if distance_x > 1:
                    distance_x = distance_x - 1  # Decrements total horizontal distance that needs to be traversed
                    route_pos_x = horiz_direction(path, route_pos_y, route_pos_x, horizDirection)
                    continue
        horiz_direction(path, route_pos_y, route_pos_x, horizDirection)  # Moves car left or right to the destination
    return path


# Function to show path on the grid
def update_map(path1):
    # print(grid)
    # print(path1)
    for i in range(0, len(path1)):
        temp_row = path1[i][0]
        temp_col = path1[i][1]
        grid[temp_row][temp_col] = 4


# Function for moving car
def move_car(grid1, path1, car1, interface, car_one_obj, vert_dir_1, horiz_dir_1):
    length = len(path1)
    instructions = []

    for i in range(0, length):
        # Creates comparison between past and current values for car 1
        if i < len(path1):
            temp_y_1 = car1[0]
            temp_x_1 = car1[1]
            car1[0] = path1[i][0]
            car1[1] = path1[i][1]

        if temp_x_1 > car1[1]:
            horiz_dir_1 = True
        else:
            horiz_dir_1 = False
        # Moves car in GUI and shows motion
        for j in range(4):
            time.sleep(0.05)
            # Moves car 1
            if i < len(path1):
                if temp_y_1 != car1[0] and vert_dir_1:
                    interface.move(car_one_obj, 0, -10)
                    interface.update()
                    if j == 0:
                        instructions.append(2)
                elif temp_y_1 != car1[0] and (not vert_dir_1):
                    interface.move(car_one_obj, 0, 10)
                    interface.update()
                    if j == 0:
                        instructions.append(2)
                elif temp_x_1 != car1[1] and horiz_dir_1:
                    interface.move(car_one_obj, -14.25, 0)
                    interface.update()
                    if j == 0:
                        instructions.append(0)
                else:
                    interface.move(car_one_obj, 14.25, 0)
                    interface.update()
                    if j == 0:
                        instructions.append(1)

        grid1[car1[0]][car1[1]] = 1
        grid1[temp_y_1][temp_x_1] = 4
        print_map(grid1)
        # time.sleep(1)
    return instructions


# Checking for intersection
def check_for_intersection(path_1, obstacle):
    test_intersection_check = False
    # Detects which path is shorter and grabs the length of the shortest path
    scan_length = len(path_1)

    # Check if there is an intersection between the first and second car

    for i in range(scan_length):
        if (path_1[i][0] == obstacle[0]) and (path_1[i][1] == obstacle[1]):
            test_intersection_check = True

    return test_intersection_check


# Creates shapes in GUI
def create_ui(interface, x_val_1, x_val2, dynamic_y1, dynamic_y2):
    for i in range(0, 4):
        interface.create_rectangle(x_val_1, dynamic_y1, x_val2, dynamic_y2, outline='black', width=5)
        x_val_1 = x_val_1 + 103
        x_val2 = x_val2 + 103


# Function for drawing route on GUI
def draw_route(path1, car1, interface, car_one_obj, vert_dir_1):
    # extra params , path2, car2, car_two_obj, vert_dir_2, horiz_dir_2
    length = len(path1)
    line_x, line_y = interface.coords(car_one_obj)

    for i in range(0, length):
        # Creates comparison between past and current values for car 1
        if i < len(path1):
            temp_y_1 = car1[0]
            temp_x_1 = car1[1]
            car1[0] = path1[i][0]
            car1[1] = path1[i][1]

        if temp_x_1 > car1[1]:
            horiz_dir_1 = True
        else:
            horiz_dir_1 = False
        # Moves car in GUI and shows motion
        # Default window color in hex #f0f0f0
        for j in range(4):
            time.sleep(0.05)
            # Moves car 1
            if i < len(path1):
                if temp_y_1 != car1[0] and vert_dir_1:
                    # interface.move(car_one_obj, 0, -10)
                    interface.create_line(line_x, line_y, line_x, line_y - 12, width=5)
                    line_y = line_y - 10
                    interface.update()
                elif temp_y_1 != car1[0] and (not vert_dir_1):
                    # interface.move(car_one_obj, 0, 10)
                    interface.create_line(line_x, line_y, line_x, line_y + 13, width=5)
                    line_y = line_y + 10
                    interface.update()
                elif temp_x_1 != car1[1] and horiz_dir_1:
                    # interface.move(car_one_obj, -14.25, 0)
                    interface.create_line(line_x, line_y, line_x - 16.25, line_y, width=5)
                    line_x = line_x - 14.25
                    interface.update()
                else:
                    # interface.move(car_one_obj, 14.25, 0)
                    interface.create_line(line_x, line_y, line_x + 17.25, line_y, width=5)
                    line_x = line_x + 14.25
                    interface.update()
        # interface.delete(55,20)


def delete_route(path1, car1, interface, car_one_obj, vert_dir_1):
    # extra params , path2, car2, car_two_obj, vert_dir_2, horiz_dir_2
    length = len(path1)
    line_x, line_y = interface.coords(car_one_obj)

    for i in range(0, length):
        # Creates comparison between past and current values for car 1
        if i < len(path1):
            temp_y_1 = car1[0]
            temp_x_1 = car1[1]
            car1[0] = path1[i][0]
            car1[1] = path1[i][1]

        if temp_x_1 > car1[1]:
            horiz_dir_1 = True
        else:
            horiz_dir_1 = False
        # Moves car in GUI and shows motion
        # Default window color in hex #f0f0f0
        for j in range(4):
            time.sleep(0.05)
            # Moves car 1
            if i < len(path1):
                if temp_y_1 != car1[0] and vert_dir_1:
                    # interface.move(car_one_obj, 0, -10)
                    interface.create_line(line_x, line_y, line_x, line_y - 12, width=5, fill='#f0f0f0')
                    line_y = line_y - 10
                    interface.update()
                elif temp_y_1 != car1[0] and (not vert_dir_1):
                    # interface.move(car_one_obj, 0, 10)
                    interface.create_line(line_x, line_y, line_x, line_y + 13, width=5, fill='#f0f0f0')
                    line_y = line_y + 10
                    interface.update()
                elif temp_x_1 != car1[1] and horiz_dir_1:
                    # interface.move(car_one_obj, -14.25, 0)
                    interface.create_line(line_x, line_y, line_x - 16.25, line_y, width=5, fill='#f0f0f0')
                    line_x = line_x - 14.25
                    interface.update()
                else:
                    # interface.move(car_one_obj, 14.25, 0)
                    interface.create_line(line_x, line_y, line_x + 17.25, line_y, width=5, fill='#f0f0f0')
                    line_x = line_x + 14.25
                    interface.update()


def draw_initial_car(interface, row, column, image):
    if row == 0:
        return interface.create_image(55 * column, 20, image=image) #52
    elif row == 6:
        return interface.create_image(55 * column, 265, image=image) #275
    elif row == 1 and column == 0:
        return interface.create_image(20, 63, image=image)
    elif row == 5 and column == 0:
        return interface.create_image(20, 220, image=image)
    elif row == 1 and column == 6:
        return interface.create_image(330, 70, image=image)
    elif row == 5 and column == 6:
        return interface.create_image(330, 220, image=image)


def draw_obstacle(obstacle_image, obstacle_y, obstacle_x):
    if obstacle_y == 1:
        canvas.create_image(55 * obstacle_x, 66, image=obstacle_image)
    else:
        canvas.create_image(55 * obstacle_x, 45 * obstacle_y, image=obstacle_image)


grid = []
intersection_check = False
create_map(grid)
print_map(grid)  # Look into displaying this grid visually through python libraries

# Window for visual interface

window = tk.Tk()
canvas = tk.Canvas(window, width=323, height=286) # 343
canvas.pack()

x_coord = -3
y_coord = 20
create_ui(canvas, x_coord, y_coord, -5, 40)   # Creates first row
create_ui(canvas, x_coord, y_coord, 90, 200)  # 200Creates second row
create_ui(canvas, x_coord, y_coord, 240, 290)  #290 Creates second row
filename1 = tk.PhotoImage(file="car1.png")
filename1 = filename1.subsample(5, 5)
# car_img = canvas.create_image(20, 70 * 4, image=filename)
canvas.update()

# Update map for car's position, look into how to make user inputs
car_1 = [int(input("Car's Starting Y Position: ")), int(input("Car's Starting X Position: "))]
carY = car_1[0]  # Rows correspond with the first coordinate
carX = car_1[1]  # Columns correspond with the second coordinate
car_img = draw_initial_car(canvas, carY, carX, filename1)
canvas.update()

# Choose destination
# destination = [2, 7]  # Test :(2, 7)(0,5)
# Possible destinations: (0,1),(0,2)(0,5),(0,6)(1,1)(1,6)(2,1)(2,6)
destination = [int(input("Destination's Y Position: ")), int(input("Destination's Starting X Position: "))]
destinationY = destination[0]
destinationX = destination[1]

# Creating obstacle
obstacle = [int(input("Obstacle's Y Position: ")), int(input("Obstacle's Starting X Position: "))]
obstacleY = obstacle[0]
obstacleX = obstacle[1]
obstacle_img = tk.PhotoImage(file="cone.png")
obstacle_img = obstacle_img.subsample(8, 8)
draw_obstacle(obstacle_img, obstacleY, obstacleX)


grid[carY][carX] = 1  # Mark car's starting point on the map
# print_map(grid)

grid[destinationY][destinationX] = 2  # Mark car's destination on the map
# print_map(grid)

grid[obstacleY][obstacleX] = 7  # Mark obstacle on the map
print_map(grid)

# Calculate total vertical distance that needs to be traversed
distanceY = destinationY - carY
if distanceY < 0:
    vertDirection1 = True  # Car needs to drive north
    distanceY = abs(distanceY)  # Creates positive value
else:
    vertDirection1 = False  # Car needs to drive south

# print(distanceY)
# print(vertDirection)

# Calculate total horizontal distance that needs to be traversed
distanceX = destinationX - carX
if distanceX < 0:
    horizDirection1 = True  # Car needs to drive left
    distanceX = abs(distanceX)  # Creates positive value
else:
    horizDirection1 = False  # Car needs to drive right

# print(distanceX)
# print(horizDirection)

# Initializes path routing
path_1 = car_path(carX, carY, grid, distanceY, distanceX, intersection_check, vertDirection1, horizDirection1, obstacle)
draw_route(path_1, car_1, canvas, car_img, vertDirection1)

intersection_check = check_for_intersection(path_1, obstacle)
print(path_1)
if intersection_check:
    delete_route(path_1, car_1, canvas, car_img, vertDirection1)
    draw_obstacle(obstacle_img, obstacleY, obstacleX)
    path_1 = car_path(carX, carY, grid, distanceY, distanceX, intersection_check, vertDirection1, horizDirection1, obstacle)
    draw_route(path_1, car_1, canvas, car_img, vertDirection1)
print(path_1)
# Store coordinates of path in 2D array - Done above
# Read off path and mark it down in the grid
update_map(path_1)
print_map(grid)
# draw_route(path_1, car_1, canvas, car_img, vertDirection1)
# Need to move car through grid
instruction = []
instruction = move_car(grid, path_1, car_1, canvas, car_img, vertDirection1, horizDirection1)
print(instruction)
rc_car = RCControl("COM5")
start_time = time.time()
end_time = time.time()

for i in range(len(instruction)):
    start_time = time.time()
    while end_time - start_time < 2:
        rc_car.steer(instruction[i])
        end_time = time.time()
rc_car.stop()
input("Press Enter to Quit")

'''
Developer Notes: 
- This code can be optimized to be more dynamic instead of a static two car system. At the time,
I wasn't thinking straight and should've used an array of objects to initialize and create
as many cars as needed. This  should be done if ever worked on in the future
-Look into creating a single function to generalize booleans for directions, so we can just call the function
maybe? Also need to look at making these functions to generalize the process for a second car when added into the
code
-screen.update() is needed throughout code for tkinter to be used without main loop

'''

"""
Notes on how tuples work in python 2D arrays
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
       print(c,end = " ")
   print()
"""

