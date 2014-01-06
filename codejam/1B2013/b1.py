import sys
import os
import math
import decimal
from fractions import Fraction as F

def _float_of_fraction(fraction):
    decimal.getcontext().prec = 6
    return (decimal.Decimal(fraction.numerator)/decimal.Decimal(fraction.denominator)).__str__()

def calculate_probability(point1,point2,y_stop,state,prb):
    #print state
    total = 0
    for vl in state.values():
        total += vl
    count = {}
    
    x = point1[0]
    y = point1[1]
    while x < 0 and y <= y_stop:
        if (x+y)%2 == 0:
            for k,c in state.items():
                a,b = k
                if a > y:
                    if (x,y) in count:
                        count[(x,y)] += c
                    else:
                        count[(x,y)] = c
            if (x,y) in count:
                prb[(x,y)] = _float_of_fraction(F(count[(x,y)],total))
        x += 1
        y += 1 
    
    x = point2[0]
    y = point2[1]
    while x > 0 and y <= y_stop:
        if (x+y)%2 == 0:
            for k,c in state.items():
                a,b = k
                if b > y:
                    if (x,y) in count:
                        count[(x,y)] += c
                    else:
                        count[(x,y)] = c
            if (x,y) in count:
                prb[(x,y)] = _float_of_fraction(F(count[(x,y)],total))
        x -= 1
        y += 1             
        
def calculate_last_layer(n,x,y,x_run,y_stop):
    prb = {}
    sure = 0
    #y_stop = 1
    #x_run = 2
    layer = []
    for i in xrange(n):   
        if not layer:
            layer.append( {(0,1):1,(1,0):1} )           
        else:
            total_of_state = 0
            t = {}
            for it,c in layer[-1].items():
                if it[1]+1 <= y_stop+1:
                    if (it[0],it[1]+1) in t:
                        t[(it[0],it[1]+1)] += c
                    else:
                        t[(it[0],it[1]+1)] = c 
                if it[0]+1 <= y_stop+1:
                    if (it[0]+1,it[1]) in t:
                        t[(it[0]+1,it[1])] += c
                    else:
                        t[(it[0]+1,it[1])] = c
            #print len(t)
            #print prb
            #print "-------------------------"
            layer.append(t)    
    if not layer:
        return '0.0'
    calculate_probability((-x_run,0),(x_run,0),y_stop,layer[-1],prb)
    #print x,y,prb
    return prb[(x,y)] if (x,y) in prb else '0.0'     

def get_diamonds_of_last_layer(n):
    for m in xrange(n,0,-1):
        c = -2*m
        denta = (1-4*1*c)
        n1 = float(-1 + math.sqrt(denta)) / 2.0
        temp = round(n1)
        if n1 > 0 and n1%2 == 1 and temp == n1:
            rs = n-m
            return rs,int(n1)
    return n,-1       
def solve(n,x,y):
    if x == 0 and y == 0:
        return '1.0'
    diamonds,good_zone_location = get_diamonds_of_last_layer(n)  
    #print diamonds,good_zone_location      
    if good_zone_location == -1:
        return calculate_last_layer(diamonds,x,y,good_zone_location+1,good_zone_location)
    else:
        if abs(x) + abs(y) <= good_zone_location -1:
            return '1.0'
        else:
            return calculate_last_layer(diamonds,x,y,good_zone_location+1,good_zone_location)

T = int(sys.stdin.readline().strip())
case = 1
for _ in xrange(T):
    n,x,y = map(int,sys.stdin.readline().split(" "))
    rs = solve(n,x,y)
    print "Case #%d: %s" %(case,rs)
    case += 1
