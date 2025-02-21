#Code author: Akilan
import random
def barycenter_coordinates(p1,p2,p3,p4):
    """u, v, w are the barycentric co-ordinates sums up to the value 1"""
    while True:
        u=random.random()
        v=(1-u)*random.random()
        w=1-u-v
        if len(p1)==len(p2)==len(p3)==len(p4)==3:
            x1,y1,z1=p1
            x2,y2,z2=p2
            x3,y3,z3=p3
            x4,y4,z4=p4
            """finding average point that relies inside the quadrilateral co-ordinates"""
            average_point1=(((u*x1)+(v*x2)+(w*x3)), ((u*y1)+(v*y2)+(w*y3)), ((u*z1)+(v*z2)+(w*z3)))
            yield average_point1
            average_point2=(((u*x1)+(v*x3)+(w*x4)), ((u*y1)+(v*y3)+(w*y4)), ((u*z1)+(v*z3)+(w*z4)))
            yield average_point2

"""Provide cyclic quadrilateral orordinates"""
triangle_coordinates=barycenter_coordinates(p1=[0,0,0], p2=[1,0,0], p3=[1,1,0], p4=[0,1,0])
"""writing the inside quadrilateral points in csv format"""
output_file=open(r"C:\Users\akilar\Desktop\test\result.csv", 'w')
for step in range(10000):
    points=next(triangle_coordinates)
    output_file.write(str(points[0])+ ',' + str(points[1])+ ',' + str(points[2]) + '\n')
output_file.close()