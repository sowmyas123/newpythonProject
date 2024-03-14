import math
def sq_rt(num):
    return math.sqrt(num)

my_list =[24, 47, 29]
sq_list =list(map(sq_rt, my_list))
print(sq_list)


#map is applied for list of items like list, set, tuple, dict

import math
def cb_rt(num):
    return math.cbrt(num)

c_list = [48, 28, 59]
cb_list = list(map(cb_rt, c_list))
print(cb_list)