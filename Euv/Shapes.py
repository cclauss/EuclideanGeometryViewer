"""
Various polygonal shapes
"""
import math

def rotate(x,y,angle):
  sa = math.sin(angle)
  ca = math.cos(angle)

  xp = x*ca - y*sa
  yp = x*sa + y*ca
  return xp,yp

def rotate_and_move_poly(polygon, angle, pos, scale=1.0):
  """rotate and move a polygon"""
  rotated_polygon = []
  for x,y in polygon:
    xp,yp = rotate(x,y,angle)
    rotated_polygon += [(scale*xp+pos[0],scale*yp+pos[1])]
  return rotated_polygon
  
def arrow_head_polygon(pos,
                       angle=0,
                       length=10,
                       width=10,
                       dip=3,
                       center_offset=5,
                       scale=1.0):
  """Create a rotated arrow head at position x,y in the direction angle.
  """
  # Unroted coordinates around zero. "dip" at (0,0)
  unrot_poly = [[0,center_offset-dip],
                [width/2,center_offset],
                [0,-(length-center_offset)],
                [-width/2,center_offset]]

  # Add pi/2 to make arrow point forward by default
  return rotate_and_move_poly(unrot_poly, angle+math.pi/2, pos, scale=scale)

def rotated_rectangle(pos,
                      angle=0,
                      width=2,
                      height=1,
                      scale=1.0):
  """Create a rotated rectangle at position x,y in the direction angle.
  """
  # Unroted coordinates around zero. "dip" at (0,0)
  unrot_poly = [[-width*0.5,-height*0.5],
                [width*0.5,-height*0.5],
                [width*0.5,height*0.5],
                [-width*0.5,height*0.5]]

  # Add pi/2 to make arrow point forward by default
  return rotate_and_move_poly(unrot_poly, angle, pos, scale=scale)

def rectangle_pair(pos,
                   rectangle_width,
                   rectangle_height,
                   rectangle_center_distance,
                   angle=0,
                   left_angle=0,
                   right_angle=0,
                   scale=1.0):
  """A rectangle pair may be used for drawing two wheels"""
  p_left = rotated_rectangle((0,-0.5*rectangle_center_distance),
                             left_angle,
                             rectangle_width,
                             rectangle_height)
  p_right = rotated_rectangle((0,0.5*rectangle_center_distance),
                              right_angle,
                              rectangle_width,
                              rectangle_height)
  p_left = rotate_and_move_poly(p_left, angle, pos, scale=scale)
  p_right = rotate_and_move_poly(p_right, angle, pos, scale=scale)

  return (p_left, p_right)
                   
