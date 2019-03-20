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
color2 = [0,0,0]
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
parse_file('script2', bowl, transform, screen2, color2)
