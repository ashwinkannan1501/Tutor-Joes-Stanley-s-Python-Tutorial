def classes_and_objects():
    class Car:
        color = "red"
        engine_cc = 6000
        price = 1000000

        def start(self):
            print("The car is started")

        def accelerate(self):
            print("The car is accelerated perfectly")

        def gear_shift(self):
            print("The car is shifting its gear perfectly")

        def brake(self):
            print("The brake pedal is working properly")

        def stop(self):
            print("The car is stopped")

    swift = Car()

    # Accessing the attributes from the 'Car' class
    print("Color : ", swift.color)
    print("Engine CC : ", swift.engine_cc)
    print("Price (Rs) : ", swift.price)

    # Accessing the methods from the "Car" class.
    swift.start()
    swift.accelerate()
    swift.gear_shift()
    swift.brake()
    swift.stop()

    print("'swift' is the instance (or) object of 'Car' class ? : ", isinstance(swift, Car))
    print("The data type of class 'Car' is : ", type(Car))
    print("The data type of object 'swift' is : ", type(swift))


if __name__ == "__main__":
    classes_and_objects()
