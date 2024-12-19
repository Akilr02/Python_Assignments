#Code author: Akilan
def find_centroid(*args):
    """Gives centroid for any number of values provided in whatsoever dimensions """
    points=[]
    co_or=[]
    for i in args:
        dimensions=len(i)
        points.append(dimensions)
    #print(points)
        max_d=0
        for j in points:
            if j > max_d:
                max_d=j
    for k in args:
        #print(len(k))
        zeros_left=max_d-len(k)
        #print(zeros_left)
        l=k+([0]*zeros_left)
        #print(l)
        co_or.append(l)
    #print(co_or)
    cen=[]
    for m in zip(*co_or):
        avg=round((sum(m)/len(m)), 3)
        cen.append(avg)
    return cen


result=find_centroid([1, 2, 3], [4, 5, 6, 7])
print(result)
