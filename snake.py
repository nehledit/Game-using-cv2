import random as r
import cv2
import numpy as np
import pandas as pd
import time
blaac=cv2.imread(r'C:\Users\hp\Desktop\black.png')
startg=cv2.imread(r'C:\Users\hp\Desktop\open.png')
over=cv2.imread(r'C:\Users\hp\Desktop\game.jpg')

X=10
Y=10
newx=r.randrange(50,500,10)
newy=r.randrange(50,500,10)
score=0

cv2.imshow('Begin Game',startg)
k=cv2.waitKey(0)
if (k==ord('p')):
    cv2.destroyAllWindows()
    
    while True:
        ##snake position
        blaac[X:X+10,Y:Y+10,0]=0
        blaac[X:X+10,Y:Y+10,1]=255
        blaac[X:X+10,Y:Y+10,2]=0

        ##item position
        blaac[newx:newx+10,newy:newy+10,0]=255
        blaac[newx:newx+10,newy:newy+10,1]=0
        blaac[newx:newx+10,newy:newy+10,2]=0

        
        
        cv2.imshow('Game main window',blaac)

        if(newx==X and newy==Y):
            
            newx=r.randrange(50,200,10)
            newy=r.randrange(50,200,10)
            score=score+1
            
        l=cv2.waitKey(0)
        
        if (l==ord('q')):
            
            
            cv2.destroyAllWindows()
            cv2.imshow('game over',over)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print('Your score is ' + str(score))
            break
        
        elif (l==ord('w')):
            blaac[X:X+10,Y:Y+10,0]=0
            blaac[X:X+10,Y:Y+10,1]=0
            blaac[X:X+10,Y:Y+10,2]=0

            blaac[newx:newx+10,newy:newy+10,0]=255
            blaac[newx:newx+10,newy:newy+10,1]=0
            blaac[newx:newx+10,newy:newy+10,2]=0

            
            
            X=X-10
            
            
             
             
        elif (l==ord('a')):
             
            blaac[X:X+10,Y:Y+10,0]=0
            blaac[X:X+10,Y:Y+10,1]=0
            blaac[X:X+10,Y:Y+10,2]=0

            blaac[newx:newx+10,newy:newy+10,0]=255
            blaac[newx:newx+10,newy:newy+10,1]=0
            blaac[newx:newx+10,newy:newy+10,2]=0
            Y=Y-10
        elif (l==ord('d')):
             
            blaac[X:X+10,Y:Y+10,0]=0
            blaac[X:X+10,Y:Y+10,1]=0
            blaac[X:X+10,Y:Y+10,2]=0

            blaac[newx:newx+10,newy:newy+10,0]=255
            blaac[newx:newx+10,newy:newy+10,1]=0
            blaac[newx:newx+10,newy:newy+10,2]=0
            Y=Y+10
        elif (l==ord('s')):
            
             
            blaac[X:X+10,Y:Y+10,0]=0
            blaac[X:X+10,Y:Y+10,1]=0
            blaac[X:X+10,Y:Y+10,2]=0

            blaac[newx:newx+10,newy:newy+10,0]=255
            blaac[newx:newx+10,newy:newy+10,1]=0
            blaac[newx:newx+10,newy:newy+10,2]=0
        
            X=X+10
        
             
    
    
elif(k==ord('e')):
    cv2.destroyAllWindows()
    
##blaac[X:X+10,Y:Y+10,0]=255
##blaac[X:X+10,Y:Y+10,1]=0
##blaac[X:X+10,Y:Y+10,2]=0
##
##cv2.imshow('game',blaac)
##k=cv2.waitKey(0)
##if (k==ord('q')):
##    blaac[X:X+10,Y:Y+10,0]=0
##    blaac[X:X+10,Y:Y+10,1]=0
##    blaac[X:X+10,Y:Y+10,2]=0
##
##    cv2.imshow('game',blaac)
##    g=cv2.waitKey(0)
##    if (g==ord('l')):
##        blaac[X:X+10,Y:Y+10,0]=0
##        blaac[X:X+10,Y:Y+10,1]=255
##        blaac[X:X+10,Y:Y+10,2]=0
##
##
##        cv2.imshow('game',blaac)
##        cv2.waitKey(0)
##        cv2.destroyAllWindows()
