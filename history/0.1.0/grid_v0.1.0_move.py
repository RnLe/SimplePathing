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
# starts randomly
start = (rand.randint(1, 8), rand.randint(1, 8))
target = start

line, = ax.plot([], [], 'b-', lw=2)

circle = plt.Circle(start, radius=0.3, fc='k')
text_target = ax.text(0.02, 0.97, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    circle.center = target
    ax.add_patch(circle)
    return circle, line

def animate(i):
    global target, start
    if (i > 0 and i % 20 == 0): 
        start = target

        newX = start[0] + rand.randint(-1, 1)
        # branchless conditions
        newX += (newX < 1)
        newX -= (newX > GridWidth)

        newY = start[1] + rand.randint(-1, 1)
        # branchless conditions
        newY += (newY < 1)
        newY -= (newY > GridHeight)

        target = (newX, newY)
    line.set_data(*zip(start, target))
    steps = (target[0] - start[0], target[1] - start[1])
    x, y = circle.center
    x = start[0] + steps[0] * ((i%20)/speed)
    y = start[1] + steps[1] * ((i%20)/speed)
    circle.center = (x, y)
    text_target.set_text(f'target = {target}')
    return circle, text_target, line

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=1000, 
                               interval=20,
                               blit=True)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Rene'), bitrate=1800)

anim.save('pathing_v1_move.mp4', writer=writer)


plt.axis('scaled')
# plt.axis('off')
plt.show()