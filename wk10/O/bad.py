class Circle:
    def __init__(self,radius):
        self.radius = radius

class Rectanggle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

def calculate_area(shape):
    if isinstance(shape,Circle):
        return 3.14*shape.radius ** 2
    elif isinstance(shape,Rectanggle):
        return shape.width * shape.height
    
    else:
        raise ValueError("Unknown shape")
        
        