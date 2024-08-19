class AdultException(Exception):
    pass

class person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age


    def get_minor_age(self):
        age=self.age
        if age<18:
            raise AdultException
        else:
            return age
        
    def display_person(self):
        try:
            print(self.get_minor_age())
        except AdultException:
            print('person is an adult')
        finally:
            print(self.name)




p=person('vinod',22)
c=person('vino',15)

p.display_person() 
c.display_person()       