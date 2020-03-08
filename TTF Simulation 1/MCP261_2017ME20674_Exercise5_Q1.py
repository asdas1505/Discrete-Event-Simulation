import math
import random
import numpy as np
from scipy import stats

def Failure():
    
    global Clock            # Simulation clock
    global NextFailure      # Time of next failure event
    global NextRepair       # Time of next repair event
    global S                # System state
    global Slast            # Previous value of the system state
    global Tlast            # Time of previous state change
    global Area             # Area under S(t) curve
   # Failure event
   # Update state and schedule future events

    S = S - 1;
    if (S == 1):      
        NextFailure = Clock +  math.ceil(6 * np.random.uniform(0, 1))
        NextRepair = Clock + 2.5
        
        
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
        NextRepair = Clock + 2.5
        NextFailure = Clock + math.ceil(6 * np.random.uniform(0, 1))
    Area = Area + Slast * (Clock - Tlast)
    Tlast = Clock
    Slast = S


def Timer():
    Infinity = 1000000;
    global Clock            # simulation clock
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

Infinity = 100000000
random.seed(0)
    
# Define and initialize replication variables
SumS = 0
SumY = 0
timeList = []
avgCompList = []

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
    timeList.append(Clock)
    avgCompList.append(Area / Clock)
    SumS = SumS + Area / Clock;
    SumY = SumY + Clock;

    
# Display output
print('Average failure at time:', SumY / 100);
print('Average functional components:', SumS / 100)
# Time array using python
timeArrayPython = np.array(timeList)
avgCompArrayPython = np.array(avgCompList)

# Time array using matlab
timeArrayMatlab = np.array([12,11,19,21,25,36,6,3,13,7,18,22,10,19,7,26,3,8,7,11,33,18,17,8,4,7,5,6,18,9,
                            16,4,7,17,5,16,3,16,21,3,4,4,31,10,4,18,11,3,22,7,7,13,22,63,7,8,4,7,11,16,
                            11,11,3,10,8,20,19,25,18,11,6,39,44,9,5,19,6,6,16,35,3,14,20,4,8,6,19,7,24,24,
                            9,18,13,15,7,6,9,8,24,19])

# functional components array using matlab
avgCompArrayMatlab = np.array([1.7083,1.6818,1.5526,1.5952,1.5600,1.5278,1.8333,1.6667,1.4615,1.8571,1.4722,1.4545,1.6500,1.3684,1.7143,1.5769,1.3333,1.7500,
                              1.7143,1.5909,1.4091,1.5278,1.5000,1.5625,1.7500,1.7143,1.8000,1.6667,1.5278,1.6111,1.6250,1.7500,1.8571,1.6471,1.6000,1.5625,
                              1.6667,1.4688,1.4762,1.6667,1.5000,1.7500,1.4839,1.5500,1.7500,1.5278,1.4545,1.3333,1.4545,1.7143,1.7143,1.5385,1.4545,1.4524,
                              1.3571,1.7500,1.5000,1.3571,1.5909,1.6250,1.3636,1.5909,1.3333,1.4000,1.5625,1.5250,1.5000,1.4600,1.6667,1.4545,1.8333,1.5000,
                              1.4432,1.6111,1.6000,1.5526,1.8333,1.4167,1.6250,1.4714,1.3333,1.5714,1.4000,1.7500,1.7500,1.2500,1.5526,1.7143,1.5000,1.5000,
                              1.5000,1.4722,1.5385,1.5333,1.5000,1.6667,1.5000,1.4375,1.5417,1.6316]) 


# Applying t-test for python and the matlab version of simulation t0 check statistical identicality
t1, p1 = stats.ttest_ind(timeArrayPython,timeArrayMatlab)
t2, p2 = stats.ttest_ind(avgCompArrayPython,avgCompArrayMatlab)

# taking confidence intervar of 95%
alpha = 0.05

# Null hypothesis is not rejected if P value if greater than alpha(which is 0.05 in case of 95 percent confidence interval)
if(p1 > alpha):
    print("Means of faliure time are statisticaly identical")
else:
    print("Means of faliure time are statisticaly different")

if(p2 > alpha):
    print("Means of functional components are statisticaly identical")
else:
    print("Means of functional components are statisticaly different")


