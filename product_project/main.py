##natoonestam pakeyg hay mokhtalef dorost konm khata midad

from asly.asus import Asus
from asly.furniture import Furniture
from asly.iphone import IPhone
from asly.lenovo import Lenovo
from asly.samsung import Samsung

try:
    #iphone
    iphone1 = IPhone("Iphone15",
             "40000",
             "200",
             "17*15",
             "apple",
             "60")
    print(iphone1)



    #samsung
    samsung1 = Samsung("samsungA50",
               "2700000",
               "120",
               "13*24",
               "samsung",
               "43")
    print(samsung1)



    #asus
    asus1 = Asus("asus12",
         "85000000",
         "1200",
         "a500",
         "b120",
         "45")
    print(asus1)



    #lenovo
    lenovo1 = Lenovo("lenovo12",
             "670000",
             "1362",
             "q2349",
             "sam12",
             "190")
    print(lenovo1)



    #furniture
    furniture1 = Furniture("furnitureA+",
                   "900000",
                   "230kg",
                   "10")
    print(furniture1)

except Exception as e:
    print(e)

