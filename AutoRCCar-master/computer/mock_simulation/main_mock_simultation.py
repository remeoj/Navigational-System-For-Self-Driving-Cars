"""
Notes on how tuples work in python 2D arrays
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
       print(c,end = " ")
   print()
"""


def create_map(grid1):
    for i in range(0, 8):
        inner_map = []
        # map.append(i)
        for j in range(0, 8):
            if (i == 0 or i == 3 or i == 4 or i == 7) and (j == 0 or j == 3 or j == 4 or j == 7) :
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
def vert_direction(path1, vertical_pos, horizontal_pos):
    # Moves car to proper Y direction
    # distanceY = distanceY - 1
    if vertDirection:
        vertical_pos = vertical_pos - 1  # Moves car up grid
        path1.append([vertical_pos, horizontal_pos])
    else:
        vertical_pos = vertical_pos + 1  # Moves car down grid
        path1.append([vertical_pos, vertical_pos])
    return vertical_pos


# Function to move a car on the grid horizontally
def horiz_direction(path1, vertical_pos, horizontal_pos):
    # Moves car to proper Y direction
    # distanceY = distanceY - 1
    if horizDirection:
        horizontal_pos = horizontal_pos - 1  # Moves car up grid
        path1.append([vertical_pos, horizontal_pos])
    else:
        horizontal_pos = horizontal_pos + 1  # Moves car down grid
        path1.append([vertical_pos, horizontal_pos])
    return horizontal_pos


# Function to show path on the grid
def update_map(path1):
    for i in range(0, len(path1)):
        temp_row = path1[i][0]
        temp_col = path1[i][1]
        grid[temp_row][temp_col] = 4


grid = []

create_map(grid)
print_map(grid)  # Look into displaying this grid visually through python libraries

# Update map for car's position
car = [7, 1]   # Will eventually be carX and carY variables
carY = car[0]  # Rows correspond with the first coordinate
carX = car[1]  # Columns correspond with the second coordinate
grid[carY][carX] = 1
print_map(grid)

# Choose destination
destination = [0, 5]
grid[destination[0]][destination[1]] = 2
print_map(grid)

# Calculate total vertical distance that needs to be traversed
distanceY = destination[0] - car[0]
if distanceY < 0:
    vertDirection = True  # Car needs to drive north
    distanceY = abs(distanceY)  # Creates positive value
else:
    vertDirection = False  # Car needs to drive south

# print(distanceY)
# print(vertDirection)

# Calculate total horizontal distance that needs to be traversed
distanceX = destination[1] - car[1]
if distanceX < 0:
    horizDirection = True  # Car needs to drive left
    distanceX = abs(distanceX)  # Creates positive value
else:
    horizDirection = False  # Car needs to drive right

# print(distanceX)
# print(horizDirection)

# Initializes path routing
path = []
route_pos_x = carX
route_pos_y = carY

# The following lines create the path that the car is going to traverse
# Initial movement from starting place
if carY == 0 or carY == 7:
    route_pos_y = vert_direction(path, route_pos_y, route_pos_x)
else:
    route_pos_x = horiz_direction(path, route_pos_y, route_pos_x)

# Following movements of the car after starting place
if carY == 0 or carY == 7:  # In this case, the destination is either at the top or bottom of the grid
    # Logic to stop this movement when it's one coordinate (X,Y) -> (0,1 or 1,0) away, stops car on the inner 6x6  grid
    while distanceX > 0 or distanceY > 2:
        # Moves car to proper Y direction
        if distanceY > 2:
            distanceY = distanceY - 1
            route_pos_y = vert_direction(path, route_pos_y, route_pos_x)
            continue
        # Moves car to proper X direction
        if distanceX > 0:
            distanceX = distanceX - 1
            route_pos_x = horiz_direction(path, route_pos_y, route_pos_x)
            continue
    vert_direction(path, route_pos_y, route_pos_x)  # Moves car up or down to the destination

else:  # In this case, the destination is either at the left or right of the grid
    while distanceX > 2 or distanceY > 0:
        # Moves car to proper Y direction
        if distanceY > 0:  # Stops car on the inner 6x6  grid
            distanceY = distanceY - 1  # Decrements total vertical distance that needs to be traversed
            route_pos_y = vert_direction(path, route_pos_y, route_pos_x)
            continue
        # Moves car to proper X direction
        if distanceX > 2:
            distanceX = distanceX - 1  # Decrements total horizontal distance that needs to be traversed
            route_pos_x = horiz_direction(path, route_pos_y, route_pos_x)
            continue
    horiz_direction(path, route_pos_y, route_pos_x)  # Moves car left or right to the destination

update_map(path)
print_map(grid)
# Store coordinates of path in 2D array - Done above
# Read off path and mark it down in the grid


# ***Look into creating a single function to generalize booleans for directions, so we can just call the function
# maybe? Also need to look at making these functions to generalize the process for a second car when added into the
# code** screen.update() is needed throughout code for tkinter to be used without main loop
