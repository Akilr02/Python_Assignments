#Code author: Akilan
def range_function(*args):
    """If only one variable given below codes does range function"""
    if len(args)==1:
        first_value=1
        while first_value <= (args[0]-1):
            yield first_value
            first_value+=1
    """If two variables given and if first value is lesser than second value, below codes does range function"""
    if len(args)==2:
        first_value=args[0]
        while first_value<args[1]:
            yield first_value
            if first_value==args[1]-1:
                break
            else:
                second_value=first_value+1
                first_value=second_value
    """If three variables given and if first value is lesser than second value with positive step value, below codes does range function"""
    if len(args)==3:
        first_value=args[0]
        while first_value<args[1]:
            yield first_value
            if first_value>=args[1]-args[2]:
                break
            else:
                second_value=first_value+args[2]
                first_value=second_value
        """If three variables given and if first value is greater than second value with negative step value, below codes does range function"""
        while first_value>args[1]:
            yield first_value
            if first_value>=args[1]+args[2]:
                second_value=first_value+args[2]
                first_value=second_value
            else:
                break
                

numbers=range_function(35, 20, -7)
for variables in numbers:
    print(variables)