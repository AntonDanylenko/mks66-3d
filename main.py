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

#parse_file( 'script', edges, transform, screen, color )

screen2 = new_screen()
transform = new_matrix()
bowl = []
cx = 250
cy = 200
cz = 0
r = 20
height = 0
while height<=100:
    add_torus(bowl, cx, cy+height, cz, 20, r, 0.01)
    r+=20
    height=int((r**4)/1000000.0)
parse_file('script2', bowl, transform, screen2, color)
