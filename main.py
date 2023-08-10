import customtkinter as ctk
import a_star
import predefined_setups
from predefined_setups import course1

root = ctk.CTk()
root._set_appearance_mode("Dark")
root.title("Pathfinder")

box_size = 80
canvas = ctk.CTkCanvas(root, width = 2000, height=1200)
canvas.pack()

#Initial Grid setup
grid = [[canvas.create_rectangle(x * box_size, y*box_size, (x+1)*box_size, (y+1)*box_size, fill="white")
         for x in range(25)]
         for y in range(15)]
#Define start and end nodes
canvas.itemconfig(grid[7][0], fill = "green")
canvas.itemconfig(grid[7][24], fill = "red")



def findColor(event):
    global color
    canvas = event.widget
    xLocation = event.x // box_size
    yLocation = event.y // box_size
    if canvas.itemcget(grid[yLocation][xLocation], "fill") == "white":
        color = "black" 
    else:
        color = "white"

def click(event):
    canvas = event.widget
    xLocation = event.x // box_size
    yLocation = event.y // box_size
    findColor(event)
    if canvas.itemcget(grid[yLocation][xLocation], "fill") != "red" and canvas.itemcget(grid[yLocation][xLocation], "fill") != "green":
        canvas.itemconfig(grid[yLocation][xLocation], fill = color)
def drag(event):
    canvas = event.widget
    xLocation = event.x // box_size
    yLocation = event.y // box_size
    if canvas.itemcget(grid[yLocation][xLocation], "fill") != "red" and canvas.itemcget(grid[yLocation][xLocation], "fill") != "green":
        canvas.itemconfig(grid[yLocation][xLocation], fill = color)

canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", drag)


def createMaze():
    maze = []
    for y in range(15):
        row = []
        for x in range(25):
            if canvas.itemcget(grid[y][x], "fill") == "black":
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    return maze

def startPathfinding():
    start = (7, 0)
    end = (7, 24)
    maze = createMaze()
    # print(maze)
    path = a_star.astar(maze, start, end)
    for node in path:
        x = node[1]
        y = node[0]
        if canvas.itemcget(grid[y][x], "fill") != "red" and canvas.itemcget(grid[y][x], "fill") != "green":
            canvas.itemconfig(grid[y][x], fill = "light blue")

startButton = ctk.CTkButton(root, text="Find Path", command=startPathfinding)
startButton.pack()

root.mainloop()
