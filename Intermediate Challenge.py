class Car:

    def __init__(car, weight: int, wheels: int, passengers: int, model_number: int, manufacturer: int):
        car.weight = weight
        car.wheels = wheels
        car.passengers = passengers
        car.model_number = model_number
        car.manufacturer = manufacturer

    def __repr__(car):
        return f"\nThe item has the following attributes: \n" \
               f"Car Weight: {car.weight} \n" \
               f"Car Wheels: {car.wheels} \n" \
               f"Passengers: {car.passengers} \n" \
               f"Model Number: {car.model_number} \n" \
               f"Manufacturer: {car.manufacturer}"


car1 = Car(250, 4, 6, 1312412312, 1241234123124123123123)


print(car1)