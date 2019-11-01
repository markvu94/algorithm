from math import sin, cos, sqrt, atan2, radians

def get_distance_from_last(lat_1,long_1,lat_2,long_2):
    # estimated Earth radius
    R = 6376
    # convert degree to radian
    lat1 = radians(lat_1)
    long1 = radians(long_1)
    lat2 = radians(lat_2)
    long2 = radians(long_2)
    # difference
    delta_long = long2 - long1
    delta_lat = lat2 - lat1
    # temp value (based on haversin)
    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_long / 2) ** 2
    b = 2 * atan2(sqrt(a), sqrt(1 - a))
    # distance
    distance = R * b
    return distance

# return the function of two point on graph
def get_f(point_1=[], point_2=[]):
    delta_y = point_2[1] - point_1[1]
    delta_x = point_2[0] - point_1[0]
    if delta_x == 0:
        delta_x = 0.01

    a = delta_y / delta_x
    b = point_1[1] - a * point_1[0]
    return a,b

