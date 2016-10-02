from pygene3.gene import *
from pygene3.population import *
from pygene3.organism import *
import pygame
from time import time
from pygame.locals import *
import random
import sys
import math

#프리셋
TARGET_FPS = 24
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LEFT = 1
RIGHT = 3
pygame.init()
screen = pygame.display.set_mode((800, 450), DOUBLEBUF)

#표본이 되는 그래프
defgs = {}
for i in range (0,400) :
    defgs[i] = int((((i-200)**2)+48000)/400)
defg = defgs

print("default graph initiated")

#그래프를 그리는 함수
def drawgraph(graph,case):
    if case == 0:
        for i in range (0,400):
            pygame.draw.circle(screen, WHITE,(i,graph[i]), 1)
    else:
        for i in range (0,400):
            pygame.draw.circle(screen, RED, (i+400,int(graph[i])), 1)

#그래프 해커 '유전자'
class GraphHacker(IntGene) :
    mutProb = 0.2
    mutAmt = 8
    randMax = 400
    randMin = 0
    def __repr__(self):
        return self.value

genome  = {}
for i in range(0,400):
    genome[str(i)] = GraphHacker #Input Random Genes

class GHOrg(Organism):
    genome = genome

    def repr(self): #유전자의 Phenotype 지정
        chars = [self[str(i)] for i in range(self.numgenes)]
        return chars
    def fitness(self): #유전자의 Fitness 결정
        guess = [self[str(i)] for i in range(self.numgenes)]
        diffs = 0
        for i in range(0,400):
            diffs += (defgs[i]-guess[i])**2 #차이가 난 만큼의 제곱을 곱함, 즉 차이가 적을수록 더 적합함
        return diffs

class GHPop (Population) :
    species = GHOrg
    initPopulation = 32
    childCull = 8
    childCount = 8

    mutants = 8

print("genome initiated") #유전자가 확실히 지정되었는지 확인

def main():
    world=GHPop()
    fontobj = pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 16)
    tt=0
    while True:
        for event in pygame.event.get():
             if event.type == QUIT:
                    pygame.QUIT
                    sys.exit()
        tt+=1
        textSurfaceObj = fontobj.render('Current Generation : %d, Current Fitness : %f'%(tt,world.fitness()), True, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (400, 25)
        screen.fill(BLACK)
        screen.blit(textSurfaceObj, textRectObj)
        drawgraph(defgs,0)
        b=world.best().repr()
        drawgraph(b,1)
        print(world.fitness(),b)
        pygame.display.flip()
        clock.tick(TARGET_FPS)
        world.gen()


if __name__ == '__main__':
    main()