#Code author: Akilan
def find_area_volume_stl(filename):
    """Provide stl file path for which area and vol;ume should be returned"""
    File=open(filename, "r")
    import math
    co_or=[]
    Total_Area=0
    vol=0
    Model=File.readlines()
    for i in Model:
        if "normal" in i or "vertex" in i:
            som = [float(x1) for x1 in i.split()[-3:]]
            #print(som)
            co_or.append(som)
            #print(co_or)
            if len(co_or)==4:
                [n, p1,p2,p3]=co_or
                #print(co_or)
                co_or.clear()
                a = math.dist(p1, p2)
                b = math.dist(p2, p3)
                c = math.dist(p3, p1)
                s = ((a + b + c) / 2)
                Area_T = (math.sqrt(s * (s - a) * (s - b) * (s - c)))
                # print("Area of the triangle by Heron's formula is: ", Area_T, "mm2")
                Total_Area = Total_Area + Area_T
                ap=[sum(v)/3 for v in zip(p1,p2,p3)]
                vol=vol+((ap[0]*n[0]+ap[1]*n[1]+ap[2]*n[2])*(Area_T/3))

    #print("Area is", round(Total_Area,2), "mm2", "and Volume is", round(vol, 5), "mm3")
    return Total_Area, vol
    #return str(Total_Area)+"mm2", str(vol)+"mm2"


area, volume = find_area_volume_stl("Unbend_Model 4")
print(f"{area} mm2, {volume} mm3")
#print(area, volume)
