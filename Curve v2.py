import pygame
import math




class Bezie():
    def __init__(self,dots):
        self.dots = dots
    def update(self,time):
        coord = []
        for i in range(len(self.dots)-1):
            coord.append(self.find(time,self.dots[i],self.dots[i+1]))
        for i in range(len(self.dots)-1):
                pygame.draw.aalines(screen, WHITE, True, [self.dots[i],self.dots[i+1]], 2)
        b = len(coord)
        while b!=1:
            b = len(coord)
            new_cords = []
            for i in range(len(coord)-1):
                pygame.draw.aalines(screen, WHITE, True, [coord[i],coord[i+1]], 2)
            for i in range(len(coord)):
                pygame.draw.circle(screen, (255,0,255), [int(coord[i][0]),int(coord[i][1])], 2, 1)
            for i in range(b-1):
                new_cords.append(self.find(time,coord[i],coord[i+1]))
            coord = new_cords.copy()
            b = len(coord)
        pygame.draw.circle(screen, (255,0,255), [int(coord[0][0]),int(coord[0][1])], 2, 1)
        return [int(coord[0][0]),int(coord[0][1])]
    def find(self,time,dotA,dotB):
        a = dotB[0] - dotA[0]
        b = dotB[1] - dotA[1]
        length = math.sqrt(a**2+b**2)
        print(a,b,length)
        try:
            cos = float(a) / length
        except:
            cos = 0.01
        try:
            sin = float(b) / length
        except:
            sin = 0.01
        #print(sin)
        new_lenght = length * time/100.0
        #print(new_lenght)
        coords = [new_lenght*cos+dotA[0],new_lenght*sin+dotA[1]]
        return coords       

WIDTH = 2500
HEIGHT = 2500
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
running = True
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
X = 2
array = [
[500*X,50*X],
[10*X,100*X],
[800*X,900*X],
[500*X,70*X],
[600*X,900*X],
[100*X,900*X]
]

bez = Bezie(array)
time = 1
cords = []
while running:
    screen.fill(BLACK)
    clock.tick(FPS)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    cords.append(bez.update(time))
    if len(cords) > 2: 
        pygame.draw.aalines(screen, (255,0,255), False, cords, 4)
    time +=0.1
    if time == 100: 
        time = 1
        cords = []
    pygame.display.update()
