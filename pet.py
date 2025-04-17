class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # TODO
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} eats and feels better!")
    
    def sleep(self):
        # TODO
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} had a good sleep!")
    
    def play(self):
        # TODO
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} plays happily!")
        else:
            print(f"{self.name} is too tired to play.")
    
    def train(self, trick):
        # TODO
          if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
          else:
              print(f"{self.name} already knows the trick '{trick}'.")
    
    def show_tricks(self):
        # TODO
         if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
         else:
             print(f"{self.name} hasn't learned any tricks yet.")
    def get_status(self):
        # TODO
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")