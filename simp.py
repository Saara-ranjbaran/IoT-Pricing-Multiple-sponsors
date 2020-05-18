import simpy
def car(env):
     while True:
         print('Start parking at %d' % env.now)
         parking_duration = 5
         yield env.timeout(parking_duration)


env = simpy.Environment()
env.process(car(env))

env.run(until=30)