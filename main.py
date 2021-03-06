from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

parse_file( 'script', edges, transform, screen, color )

'''screen2 = new_screen()
transform = new_matrix()
color2 = [255,255,255]
color3 = [255,255,0]
bowl = []
cx = 250
cy = 150
cz = 0
r = 5
height = 0
while height<=150:
    add_torus(bowl, cx, cy+height, cz, 5, r, 0.01)
    r+=5
    height=int((r**4)/9000000.0)
fruit = []
add_sphere(fruit, 250, 205, 0, 50, 0.01)
add_box(bowl, 245, -100, -5, 10, 250, 10)
parse_file('script2', fruit, transform, screen2, color3)
parse_file('script2', bowl, transform, screen2, color2)
save_extension(screen2, 'bowl.png')
'''
