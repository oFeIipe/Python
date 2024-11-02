from turtle import Turtle, Screen

cleitin = Turtle()
robertim = Turtle()
tela = Screen()

cleitin.shape("turtle")
cleitin.color("MediumSlateBlue")
robertim.shape("turtle")
robertim.color("red")




for i in range(4):
    cleitin.forward(100)
    robertim.left(90)
    cleitin.left(90)
    robertim.forward(100)

import heroes

for a in range(10):
    print(heroes.gen())

'''cleitin.left(45)
cleitin.forward(100)
cleitin.right(90)
cleitin.forward(100)
cleitin.right(135)
cleitin.forward(150)'''

tela.exitonclick()


'''
colors = [
    "black", "gray", "grey", "red", "green", "blue", "yellow", "cyan", "magenta", "orange", "purple",
    "brown", "pink", "violet", "turquoise", "gold", "silver", "maroon", "navy", "lime", "aqua", "teal",
    "olive", "salmon", "coral", "khaki", "indigo", "orchid", "plum", "chocolate", "tomato", "lavender",
    "hotpink", "deeppink", "crimson", "firebrick", "sienna", "tan", "beige", "indianred", "darkred",
    "rosybrown", "palevioletred", "mediumvioletred", "darkviolet", "blueviolet", "mediumpurple",
    "slateblue", "darkslateblue", "mediumslateblue", "darkorange", "orangered", "darkgreen", "forestgreen",
    "seagreen", "mediumseagreen", "darkkhaki", "darkgoldenrod", "goldenrod", "yellowgreen", "chartreuse",
    "lawngreen", "greenyellow", "olivedrab", "mediumspringgreen", "springgreen", "mediumturquoise",
    "aquamarine", "mediumaquamarine", "mediumblue", "steelblue", "royalblue", "dodgerblue", "cornflowerblue",
    "midnightblue", "darkslategray", "slategray", "dimgrey", "darkgray", "slategrey"
]


for i in range(20):
    ronaldin.penup()
    ronaldin.forward(10)
    ronaldin.pendown()
    ronaldin.forward(10)

ronaldin.penup()
ronaldin.goto(-50, 400)
ronaldin.pendown()

def desenhar(numero_lados):
    angulo = 360 / numero_lados
    for j in range(numero_lados):
        ronaldin.pencolor(random.choice(colors))
        ronaldin.forward(100)
        ronaldin.right(angulo)

for i in range(3, 31):
    desenhar(i)

ronaldin = Turtle()

lados = [0, 90, 180, 270]
ronaldin.pensize(10)
ronaldin.speed(0)
for i in range(300):
    ronaldin.forward(30)
    ronaldin.setheading(random.choice(lados))
    ronaldin.pencolor(random.choice(colors))
tela = Screen()
tela.exitonclick()'''