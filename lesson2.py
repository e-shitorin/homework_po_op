class Car:
    def  __init__(self, model, color, volume):
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError("Model must be a string")
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Color must be a string")
        if isinstance(volume, float):
            self.volume = volume
        else:
            raise ValueError("Volume must be a float")

    def drive(self, speed):
        return f'This car drives {speed} km/h'

    def __str__(self):
        return (f"Model: {self.model}\n"
                f"Color: {self.color}\n" 
                f"Volume: {self.volume}\n")
    
print('Простые машины')
print('-' * 10)
car_1 = Car(model = 'Ford', color = 'blue',  volume = 2.5)
car_2 = Car(model = 'Lexus', color = 'black',  volume = 4.5)
print(f'{car_1}\n'
      f'----------\n'
      f'{car_2}')
print('-' * 10)
print(car_1.drive(200))
print(car_2.drive(500))

class HybridCar(Car):
    def __init__(self, model, color, volume, battery, comfort):
        super().__init__(model, color, volume)
        if isinstance(battery, float):
            self.battery = battery
        else:
            raise ValueError('Battery must be of type float')
        if isinstance(comfort, bool):
            self.comfort = comfort
        else:
            raise ValueError('Comfort must be of type bool')
        
    def call(self):
        return f'Hybrid car {self.model} is calling you'

    def __str__(self):
        return super().__str__()+(f'\n Battery {self.battery}\n'
                                  f'Comfort {self.comfort}')
    
hybrid_1 = HybridCar(model="Toyota Prius", color='black', volume=1.5, battery = 72.5, comfort = False)
hybrid_2 = HybridCar(model="Honda Civic", color='white', volume=1.8,  battery = 60.5, comfort = True)
print(f'----------\n'
      f'{hybrid_1}\n'
      f'{hybrid_2}')
print(hybrid_1.drive(600))
print(hybrid_2.drive(700))
print(hybrid_1.call())
print(hybrid_2.call())