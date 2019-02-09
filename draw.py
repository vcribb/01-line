from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    if x0 > x1:
        tempOne = x0
        x0 = x1
        x1 = tempOne
        tempTwo = y0
        y0 = y1
        y1 = tempTwo

    #vertical line
    if x1 == x0:
        x = x0
        y = 0
        yFin = 0
        if y0 > y1:
            y = y1
            yFin = y0
        else:
            y = y0
            yFin = y1
        while y <= yFin:
            plot(screen, color, x, y)
            y+=1

    #horizontal line
    elif y1 == y0:
        y = y0
        x = x0
        while x <= x1:
            plot(screen, color, x, y)
            x+=1

    else:
        x = x0
        y = y0
        a = y1 - y0
        b = x0 - x1
        if a > 0:
            #if the slope is less than 1, use octant one
            if -1*a > b:
                d = 2*a + b
                while x <= x1:
                    plot(screen, color, x, y)
                    if d > 0:
                        y+=1
                        d+=2*b
                    x+=1
                    d+=2*a
            #otherwise, use octant two
            else:
                d = a + 2*b
                while y <= y1:
                    plot(screen, color, x, y)
                    if d < 0:
                        x+=1
                        d+=2*a
                    y+=1
                    d+=2*b
        else:
            #if the slope is less than -1, use octant seven
            if a < b:
                d = 2*b - a
                while y >= y1:
                    plot(screen, color, x, y)
                    if d < 0:
                        x+=1
                        d-=2*a
                    y-=1
                    d+=2*b
            #otherwise, use octant eight
            else:
                d = b - 2*a
                while x <= x1:
                    plot(screen, color, x, y)
                    if d > 0:
                        y-=1
                        d+=2*b
                    x+=1
                    d-=2*a
pass

