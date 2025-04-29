

class Auth:
    def __init__(self):
        # Dictionary to store registered drivers, keyed by driver_number.
        self.registered_drivers = {}

    def register(self, driver):
      
        if driver.driver_number in self.registered_drivers:
            print("Driver already registered.")
        else:
            self.registered_drivers[driver.driver_number] = driver
            print("Registration successful.")

    def login(self, identifier, password):
       
        for driver in self.registered_drivers.values():
            if str(driver.driver_number) == str(identifier) or driver.email == identifier:
                if driver.check_password(password):
                    print("Login successful!")
                    # Return the driver object as a session token (for now, just the driver object)
                    return driver
                else:
                    print("Incorrect password.")
                    return None
        print("Driver not found.")
        return None

    def password_reset(self, contact):
        
        print(f"Password reset instructions sent to {contact}.")
