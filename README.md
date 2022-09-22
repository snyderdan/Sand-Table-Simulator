# Sand-Table-Simulator

Requires pyautogui to be installed.

This simulation will move the mouse in ways to simulate the motion of a sand table (in the works).
It is intended to be run on a blank Paint canvas, in order to draw the patterns that would
emerge on a sand table.

sand_table_simulator.py is the core of the simulation, sample_driver.py is
just a demo of actually driving the table.

The sand_table_simulator.py has 2 functions:
    moveTo(theta, radius)
    resetTable()

moveTo will pace the drawing to match the speed of the motors. You can
optionally pass a speed= parameter between 0 and 1 to scale the speed.
If the motion you see on screen is extremely sporadic, you're telling
the motors to move too fast.

To run the sample driver:
    1) Open sample_driver.py in IDLE, and click run.
    2) Open up a blank Paint window and select your brush of choice.
    3) Type run(unitCircle) but DON'T press enter yet.
    4) Position your mouse in the center of the Paint window.
    5) Tab back to IDLE, and press enter. 
