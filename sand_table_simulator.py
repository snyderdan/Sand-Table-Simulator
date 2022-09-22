import pyautogui, math

# based on stepper motor 28BYJ-48 12V with 1:16 internal reduction
# https://www.adafruit.com/product/918
STEPS_PER_REV = 516.096
MAX_RPM = 20

# mechanical variables
# units are in mm
ARM_RADIUS = 180          # ~ 7in
PULLEY_PITCH_DIAM = 12.73 # 20T GT2 pulley
PULLEY_REDUCTION = 3
ARM_REDUCTION = 1
PIXELS_PER_MM = 2         # rendering parameter

# computed variables to simulate physical behavior
STEPS_PER_RADIAN = STEPS_PER_REV / ARM_REDUCTION / 2 / math.pi
STEPS_PER_MM = STEPS_PER_REV / PULLEY_REDUCTION / PULLEY_PITCH_DIAM / math.pi
SEC_PER_STEP = 60 / MAX_RPM / STEPS_PER_REV

curTheta = 0
curRadius = 0
center = pyautogui.position()

def resetTable():
    global center, curTheta, curRadius
    curTheta = 0
    curRadius = 0
    center = pyautogui.position()

def moveTo(theta, radius, speed=1):
    ''' move to polar position specified by (theta, radius)
        Radius should be bound to [0,1]
        speed is [0,1] proportion of maximum speed to move '''
    global curTheta, curRadius, center
    dTheta = curTheta - theta
    dRadius = curRadius - radius
    tangentTime = abs(dTheta * STEPS_PER_RADIAN * SEC_PER_STEP)
    radialTime = abs(dRadius * ARM_RADIUS * STEPS_PER_MM * SEC_PER_STEP)
    movementTime = max(tangentTime, radialTime)
    
    xRel = radius * math.cos(theta) * ARM_RADIUS * PIXELS_PER_MM
    yRel = radius * math.sin(theta) * ARM_RADIUS * PIXELS_PER_MM
    xDest = center.x + xRel
    yDest = center.y + yRel
    pyautogui.dragTo(xDest, yDest, movementTime)
    curTheta = theta
    curRadius = radius
