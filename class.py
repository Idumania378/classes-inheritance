# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, camera_megapixels):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def make_call(self, number):
        print(f"Calling {number}... 📞")

    def take_picture(self):
        print(f"Taking a picture with {self.camera_megapixels} MP camera! 📸")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"


# Subclass: SmartPhone with a custom method for gaming
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels, has_joystick):
        super().__init__(brand, model, storage, camera_megapixels)
        self.has_joystick = has_joystick

    def play_game(self, game_name):
        if self.has_joystick:
            print(f"Playing {game_name} with joystick control! 🎮")
        else:
            print(f"Playing {game_name} using touchscreen controls. 📱")


# Subclass: CameraSmartphone with a custom method for photography
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels, lens_quality):
        super().__init__(brand, model, storage, camera_megapixels)
        self.lens_quality = lens_quality

    def take_professional_picture(self):
        print(f"Taking a professional picture with {self.lens_quality} lens quality! 📸")


# Create instances of the different smartphone types
basic_phone = Smartphone("GenericBrand", "X100", 64, 12)
gaming_phone = GamingSmartphone("GamerTech", "GTX200", 128, 16, True)
camera_phone = CameraSmartphone("PhotoPro", "P1000", 256, 48, "Ultra HD")

# Test polymorphism
print(basic_phone)
basic_phone.make_call("0114602603")
basic_phone.take_picture()

print(gaming_phone)
gaming_phone.play_game("Fortnite")
gaming_phone.make_call("0724138831")

print(camera_phone)
camera_phone.take_professional_picture()
camera_phone.take_picture()
