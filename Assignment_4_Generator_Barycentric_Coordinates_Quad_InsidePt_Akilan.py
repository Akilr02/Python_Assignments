#Code author: Akilan
import math
import random

def tria_gen(p1,p2,p3):
    """u, v, w are the barycentric co-ordinates sums up to the value 1"""
    while True:
        u=random.random()
        v=(1-u)*random.random()
        w=1-u-v
        if len(p1)==len(p2)==len(p3)==3:
            x1,y1,z1=p1
            x2,y2,z2=p2
            x3,y3,z3=p3
            """finding average point that relies inside the triangle co-ordinates"""
            average_point=(((u*x1)+(v*x2)+(w*x3)), ((u*y1)+(v*y2)+(w*y3)), ((u*z1)+(v*z2)+(w*z3)))
            yield average_point

def insidePoint_Quad(p1, p2, p3, p4):
      "find smaller & bigger tria areas and check condition"
      a1 = math.dist(p1, p2)
      b1 = math.dist(p2, p4)
      c1 = math.dist(p4, p1)
      s1 = ((a1 + b1 + c1) / 2)
      Area_T1 = (math.sqrt(s1 * (s1 - a1) * (s1 - b1) * (s1 - c1)))
      a2 = math.dist(p2, p3)
      b2 = math.dist(p3, p4)
      c2 = math.dist(p4, p2)
      s2 = ((a2 + b2 + c2) / 2)
      Area_T2 = (math.sqrt(s2 * (s2 - a2) * (s2 - b2) * (s2 - c2)))
      a3 = math.dist(p1, p2)
      b3 = math.dist(p2, p3)
      c3 = math.dist(p1, p3)
      s3 = ((a3 + b3 + c3) / 2)
      Area_T3 = (math.sqrt(s3 * (s3 - a3) * (s3 - b3) * (s3 - c3)))
      a4 = math.dist(p1, p3)
      b4 = math.dist(p3, p4)
      c4 = math.dist(p4, p1)
      s4 = ((a4 + b4 + c4) / 2)
      Area_T4 = (math.sqrt(s4 * (s4 - a4) * (s4 - b4) * (s4 - c4)))
      if abs(Area_T1+Area_T2+Area_T3 -Area_T4) <=1e-10:
         return True

def quad_gen(p1,p2,p3,p4):
      "consider point 2 is inside, plot points for 1,2,4 and 2,3,4 triangles"
      if insidePoint_Quad(p1,p2,p3,p4):
          tg1=tria_gen(p1,p2,p4)
          tg2=tria_gen(p2,p3,p4)
          "consider point 1 is inside, plot points for 1,3,4 and 1,2,3 triangles"
      elif insidePoint_Quad(p4,p1,p2,p3):
          tg1=tria_gen(p1,p3,p4)
          tg2=tria_gen(p1,p2,p3)
          "consider point 4 is inside, plot points for 1,2,4 and 2,3,4 triangles"
      elif insidePoint_Quad(p3,p4,p1,p2):
          tg1=tria_gen(p1,p2,p4)
          tg2=tria_gen(p2,p3,p4)
          "consider point 2 is inside, plot points for 1,3,4 and 1,2,3 triangles"
      elif insidePoint_Quad(p2,p3,p4,p1):
          tg1=tria_gen(p1,p3,p4)
          tg2=tria_gen(p1,p2,p3)
      else:
          print("provide correct co ordinate values")
          return
      while True:
          yield next(tg1)
          yield next(tg2)


"""Provide quadrilateral orordinates"""
coordinates=quad_gen([0,0,0], [0.5,-1.076157361269,0], [1,-0.49060314148664,0], [0.5,-0.77156987041235,0])
"""writing the quadrilateral points in csv format"""
output_file=open(r"C:\Users\akilar\Desktop\test\result2.csv", 'w')
for step in range(10000):
    points=next(coordinates)
    output_file.write(str(points[0])+ ',' + str(points[1])+ ',' + str(points[2]) + '\n')
output_file.close()