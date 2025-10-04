import math

# Class of polygon 
class Polygon():
    def __init__(self, vertices):
        self._listOfVertices = vertices
        self._numOfSides = len(vertices)

    def _get_listOfVertices(self):
        return self._listOfVertices
    
    def _get_numOfSides(self):
        return self._numOfSides
        
# Function to check if the polygon is convex polygon or not
def isConvex(Polygon):
    vertices = Polygon._get_listOfVertices()
    sign = [0, 0]

    num = Polygon._get_numOfSides()

    if (num < 3):
        return False

    for i in range(num):
        p1 = vertices[i]
        p2 = vertices[(i+1)%num]
        p3 = vertices[(i+2)%num]

        # 計算外積(z 方向當作 0)
        cross = (p2[0]-p1[0]) * (p3[1]-p2[1]) - (p2[1]-p1[1]) * (p3[0]-p2[0])

        if (cross > 0):
            sign[0] += 1
        elif (cross < 0):
            sign[1] += 1
    
    if (sign[0] > 0 and sign[1] > 0):
        return False
    
    return True


# Driver script
if __name__ == '__main__':
    #sample input polygon
    vertices = [ [ 0, 0 ], [ 0, 1 ], 
                 [ 1, 1 ], [ 1, 0 ] ]
    p=Polygon(vertices)
    result="is" if (isConvex(p)) else "is not"
    print(f"The given polygon {p._get_listOfVertices()} {result} convex.")