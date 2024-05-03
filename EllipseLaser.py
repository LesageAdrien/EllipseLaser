import pygame as pg
import numpy as np
SCREEN_SIZE = (1000,800)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)


pg.init()

a = 450
b = 300

c = np.array((500,400))

t = np.linspace(0,2*np.pi,150)
ellipse = np.vstack((a*np.cos(t) +c[0],b*np.sin(t)+c[1]))

p = np.array((100,100))

d = np.random.random(2)-0.5
d *= 1/np.linalg.norm(d)
print(d)


def pondcross(u, v, a, b):
    return u[0]*v[0]/a**2 + u[1]*v[1]/b**2
def howfarfromborder(p, d, a, b):
    return (-pondcross(p, d, a, b) + np.sqrt(pondcross(p, d, a, b)**2 - pondcross(d, d, a, b)*(pondcross(p, p, a, b)-1)))/pondcross(d, d, a, b)
def normaltoellipse(p,a,b):
    d = np.array((p[0]*b**2, p[1]*a**2))
    return d/np.linalg.norm(d)
def symetrie(p, n):
    return 2* (p[0]*n[0] + p[1]*n[1]) * n - p
def next(p,d,a,b):
    newp = p + howfarfromborder(p,d,a,b) * d
    return newp , symetrie(-d, normaltoellipse(newp, a, b))

ti = howfarfromborder(p,d,a,b)
n = normaltoellipse(p+ti*d, a, b)

loopperrate = 10000

i = 0
scr = pg.display.set_mode(SCREEN_SIZE)
running = True
while running:
    scr.fill(BLACK)
    pg.draw.polygon(scr, WHITE, ellipse.T, 3)
    i = (i+1)%loopperrate
    d = np.array((np.cos(i * np.pi * 2 / loopperrate),np.sin(i * np.pi * 2 / loopperrate)))

    p1 = p
    d1 = d
    for k in range(60):
        p2, d2 = next(p1, d1, a, b)
        if k == 0 :
            pg.draw.line(scr, (170,50,50), p1+c, p2+c, 4)
        else :
            pg.draw.line(scr, RED, p1+c, p2+c, 1)
        p1 , d1 = p2, d2
    pg.draw.circle(scr, BLUE, p+c, 10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False ; print("STOP")

    if pg.mouse.get_pressed()[0]:
        print("mouse clicked")

    pg.display.flip()

pg.quit()
