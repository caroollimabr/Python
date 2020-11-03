import turtlefunctions

#faz tartaruga t desenhar os anéis
def olimpiadas(t):
    t.pensize(3)
    jump(1, 0, 0) #fundo círculo superior no centro
    t.setheading(0)

    t.circle(100) #círculo superior no centro
    turtlefunctions.jump(t, -220, 0)
    t.circle(100) #círculo superior esquerdo
    turtlefunctions.jump(t, 220, 0)
    t.circle(100) #círculo superior direito
    turtlefunctions.jump(t, 110, -100)
    t.circle(100) #círculo inferior direito
    turtlefunctions.jump(t, -110, -100)
    t.circle(100) #círculo inferior esquerdo