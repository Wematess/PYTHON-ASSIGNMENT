class Smartphone:
    def __init__(self, brand, model, battery_level=50):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"The {self.brand} {self.model} is now on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"The {self.brand} {self.model} is now off.")

    def charge(self, amount):
        if amount > 0:
            self.battery_level += amount
            if self.battery_level > 100:
                self.battery_level = 100
            print(f"The battery is now at {self.battery_level}%.")

    def send_message(self, recipient, message):
        if self.is_on:
            print(f"Message sent to {recipient}: '{message}'")
            self.battery_level -= 2
            if self.battery_level < 0:
                self.battery_level = 0
            print(f"Battery level is now {self.battery_level}%.")
        else:
            print("Cannot send message. The phone is off.")
    
    def get_status(self):
        status = "on" if self.is_on else "off"
        print(f"--- {self.brand} {self.model} Status ---")
        print(f"Power: {status}")
        print(f"Battery: {self.battery_level}%")
        print("----------------------------")


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_level=50, cooling_system_on=False):
        super().__init__(brand, model, battery_level)
        self.cooling_system_on = cooling_system_on

    def play_game(self, game_name, hours):
        if self.is_on:
            print(f"Playing {game_name} for {hours} hours...")
            battery_drain = hours * 5
            if self.cooling_system_on:
                battery_drain -= 5
                print("Cooling system is active, reducing battery drain.")
            
            self.battery_level -= battery_drain
            if self.battery_level < 0:
                self.battery_level = 0
            print(f"Battery level after playing: {self.battery_level}%.")
        else:
            print("Cannot play game. The phone is off.")

    def get_status(self):
        status = "on" if self.is_on else "off"
        cooling_status = "on" if self.cooling_system_on else "off"
        print(f"--- {self.brand} {self.model} Status ---")
        print(f"Power: {status}")
        print(f"Battery: {self.battery_level}%")
        print(f"Cooling System: {cooling_status}")
        print("----------------------------")


my_phone = Smartphone(brand="Google", model="Pixel 7")
my_gaming_phone = GamingSmartphone(brand="ASUS", model="ROG 6", cooling_system_on=True)

my_phone.turn_on()
my_phone.get_status()
my_phone.send_message("Alice", "Hello!")
my_phone.charge(20)

print("\n--- Testing Gaming Smartphone ---")
my_gaming_phone.turn_on()
my_gaming_phone.get_status()
my_gaming_phone.play_game("Fortnite", 2)
my_gaming_phone.get_status()

print("\n--- Demonstrating Polymorphism ---")
phones = [my_phone, my_gaming_phone]

for phone in phones:
    phone.get_status()
