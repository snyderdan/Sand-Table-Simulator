from sand_table_simulator import moveTo, resetTable
import time
import math

def simpleRevolve(t):
    # 10s per revolution
    return t * 2 * math.pi / 10

def unitCircle(t, theta):
    return 1

def coolSpiral(t, theta):
    # change divisor to change pattern
    return math.sin(t / 15)

def run(rFunc, thetaFunc=simpleRevolve, cycles=100):
    resetTable()
    theta = 0
    radius = 0
    startTime = time.perf_counter()

    for i in range(cycles):
        t = time.perf_counter() - startTime
        theta = thetaFunc(t)
        radius = rFunc(t, theta)
        moveTo(theta, radius)
        if i == 0:
            # reset after moving to first position
            startTime = time.perf_counter()

# run(unitCircle)
# run(coolSpiral, cycles=10000)
