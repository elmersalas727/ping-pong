#juego de serpiente/ping pong
import turtle



wn = turtle.Screen()
wn.title("Pong by Cesar")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

#jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

#pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.50
pelota.dy = 0.50

#linea
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#marcadores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("JugadorA: 0      JugadorB: 0", align = "center", font=("courier", 24 , "normal"))

# marcador
marcadorA=0
marcadorB=0


#def
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)


#teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")

while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #límites
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    #límites/ costados
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("JugadorA: {}      JugadorB: {} ".format(marcadorA,marcadorB), align= "center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("JugadorA: {}      JugadorB: {} ".format(marcadorA,marcadorB), align="center", font=("Courier", 24, "normal"))

 
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and(pelota.ycor() < jugadorB.ycor() + 50
            and pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and(pelota.ycor() < jugadorA.ycor() + 50
            and pelota.ycor() > jugadorA.ycor() -50 )):
        pelota.dx *= -1






