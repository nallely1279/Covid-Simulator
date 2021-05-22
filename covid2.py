# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:29:30 2020

@author: Nallely
"""
import dot
import random
import pygame
pygame.init()
day=0
screen_width=500
screen_height=500
screen=pygame.display.set_mode([screen_width,screen_height])
timer=pygame.time.Clock()

radiusDot=3
radiusSD=radiusDot*3

colors={'blue':(0,0,255),'orange':(255,165,0),'red':(0,128,0),'black':(0,0,0),'green':(0,128,0)}

healthy=pygame.sprite.Group()
infected=pygame.sprite.Group()
sick=pygame.sprite.Group()
immune=pygame.sprite.Group()
dead=pygame.sprite.Group()
allsprites=pygame.sprite.Group()
allspriteslist=[]
def addDotsToGroups():
    
    for i in range(89):
        start=(random.randint(0, screen_width),random.randint(0,screen_height))
        end=(random.randint(0, screen_width),random.randint(0,screen_height))
        newdot=dot.dot(True, radiusDot, radiusSD, i, start, end,(0,0,255))
        allsprites.add(newdot)
        allspriteslist.append(newdot)
        healthy.add(newdot)
    for i in range(10):
        start=(random.randint(0, screen_width),random.randint(0,screen_height))
        end=(random.randint(0, screen_width),random.randint(0,screen_height))
        newdot=dot.dot(False, radiusDot, radiusSD, i, start, end,(0,0,255))
        allsprites.add(newdot)
        allspriteslist.append(newdot)
        healthy.add(newdot)
    immune_count=0
    while immune_count<=5:
        index=random.randint(0,98)
        immune.add(allspriteslist[index])
        healthy.remove(allspriteslist[index])
        immune_count+=1
    start=(random.randint(0, screen_width),random.randint(0,screen_height))
    end=(random.randint(0, screen_width),random.randint(0,screen_height))
    original_infected=dot.dot(False,radiusDot,radiusSD,i,start,end,colors['orange'], 'infected')
    infected.add(original_infected)
    allsprites.add(original_infected)     

'''def collision_avoidance():
    for e in allsprites:
        allcollisions=pygame.sprite.spritecollideany(e, allsprites,pygame.sprite.collide_circle)
        while allcollisions!=0:
            e.collison=True
            e.calculate_tempgoal()
            e.movetemp()'''     
    
        
    
def main():
    global day
    addDotsToGroups()
    day_count=0
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        if day_count==20:
            day_count=0
            day+=1
            
        screen.fill((250,250,250))
        #dot_group.draw(screen)
        #dot_group.update(day)
        
        for e in allsprites:
            e.drawCircle(screen)
            e.move()
        for e in allsprites:
            collisions_Infected = pygame.sprite.spritecollide(e, infected, False, pygame.sprite.collide_circle)
            collisions_Sick = pygame.sprite.spritecollide(e, sick, False, pygame.sprite.collide_circle)
            if len(collisions_Infected) != 0 or len(collisions_Sick) != 0:    # there's at least 1 collision
                if e.state=='healthy':
                    run_infected=e.getInfected(day)
                    run_infected
                    if run_infected==True:
                        infected.add(e)
                        healthy.remove(e)
                elif e.state=='infected':
                    run_checkI=e.checkInfected(day)
                    run_checkI
                    if run_checkI==True:
                        if e.state=='sick':
                            sick.add(e)
                            infected.remove(e)
                elif e.state=='sick':
                    run_checkS=e.checkSick(day)
                    run_checkS
                    if run_checkS==True:
                        if e.state=='immune':
                            immune.add(e)
                            sick.remove(e)
                        if e.state=='dead':
                            dead.add(e)
                            sick.remove(e)
            
            

    # Flip the display
        pygame.display.flip()
        day_count+=1
        timer.tick(100)       # slowed down to 1fps so beep is not too annoying

# Done! Time to quit.
    pygame.quit()


if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
