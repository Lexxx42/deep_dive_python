"""
Создайте класс-фабрику.

1. Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.

2. Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        pass


class Fish(Animal):
    def __init__(self, name: str, water_type: str):
        super().__init__(name=name)
        self.water_type = water_type

    def swim(self) -> str:
        return f"{self.name} is swimming in {self.water_type} water."


class Bird(Animal):
    def __init__(self, name: str, wingspan: str):
        super().__init__(name=name)
        self.wingspan = wingspan

    def fly(self) -> str:
        return f"{self.name} has a wingspan of {self.wingspan} centimeters and can fly."


class Mammal(Animal):
    def __init__(self, name: str, fur_color: str):
        super().__init__(name=name)
        self.fur_color = fur_color

    def run(self) -> str:
        return f"{self.name} with {self.fur_color} fur can run on land."


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, name: str, **kwargs) -> Fish | Bird | Mammal:
        animal_type = animal_type.lower()

        if animal_type == "fish":
            water_type = kwargs.get("water_type", "unknown")
            return Fish(name=name, water_type=water_type)

        elif animal_type == "bird":
            wingspan = kwargs.get("wingspan", 0)
            return Bird(name=name, wingspan=wingspan)

        elif animal_type == "mammal":
            fur_color = kwargs.get("fur_color", "unknown")
            return Mammal(name=name, fur_color=fur_color)

        else:
            raise ValueError("Invalid animal type")


# Example usage of the AnimalFactory
factory = AnimalFactory()

# Create instances of different animals using the factory
nemo = factory.create_animal(animal_type="Fish", name="Nemo", water_type="ocean")
eagle = factory.create_animal(animal_type="Bird", name="Eagle", wingspan=72)
lion = factory.create_animal(animal_type="Mammal", name="Lion", fur_color="golden")

print(nemo.swim())  # "Nemo is swimming in ocean water."
print(eagle.fly())  # "Eagle has a wingspan of 72 centimeters and can fly."
print(lion.run())  # "Lion with golden fur can run on land."
