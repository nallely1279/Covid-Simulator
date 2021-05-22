# -*- coding: utf-8 -*-

import numpy
import pygame
import random
colors={'blue':(0,0,255),'orange':(255,165,0),'red':(255,0,0),'black':(0,0,0),'immune':(0,128,0)}
pygame.init()
class dot(pygame.sprite.Sprite):
    count=0
    
    def __init__(self, social_distancing, radiusDot, radiusSD, id, start=(0,0), end=(0,0),color=(0,0,255), state='healthy'):
        super().__init__()
        self.id= id
        self.day=0
        self.state=state
        self.incubator=False
        self.incubator_date=0
        self.infected_date=0
        self.social_distancing=social_distancing
        #Drawing Cicles
        self.image=pygame.Surface([2*radiusSD,2*radiusSD])
        self.image.fill((0,0,0,0))
        self.color=color
        
        self.rect=self.image.get_rect()
        self.rect.x=start[0]
        self.rect.y=start[1]
        self.radius=radiusDot
        self.radiusSD=radiusSD
        
        self.start=start
        self.end=end
        self.gps=start
        self.goal=end
        #collison avoidance
        self.collision=False
        self.tempgoal=(0,0)
        
        
        self.size=5
    def drawCircle(self,screen):
        if self.social_distancing==False:
            pygame.draw.circle((screen),self.color,self.gps,self.radius)
            #pygame.draw.circle((screen),(0,0,0,0),self.gps,self.radiusSD,1)
        if self.social_distancing==True:
            pygame.draw.circle((screen),self.color,self.gps,self.radius)
            pygame.draw.circle((screen),(0,0,0),self.gps,self.radiusSD,1)

        
    def getInfected(self, day):
        randomprob=random.randint(1,100)
        if randomprob in range(1,80):
            self.infected_date=day
            self.state='infected'
            self.color=(255,165,0)
            return True
        else:
            return False
        
    def checkInfected(self,day):
        if (day-self.infected_date)==5:
            randomprob=random.randint(1,100)
            if randomprob in range(1,50):
                self.state='infected'
                self.infected_date=day
                return True
            else:
                self.state='sick'
                self.color=colors['red']
                self.infected_date=day
                return True
        else:
            return False
        
    def checkSick(self,day):
        if (day-self.infected_date)==15:
            randomprob=random.randint(1,100)
            if randomprob in range(1,98):
                self.state='immune'
                self.color=(0,128,0)
                return True
            else:
                self.state='dead'
                self.color=(0,0,0)
                return True
        else:
            return False
        
    '''def calculate_tempgoal(self):
        tempX=random.randint(-15,15)+self.gps[0]
        tempY=random.randint(-15,15)+self.gps[1]
        self.tempgoal=(tempX,tempY)'''
        
    def move(self):
        if self.gps==self.end:
            self.goal=self.start
        elif self.gps==self.start:
            self.goal=self.end
            
        if self.state!='sick' and self.state!='dead' and self.collision==False:     
            sx = numpy.sign(self.goal[0]-self.gps[0])  # returns -1,0,1
            nx = self.gps[0] + sx
            sy = numpy.sign(self.goal[1]-self.gps[1])
            ny = self.gps[1] + sy
            self.gps = (nx,ny)
            self.rect.x=self.gps[0]
            self.rect.y=self.gps[1]
    '''def movetemp(self):
        if self.state!='sick' and self.state!='dead' and self.collision==True:
            sx = numpy.sign(self.tempgoal[0]-self.gps[0])  # returns -1,0,1
            nx = self.gps[0] + sx
            sy = numpy.sign(self.tempgoal[1]-self.gps[1])
            ny = self.gps[1] + sy
            self.gps = (nx,ny)
            self.rect.x=self.gps[0]
            self.rect.y=self.gps[1]'''
            
            
        