import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
# canvas.create_rectangle(x0, y0, x1, y1, option, ... )
# x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
rc1 = canvas.create_rectangle(20, 260, 120, 360, outline='white', fill='blue')
rc2 = canvas.create_rectangle(20, 10, 120, 110, outline='white', fill='red')
for x in range(50):
    y = x = 5
    time.sleep(0.025)
    canvas.move(rc1, x, -y)
    canvas.move(rc2, x, y)
    canvas.update()
while 1:
    canvas.update()
# root.mainloop()

#canvas.create_rectangle(-3, -5, 40, 50, outline='black', width=5)     # Corner 1
#canvas.create_rectangle(100, -5, 143, 50, outline='black', width=5)   # Top street 1
#canvas.create_rectangle(203, -5, 246, 50, outline='black', width=5)   # Top street 2
#canvas.create_rectangle(306, -5, 349, 50, outline='black', width=5)   # Corner 2
'''
for i in range(0, 4):
    canvas.create_rectangle(x_coord, -5, y_coord, 50, outline='black', width=5) 
    x_coord = x_coord + 103
    y_coord = y_coord + 103

canvas.create_rectangle(-3, 90, 40, 200, outline='black', width=5)    # side street 1
canvas.create_rectangle(100, 90, 143, 200, outline='black', width=5)  # mid street 1
canvas.create_rectangle(203, 90, 246, 200, outline='black', width=5)  # mid street 2
canvas.create_rectangle(306, 90, 360, 200, outline='black', width=5)  # side street 2
canvas
canvas.update()
'''
'''
#h_corner1 = canvas.create_line(0, 50, 43, 50, fill='black', width=5)
#v_corner2 = canvas.cre
# canvas.create_rectangle(x0, y0, x1, y1, option, ... )
# x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
rc1 = canvas.create_rectangle(20, 260, 120, 360, outline='white', fill='blue')
rc2 = canvas.create_rectangle(20, 10, 120, 110, outline='white', fill='red')
for x in range(50):
    y = x = 5
    time.sleep(0.025)
    canvas.move(rc1, x, -y)
    canvas.move(rc2, x, y)
    canvas.update()
#while 1:
   # canvas.update()
'''