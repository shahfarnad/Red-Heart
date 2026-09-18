import turtle as t,math as m

def heart(z):
  x=16*m.sin(z)**3
  y=13*m.cos(z)-5* m.cos(2*z)-2*m.cos(3*z)
  -m.cos(4*z)
  return x,y

screen=t.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.colormode(1.0)

z=t.Turtle()
t.speed(0)
t.hideturtle()
t.width(1)

n,k=140,2.1
scale=10
bright,dark=(0.95,0.15,0.1),(0.03,0.0,0.0)

for i in range(n):
  ang=2*m.pi*i/n
  hx,hy=heart(ang)
  hx,hy=hx*scale,hy*scale
  ex,ey=hx*k,hy*k
  steps=14
  
  z.penup()
  z.goto(hx,hy)
  z.pendown()
  
  for j in range(steps) :
    f=(j+1)/steps
    col=tuple(bright[c]+dark[c]-bright[c] * f for c in range(3))
    z.pencolor(col)
    z.goto(hx+(ex-hx)* f,hy+(ey-hy)*f)
    
t.done()