"""
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
       print(c,end = " ")
   print()
"""


def createmap(grid):
    for i in range(0, 8):
        inner_map = []
        # map.append(i)
        for j in range(0, 8):
            if (i == 0 or i == 3 or i == 4 or i == 7) and (j == 0 or j == 3 or j == 4 or j == 7) :
                inner_map.append(3)
            else:
                inner_map.append(0)
        grid.append(inner_map)


def printmap(grid):
    # Simple print out function for 2D array
    for r in grid:
        for c in r:
            print(c, end=" ")
        print()

def vertdecider(path, routePosX, routePosY):
  if vertDirection:
    routePosY = routePosY - 1 #Moves car up grid
    path.append([routePosX,routePosY])    
  else:
    routePosY = routePosY + 1 #Moves car down grid
    path.append([routePosX,routePosY])

grid = []

createmap(grid)
printmap(grid)  # Look into displaying this grid visually through python libraries

# Update map for car's position
car = [7, 1]  # Will eventually be carX and carY variables
carY = car[0] #Rows correspond with the first coordinate
carX = car[1] #Columns correspond with the second coordinate
grid[carY][carX] = 1
printmap(grid)

# Choose destination
destination = [0, 5]
grid[destination[0]][destination[1]] = 2
printmap(grid)

# Calculate total vertical distance that needs to be traversed
distanceY = destination[0] - car[0]
if distanceY < 0:
    vertDirection = True  # Car needs to drive north
    distanceY = abs(distanceY)  # Creates positive value
else:
    vertDirection = False  # Car needs to drive south

print(distanceY)
print(vertDirection)

# Calculate total horizontal distance that needs to be traversed
distanceX = destination[1] - car[1]
if distanceX < 0:
    horizDirection = True  # Car needs to drive left
    distanceX = abs(distanceX)  # Creates positive value
else:
    horizDirection = False  # Car needs to drive right

print(distanceX)
print(horizDirection)

path = []
routePosX = carX
routePosY = carY
while (distanceX > 0) and (distanceY > 0):
  #Moves car to proper Y direction
  distanceY = distanceY - 1
  vertdecider(path, routePosX, routePosY)

  

#Store coordinates of path in 2D array
#Read off path and mark it down in the grid

# ***Look into creating a single function to generalize booleans for directions, so we can just call the function
# maybe? Also need to look at making these functions to generalize the process for a second car when added into the
# code** screen.update() is needed throughout code for tkinter to be used without main loop
