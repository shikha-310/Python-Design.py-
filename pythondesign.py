import turtle as t
import colorsys 
t.bgcolor('black')
t.tracer(100)
t.pensize(4)
h=0.3
def draw(anglr, n):
    t.circle(30+n, 90)
    t.left(angle=70)
    t.circle(30+n,60)
t.goto(-50,0)
for i in range(150):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.008
    t.color(c)
    draw(60,i)
    draw(90,i)
    draw(120,i*2)
    draw(180,i)
    draw(360,i)
t.done()