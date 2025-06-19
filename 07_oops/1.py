
# Encapsulation ==> make a variable private
# any variable can be made private by :
#  variable ==> __variable
# eg make brand private
#  a private varibale can only be acces in the class only ,
#  any object made from this class can't acces this variable

class Car:

    #class variables
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    #getter function
    def get_brand(self):
        return self.__brand + " !"
    #setter function
    def set_brand(self, new_brand):
        self.__brand = new_brand
    
    #polymorphism
    def fuel_type(self):
        return "Petrol or diesel"
    
    # static methods: remove self
    # only classes have access
    @staticmethod
    def general_desc():
        return "Car are means of transport"

    #prevents over writing
    @property
    def model(self):
        return self.__model
    

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "ELectric Charge"
    


# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("tata", "safari")
# result = my_new_car.full_name()
# print(result)


my_elec_car = ElectricCar("Tesla","CyberTruck","85kWh")
# print(my_elec_car.__brand)
# print(my_elec_car.get_brand())
# print(my_elec_car.model)
# print(my_elec_car.battery_size)
# print(my_elec_car.full_name())

my_elec_car.set_brand("BYD")
# print(my_elec_car.get_brand())


one_more_car = Car("BMW", "GTR")

# one_more_car.model = "City"
# print(one_more_car.full_name())
#  now making model as read only:
# print(one_more_car.model)



# print(one_more_car.fuel_type())
# print(my_elec_car.fuel_type())

# print(Car.total_car)

# print(my_elec_car.general_desc())
# print(Car.general_desc())


# print(isinstance(my_elec_car, ElectricCar))


# multiple inheritance
class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class EvCar(Battery, Engine, Car):
    pass

tesla = EvCar("Tesla", "Model S")
print(tesla.battery_info())
print(tesla.engine_info())