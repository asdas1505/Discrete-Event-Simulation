import math
import random
import numpy as np

random.seed(1)


def Failure():
    
    global Clock            # simulation clock
    global NextFailure      # time of next failure event
    global NextRepair       # time of next repair event
    global S                # system state
    global Slast            # previous value of the system state
    global Tlast            # time of previous state change
    global Area             # area under S(t) curve

   # Failure event
   # Update state and schedule future events
    S = S - 1;
    if (S == 1):      
        NextFailure = Clock +  math.ceil(6 * np.random.uniform(0, 1))
        z = np.random.uniform(0,1)
        if(z <= 0.65):              
            NextRepair = Clock + 2.5
        else:
            NextRepair = Clock + 1.5
        
        
    # Update area under the S(t) curve
    Area = Area + Slast * (Clock - Tlast)
    Tlast = Clock
    Slast = S
    
def Repair():
    global Clock            # simulation clock
    global NextFailure      # time of next failure event
    global NextRepair       # time of next repair event
    global S                # system state
    global Slast            # previous value of the system state
    global Tlast            # time of previous state change
    global Area             # area under S(t) curve
    
    # Repair event
    # Update state and schedule future events

    S = S + 1
    if (S == 1):
        z = np.random.uniform(0,1)
        if(z <= 0.65): 
            NextRepair = Clock + 2.5
        else:
            NextRepair = Clock + 1.5
            
        NextFailure = Clock + math.ceil(6 * np.random.uniform(0, 1))
    Area = Area + Slast * (Clock - Tlast)
    Tlast = Clock
    Slast = S


def Timer():
    Infinity = 1000000;
    global Clock            #  simulation clock
    global NextFailure      # time of next failure event
    global NextRepair       # time of next repair event
    
    # Determine the next event and advance time
    if NextFailure < NextRepair:
            y = 'Failure'
            Clock = NextFailure
            NextFailure = Infinity
    else:
        y = 'Repair'
        Clock = NextRepair
        NextRepair = Infinity
    
    return y


Infinity = 1000000
    
# Define and initialize replication variables
SumS = 0
SumY = 0

for Rep in range(100):
            
    # Initialize the state and statistical variables
    S = 2
    Slast = 2
    Clock = 0
    Tlast = 0
    Area = 0
        
    # Schedule the initial failure event
    NextFailure = math.ceil(6 * np.random.uniform(0,1))
    NextRepair = Infinity;

    # Advance time and execute events until the system fails
    while (S != 0):
        
        NextEvent = Timer()
        if NextEvent == 'Failure':
            Failure()
        else:
            Repair()
          
        
   # Accumulate replication statistics
    SumS = SumS + Area / Clock;
    SumY = SumY + Clock;

# Display output
print('Average failure at time: ', SumY / 100 );

