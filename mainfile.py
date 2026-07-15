import numpy as np
import math
import random

#useful functions
def fib_theta(n):
    return [math.acos(1-(2*(i+1)/float(n))) for i in range(n)]

def fib_phi(n):
    pi=3.141592653589793
    gratio=1.618033988749895
    return [(2*(i+1)*pi)/gratio for i in range(n)]

def format_transout(inp):
    inplist=np.array(inp.replace("{", "").replace("}", "").split(), dtype='float64')
    outlist=inplist.reshape([4, 4]).T.flatten()
    return outlist

def gen_2grid(pos, xdim, ydim, zdim, npoints):
    xpos=np.linspace(int(pos[0])-xdim, int(pos[0])+xdim, num=npoints)
    ypos=np.linspace(int(pos[1])-ydim, int(pos[1])+ydim, num=npoints)
    zpos=np.linspace(int(pos[2])-zdim, int(pos[2])+zdim, num=npoints)
    return xpos, ypos, zpos



if __name__=="__main__":
    fib_theta(100)
    fib_phi(20)
    gen_2grid(pos=[0.0, 1.0, -1.0], xdim=10, ydim=10, zdim=10, npoints=11)

