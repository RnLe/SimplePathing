import matplotlib.pyplot as plt
from matplotlib import animation
import random as rand

GridWidth, GridHeight = 8, 8
GridScale = 1
GridOffset = -0.5

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes()

rectangle = []
for x in range(GridWidth):
    for y in range(GridHeight):
        tempRec = plt.Rectangle((x*GridScale-GridOffset, y*GridScale-GridOffset), GridScale, GridScale, fc='w', ec='k')
        rectangle.append(tempRec)
        plt.gca().add_patch(tempRec)


speed = 20
interval = 20
# starts randomly
start = (rand.randint(1, 8), rand.randint(1, 8))
target = start

class path:
    # count of global paths (!= length)
    pathCount = 0

    def __init__(self):
        pathCount += 1
        pathLength = 0
        # array of coordinates
        path = []
        

    def __del__(self):
        pathCount -= 1


def pathing(startPoint, steps):
    points = []
    points.append(startPoint)
    i = 0
    attemps = 0

    while (i < steps):
        newX = points[i][0] + rand.randint(-1, 1)
        # branchless conditions
        newX += (newX < 1)
        newX -= (newX > GridWidth)

        newY = points[i][1] + rand.randint(-1, 1)
        # branchless conditions
        newY += (newY < 1)
        newY -= (newY > GridHeight)

        # if new coordinate is already in points, don't iterate and redo pathing step
        # else save new points and carry on
        if (newX, newY) not in points:
            i += 1
            points.append((newX, newY))
        elif attemps > 10: break
        else: attemps += 1

    return points

line, = ax.plot([], [], 'b-', lw=2)
points = pathing(start, 5)

circle = plt.Circle(start, radius=0.3, fc='k')
text_target = ax.text(0.02, 0.97, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    circle.center = target
    ax.add_patch(circle)
    return circle, line

def animate(i):
    global target, start, points, interval
    steps = len(points)-1
    # gets step count
    if (i % (steps*interval) == 0): points = pathing(points[-1], 5)
    step = int((i % (steps*interval)) / interval)
    # draw path
    line.set_data(list(zip(*points)))
    # calculate relative steps
    stepping = (points[step+1][0] - points[step][0], points[step+1][1] - points[step][1])
    # move circle
    x, y = circle.center
    x = points[step][0] + stepping[0] * ((i%20)/speed)
    y = points[step][1] + stepping[1] * ((i%20)/speed)
    circle.center = (x, y)
    # update text
    text_target.set_text(f'target = {(points[step+1][0], points[step+1][1])}')
    return circle, text_target, line

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=1000, 
                               interval=interval,
                               blit=True)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Rene'), bitrate=1800)

anim.save('pathing_v1.mp4', writer=writer)

plt.axis('scaled')
# plt.axis('off')
plt.show()