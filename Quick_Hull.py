#By Tonia Alderbashi
#QuickHull program
import sys
sys.setrecursionlimit(10000000)

from graphics import *
from random import randrange

def quickhull(points):

    """This function calls the halfhull() function two times on two
        different sets of points. The points 'above' the p1-pn line,
        and the points 'below' it. quickhull() also precalculates the
        determinants needed for halfhull(), to avoid recalculating. 
    """

    if len(points) > 2:
        
        p1, pn = min(points), max(points)
        

        #computes determinants of all the points (efficiency) 
        #determ_lst = [determ(p1, pn, p) for p in points]

        determ_lst = []
        for point in points:
            det = determ(p1, pn, point)
            determ_lst.append(det)

        #make a set for all points 'left' of the line p1-pn 
        s1 = [p for p in points if determ(p1, pn, p) > 0]

        #positive determinants for s1
        #s1_determs = [(points[p], determ_lst[p]) for p in range(len(points))
                      #if determ_lst[p] > 0]
        
        s1_determs = []
        for det in determ_lst:
            if det > 0:
                s1_determs.append(det)

        #make a set for all points 'right' of the line p1-pn
        s2 = [p for p in points if determ(pn, p1, p) > 0]

        #negative determinants for s2
        #s2_determs = [(points[p], determ_lst[p]) for p in range(len(points))
                      #if determ_lst[p] < 0]

        s2_determs = []
        for det in determ_lst:
            if det < 0:
                s2_determs.append(det)
        #print(s2_determs)

        upper = halfhull(p1, pn, s1, s1_determs)
        lower = halfhull(pn, p1, s2, s2_determs)
        upper.extend(lower)
        

        #covex_hull = [p1] + upper + [pn] + lower
        convex_hull = upper
        
        #covex_hull = upper
       
        return convex_hull
    

    else:
        return points

def find_pmax(p1, pn, s):
    determ_max = 0
    pmax = 0
    

    
    for p in s:
        det = abs(determ(p1, pn, p))
        if det > determ_max:
            determ_max = det

            pmax = p
    
    return pmax

def halfhull(p1, pn, s, determinants = []):
    
    if len(s) == 0:
        return [(p1, pn)]
    
    

    
    
    p = find_pmax(p1, pn, s)
    

    

    
    determinants_l = []
    s_left = []

    for point in s:
        det = determ(p1, p, point)
        if det > 0:
            s_left.append(point)
            determinants_l.append(determ(p1, p, point))
    
    determinants_r = [determ(p, pn, point) for point in s]

    determinants_r = []
    s_right = []

    for point in s:
        det = determ(p, pn, point)
        if det > 0:
            s_right.append(point)
            determinants_r.append(determ(p, pn, point))
    
    

    return halfhull(p1, p, s_left, determinants_l) + halfhull(p, pn,
            s_right, determinants_r)

    

    #print(s_left)

def determ(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    determinant = x1*y2 + x3*y1 + x2*y3 -x3*y2 - x2*y1 - x1*y3

    return determinant




def main():


    #Collaborated with Isaac ans Vanja on this part of the code
    n = int(input("Enter number of points ==> "))
    points = [(randrange(150,650),randrange(150,650)) for i in range (n)]

    win = GraphWin("quickhull", 800, 800)

    for point in points:
                
            c = Circle(Point(point[0],point[1]),2)
            
            c.setFill("red")
            
            c.draw(win)

    lines = quickhull(points)
    for line in lines:
        x1 =line[0][0]
        y1= line[0][1]

        x2 =line[1][0]
        y2= line[1][1]
        
        l = Line(Point(x1,y1), Point(x2,y2))
        l.draw(win)

main()
