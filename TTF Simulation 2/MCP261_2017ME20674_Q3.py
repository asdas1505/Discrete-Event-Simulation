import simpy
import numpy
numpy.random.seed(1234)

def car(env):
  while True:
    print('start parking at %d'% env.now)
    parking_duration=numpy.random.normal(20,1)
    yield env.timeout(parking_duration)

    print('start driving at %d'% env.now)
    trip_duration = numpy.random.exponential(30)
    yield env.timeout(trip_duration)

env=simpy.Environment()
env.process(car(env))
env.run(until=1000)
