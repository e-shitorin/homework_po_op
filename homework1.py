class Animals:
    def __init__(self, name, age, weight, habitat, diet):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be of type str")
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError("Age must be of type int")
        if isinstance(weight, (int, float)):
            self.weight = weight
        else:
            raise ValueError("Weight must be of type int or float")
        if isinstance(habitat, str):
            self.habitat = habitat
        else:
            raise ValueError("Habitat must be of type str")
        if isinstance(diet, str):
            self.diet = diet
        else:
            raise ValueError("Diet must be of type str")

    def eat(self):
        return f"{self.name} is eating {self.diet}"

    def sleep(self):
        return f"{self.name} is sleeping in {self.habitat}"

    def make_sound(self, sound):
        return f"{self.name} makes {sound} sound"

    def move(self):
        return f"{self.name} is moving in {self.habitat}"

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Weight: {self.weight}\n"
                f"Habitat: {self.habitat}\n"
                f"Diet: {self.diet}")


class Reptiles(Animals):
    def __init__(self, name, age, weight, habitat, diet,
                 length, venomous, scales_type, color,
                 tail_length, shell_size, speed, life_span):
        super().__init__(name, age, weight, habitat, diet)
        if isinstance(length, float):
            self.length = length
        else:
            raise ValueError("Length must be of type float")
        if isinstance(venomous, bool):
            self.venomous = venomous
        else:
            raise ValueError("Venomous must be of type bool")
        if isinstance(scales_type, str):
            self.scales_type = scales_type
        else:
            raise ValueError("Scales type must be of type str")
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Color must be of type str")
        if isinstance(tail_length, float):
            self.tail_length = tail_length
        else:
            raise ValueError("Tail length must be of type float")
        if isinstance(shell_size, float):
            self.shell_size = shell_size
        else:
            raise ValueError("Shell size must be of type float")
        if isinstance(speed, float):
            self.speed = speed
        else:
            raise ValueError("Speed must be of type float")
        if isinstance(life_span, int):
            self.life_span = life_span
        else:
            raise ValueError("Life span must be of type int")

    def crawl(self, is_crawling: bool) -> str:
        state = "ползет" if is_crawling else "не ползет"
        return f"Рептилия {state}."

    def shed_skin(self, is_shedding: bool) -> str:
        state = "сбрасывает кожу" if is_shedding else "не сбрасывает кожу"
        return f"Рептилия {state}."

    def bask_in_sun(self, is_basking: bool) -> str:
        state = "греется на солнце" if is_basking else "не греется на солнце"
        return f"Рептилия {state}."

    def lay_eggs(self, is_laying: bool) -> str:
        state = "откладывает яйца" if is_laying else "не откладывает яйца"
        return f"Рептилия {state}."

    def __str__(self):
        return super().__str__() + (f'Length: {self.length}\n'
                                    f'Venomous: {self.venomous}\n'
                                    f'Scales type: {self.scales_type}\n'
                                    f'Color: {self.color}\n'
                                    f'Tail length: {self.tail_length}\n'
                                    f'Shell size: {self.shell_size}\n'
                                    f'Speed: {self.speed}\n'
                                    f'Life span: {self.life_span}')

class Mammals(Animals):
    def __init__(self, name, age, weight, habitat, diet,
                 mane_size, strength, pride_size, trunk_length,
                 tusk_size, pouch_size, speed, jump_height):
        super().__init__(name, age, weight, habitat, diet)
        if isinstance(mane_size, float):
            self.mane_size = mane_size
        else:
            raise ValueError("Mane size must be of type float")
        if isinstance(strength, int):
            self.strength = strength
        else:
            raise ValueError("Strength must be of type int")
        if isinstance(pride_size, int):
            self.pride_size = pride_size
        else:
            raise ValueError("Pride size must be of type int")
        if isinstance(trunk_length, float):
            self.trunk_length = trunk_length
        else:
            raise ValueError("Trunk length must be of type float")
        if isinstance(tusk_size, float):
            self.tusk_size = tusk_size
        else:
            raise ValueError("Tusk size must be of type float")
        if isinstance(jump_height, float):
            self.jump_height = jump_height
        else:
            raise ValueError("Jump height must be of type float")
        if isinstance(pouch_size, float):
            self.pouch_size = pouch_size
        else:
            raise ValueError("Pouch size must be of type float")
        if isinstance(speed, float):
            self.speed = speed
        else:
            raise ValueError("Speed must be of type float")

    def run(self, is_running: bool) -> str:
        state = "бежит" if is_running else "не бежит"
        return f"Млекопитающее {state}."

    def hunt(self, is_hunting: bool) -> str:
        state = "охотится" if is_hunting else "не охотится"
        return f"Млекопитающее {state}."

    def nurture_young(self, is_nurturing: bool) -> str:
        state = "воспитывает потомство" if is_nurturing else "не воспитывает потомство"
        return f"Млекопитающее {state}."

    def communicate(self, is_communicating: bool) -> str:
        state = "общается с другими" if is_communicating else "не общается с другими"
        return f"Млекопитающее {state}."

    def __str__(self):
        return super().__str__() + (f'Mane size: {self.mane_size}\n'
                                    f'Strength: {self.strength}\n'
                                    f'Pride size: {self.pride_size}\n'
                                    f'Trunk length: {self.trunk_length}\n'
                                    f'Tusk size: {self.tusk_size}\n'
                                    f'Speed: {self.speed}\n'
                                    f'Jump height: {self.jump_height}\n'
                                    f'Pouch size: {self.pouch_size}')

class ZooShow:
    def __init__(self, show_name: str, ticket_price: float, animal_performer):
        if isinstance(show_name, str):
            self.show_name = show_name
        else:
            raise ValueError("Show name must be of type str")
        if isinstance(ticket_price, (int, float)):
            self.ticket_price = ticket_price
        else:
            raise ValueError("Ticket price must be of type float")
        if isinstance(animal_performer, (Reptiles, Mammals)):
            self.animal_performer = animal_performer
        else:
            raise ValueError("Animal performer must be an instance of Reptiles or Mammals")
        self.tickets_sold = 0

    def perform_show(self):
        return f"{self.animal_performer.name} выполняет трюк"
    def display_info(self):
        return (f"Show Name: {self.show_name}\n"
                f"Ticket Price: {self.ticket_price}\n"
                f"Animal Performer: {self.animal_performer.name}\n"
                f"Animal Details:\n{self.animal_performer}")

    def sell_ticket(self, quantity: int):
        if isinstance(quantity, int) and quantity > 0:
            self.tickets_sold += quantity
            return self.tickets_sold
        else:
            raise ValueError("Количество должно быть положительным целым числом")

    def calculate_revenue(self):
        return self.tickets_sold * self.ticket_price

snake = Reptiles(name='Змея', age=3, weight=2.5, habitat='лес',
                     diet='мясо', length=3.3, venomous=True, scales_type='гладкая',
                     color='...', tail_length=0.0, shell_size=0.0,
                     speed=0.0, life_span=0)
lizard = Reptiles(name='Ящерица', age=2, weight=1.3, habitat='джунгли',
                      diet='всеядная', length=0.0, venomous=False, scales_type='...',
                      color='зелёный', tail_length=0.2, shell_size=0.0, speed=0.0, life_span=0)
turtle = Reptiles(name='Черепаха', age=2, weight=1.3, habitat='океан',
                      diet='всеядная', length=0.0, venomous=False, scales_type='...',
                      color='...', tail_length=0.0, shell_size=1.0, speed=0.2, life_span=100)

lion = Mammals(name='Лев', age=3, weight=150, habitat='саванна',
                   diet='мясо', mane_size=1.70, strength=100, pride_size=8, trunk_length=0.0,
                   tusk_size=0.0, speed=0.0, pouch_size=0.0, jump_height=0.0)
elephant = Mammals(name='Слон', age=7, weight=380, habitat='саванна',
                       diet='трава', mane_size=0.0, strength=0, pride_size=0, trunk_length=1.5,
                       tusk_size=1.2, speed=0.0, pouch_size=0.0, jump_height=0.0)
kangaroo = Mammals(name='Кенгуру', age=6, weight=180, habitat='саванна',
                       diet='клевер', mane_size=0.0, strength=0, pride_size=0, trunk_length=0.0,
                       tusk_size=0.0, speed=6.3, pouch_size=12.0, jump_height=2.0)

zoo_show = ZooShow(show_name='Змеиное шоу', ticket_price=250, animal_performer=snake)
print(zoo_show.display_info())
print(zoo_show.perform_show())
zoo_show.sell_ticket(10)
print(f"Доход: {zoo_show.calculate_revenue()} сом")