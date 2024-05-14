class Vehicle:
    
    def __init__(self, wheel_size, wheel_number):
        """
        Initialize a Vehicle with a wheel size and number.

        Args:
            wheel_size (int): The size of the vehicle's wheels.
            wheel_number (int): The number of wheels the vehicle has.
        """
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"

