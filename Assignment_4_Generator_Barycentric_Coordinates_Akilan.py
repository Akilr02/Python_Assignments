#Code author: Akilan
import random
def barycenter_coordinates(p1,p2,p3):
    """u, v, w are the barycentric co-ordinates sums up to the value 1"""
    while True:
        u=random.random()
        v=(1-u)*random.random()
        w=1-u-v
        if len(p1)==len(p2)==len(p3)==3:
            x1=p1[0]
            y1=p1[1]
            z1=p1[2]
            x2=p2[0]
            y2=p2[1]
            z2=p2[2]
            x3=p3[0]
            y3=p3[1]
            z3=p3[2]
            """finding average point that relies inside the triangle co-ordinates"""
            average_point=(((u*x1)+(v*x2)+(w*x3)), ((u*y1)+(v*y2)+(w*y3)), ((u*z1)+(v*z2)+(w*z3)))
            yield average_point


triangle_coordinates=barycenter_coordinates(p1=[1,0,0], p2=[0,1,0], p3=[0,0,0])
"""writing the inside triangle points in csv format"""
output_file=open(r"C:\Users\akilar\Desktop\test\result.csv", 'w')
for step in range(100000):
    points=next(triangle_coordinates)
    output_file.write(str(points[0])+ ',' + str(points[1])+ ',' + str(points[2]) + '\n')
output_file.close()