from display import *
from draw import *

screen = new_screen()
color = [186, 212, 255]

clear_screen(screen)

for x in range(50):
    for y in range(50):
        draw_line(x*10, y*10, x*10, y*10, screen, color)

for x in range(25):
    draw_line(0, 10*x, 10*x, 0, screen, color)
    draw_line(10*x, 20*x, 20*x, 10*x, screen, color)
    draw_line(0, 10*x, 10*x, 20*x, screen, color)
    draw_line(20*x, 10*x, 10*x, 0, screen, color)

    

display(screen)
save_extension(screen, 'img.png')
