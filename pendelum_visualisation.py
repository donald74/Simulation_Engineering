#!/usr/bin/env python
# coding: utf-8

#imports
from vpython import *
import numpy as np 
from math import * 
from matplotlib import pyplot as plt 
from scipy.integrate import odeint
import random as rn
#instantiate simulation
display(width=600,height=600,center=vector(0,12,0),background=color.white)
bob=sphere(pos=vector(5,2,0),radius=0.5,color=color.white)
pivot=vector(0,20,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.white)
rod=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.white)
# define the equations
def equations(y0, t):
	theta, x = y0
	f = [x, -(g/l) * sin(theta)]
    
	return f


    
# here we have the start time 0.0, end time 20, and the time step is 0.1.

time = np.arange(0.0, 20.0, 0.1)

#parameters and constants
#assume length as 1
dt = 0.1
l = 1

# g represent the gravity
g = 9.81

# initial conditions of the start angle of the pendelum

initial_theta = rn.uniform(55, 65)

theta0 = np.radians(initial_theta)

x0 = np.radians(rn.uniform(0.25, 0.35))

start_time=0 # time 
dt=0.01 # time interval 
# find the solution to the nonlinear problem
# odeint is a function wich is used to derivate and integrate our values.
# equation represent the model that return derivative request
# theta0, x0 are initial condition of the differential states 
# theata1 is a table of differents value of the pendelum between 0 and 20 sec.

theta1 = odeint(equations, [theta0, x0],  time)


l=mag(bob.pos-pivot) # length of pendulum
cs=(pivot.y-bob.pos.y)/l # calculation of cos(theta) 
theta=acos(cs) # angle with vertical direction
vel=0.5 # angular velocity



vel=1.0 # angular velocity

while (start_time<100):
  rate(100) # maximum 100 calculations per second
  acc=-g/l*sin(theta) # updating of angular acceleration
  theta=theta+vel*dt # updating of angular position
  vel=vel+acc*dt # updating of angular velocity
  bob.pos=vector(l*sin(theta),pivot.y-l*cos(theta),0) # cal. position
  rod.axis=bob.pos-rod.pos # updating other end of rod of pendulum
  start_time=start_time+dt # updating time







