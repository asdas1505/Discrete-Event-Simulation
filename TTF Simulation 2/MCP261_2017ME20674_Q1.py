import random
import math
import numpy as np
random.seed(1234)


def Failure():
  global Clock
  global NextFailure
  global NextRepair
  global S
  global Slast
  global Tlast
  global Area
  
  S=S-1
  if S in range (1,n) :
    NextFailure = Clock + random.randint(1,5)*2  
  if NextRepair>100000:  
    NextRepair = Clock + 3.5
  else:
    NextRepair=NextRepair
    
  
  Area = Area + Slast * (Clock - Tlast)
  Tlast = Clock
  Slast = S

def Repair():
  global Clock
  global NextFailure
  global NextRepair
  global S
  global Slast
  global Tlast
  global Area
 
  S=S+1
  if S in range(1,n):
    if NextFailure>100000: 
      nextFailure = Clock + random.randint(1,5)*2
    else:
      NextFailure=NextFailure  
    NextRepair = Clock + 3.5
    
    
  
  Area = Area + Slast * (Clock - Tlast)
  Tlast = Clock
  Slast = S

def Timer():
  Infinity=1000000
  global Clock
  global NextFailure
  global NextRepair

  if NextFailure < NextRepair:
     y = 'Failure'
     Clock = NextFailure
     NextFailure = Infinity
  else:
     y = 'Repair'
     Clock = NextRepair
     NextRepair = Infinity
  return y


global Clock             
global NextFailure      
global NextRepair       
global S                
global Slast            
global Tlast            
global Area             



Infinity = 1000000

SumS=0
SumY=0


n=5 # Number of machines

for rep in range(1,101):
  S=n
  Slast=n
  Clock=0
  Tlast=0
  Area=0

  NextFailure = random.randint(1,5)*2
  NextRepair = Infinity

  while S!=0:
    NextEvent=Timer()
    if NextEvent == 'Failure':
      Failure()
    if NextEvent == 'Repair':
      Repair()

  SumS=SumS+Area/Clock
  SumY=SumY+Clock


  
print('Average failure time of system',SumY/100)
print('Average functional components', SumS/100)
