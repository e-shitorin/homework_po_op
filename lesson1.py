class Person:
    def __init__(self, name, age, gender, height, hobby):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be of type str")
        if isinstance(age, int):
            self.age  = age
        else:
            raise ValueError("Age must be of type int")
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError("Gender must be of type str")
        if  isinstance(height, float):
            self.height = height
        else:
            raise ValueError("Height must be of type float")
        if isinstance(hobby, bool):
            self.hobby = hobby
        else:
            raise ValueError("Hobby must be of type bool")

    def buy_energy_drink(self):
        if self.age >= 18:
            return("You can buy an energy drink", self.name)
        else:
            return("You can't buy an energy drink", self.name)

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n" 
                f"Gender: {self.gender}\n"
                f"Height: {self.height}\n"
                f"Hobby: {self.hobby}")
    
human_1 = Person(name = 'Vera', age = 16, gender = 'female',
                height = 1.67, hobby = True)
human_2 = Person(name = 'Joe', age = 22, gender = 'male',
                height = 1.85, hobby = False)
    
print(human_1)
print('-' * 10)
print(human_2)
print('-' * 10)
print(human_1.buy_energy_drink())
print(human_2.buy_energy_drink())