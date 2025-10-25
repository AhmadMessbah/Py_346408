from model import Employee
from model import EmployeeService


service = EmployeeService()
#
# employee1 = Employee( 1 , "ali" , "mohammadi" , 3000 , "foroosh" , 9121998381 , "alimo" , "ali987","foroshande")
# service.save(employee1)
#
# employee2 = Employee( 2 , "taranom" , "bagheri" , 4000 , "manage" , 9127846381 , "tariii" , "taranom876","manager")
# service.save(employee1)
#
# employee3 = Employee( 3 , "kiarash" , "hoseyni" , 2000 , "program" , 9121947681 , "kiahosei" , "kiarash765","programer")
# service.save(employee3)
#
#
# employee4 = Employee( 4 , "adrina" , "joorabchi" ,  4000, "foroosh" , 9126746381 , "adrinef" , "adrina654","foroshande")
# service.save(employee4)
#
#
# employee5 = Employee( 5 , "malihe" , "asady" , 3678 , "manage" ,9125436756 , "amalyasdy" , "malihe543","manager")
# service.save(employee5)
#
# employee6 = Employee( 6 , "mahdis" , "bakhshi" , 3093 , "sale" , 9122254534 , "mmmht" , "mahds321","saler")
# service.save(employee6)
#
# # print(service.find_by_firstname_and_lastname("adrina" , "joorabchi"))


print(service.find_by_username_and_password("ali", "ali123"))