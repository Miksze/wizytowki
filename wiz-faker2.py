from pickle import APPEND
from re import A
from faker import Faker


class wizy:
   def __init__(self, name, surname, firm, position, email):
       self.name = name
       self.surname = surname
       self.firm = firm
       self.position = position
       self.email = email

faker = Faker()
bs = []
for i in range(1): 

    a = faker.first_name() 
    b = faker.last_name() 
    c = faker.company() 
    d = faker.job()
    e = faker.email()

    
    baza = wizy( name=a, surname=b, firm=c, position=d, email=e)
        
 #  bs.append(baza.name, baza.surname, baza.firm, baza.position, baza.email)
 #   print(bs)
 #   by_name = sorted(bs)
    print(baza.name, baza.surname, baza.email)

 
