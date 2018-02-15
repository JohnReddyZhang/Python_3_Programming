def circleWithD(diameter):
    import math
    area = math.pi * (diameter/2)**2
    return area
def circleWithR(radius):
    import math
    area = math.pi * (radius**2)
    return area
def traingle(base,height):
    area = 0.5 * base * height
    return area
def rectangles(length, width):
    area = length * width
    return area
def area(shape, **kwargs):
    if shape == 'rectangles':
        return(rectangles(kwargs['length'],kwargs['width']))
    elif shape == 'traingle':
        return(triaingle(kwargs['base'],kwargs['height']))
    elif shape == 'circle':
        if 'radius' in kwargs:
            return(circleWithR(kwargs['radius']))
        if 'diameter' in kwargs:
            return(circleWithD(kwargs['diameter']))
#TEST:
# print('circle a area is {}'.format(area('circle', radius=10)))
# print(area('rectangles', length=20, width=23))
