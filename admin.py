
class Admin:
    def __init__(self, admin_id, name, email):
        self.admin_id = admin_id
        self.name = name
        self.email = email
        # In-memory storage for duty templates and drivers
        self.duties = {}   # Key: duty_id, Value: Duty object
        self.drivers = {}  # Key: driver_number, Value: Driver object

    def add_duty_info(self, duty):
        self.duties[duty.duty_id] = duty
        print(f"Duty {duty.duty_id} added successfully.")

    def edit_duty_info(self, duty_id, **kwargs):
        if duty_id in self.duties:
            duty = self.duties[duty_id]
            for key, value in kwargs.items():
                if hasattr(duty, key):
                    setattr(duty, key, value)
                    print(f"Updated {key} for Duty {duty_id}.")
                else:
                    print(f"Duty has no attribute '{key}'.")
        else:
            print(f"No duty found with ID {duty_id}.")

    def view_all_duties(self):
        print("All Duties:")
        for duty in self.duties.values():
            duty.summary_view()

    def assign_duty(self, driver_number, duty_id):
        if driver_number in self.drivers and duty_id in self.duties:
            driver = self.drivers[driver_number]
            driver.add_duty("Assigned Day", duty_id)
            print(f"Duty {duty_id} assigned to driver {driver_number}.")
        else:
            print("Invalid driver number or duty ID.")

    def view_driver_info(self, driver_number):
        if driver_number in self.drivers:
            driver = self.drivers[driver_number]
            print(f"Driver Number: {driver.driver_number}")
            print(f"Name: {driver.name}")
            print("Weekly Duties:")
            driver.view_duties()
        else:
            print("Driver not found.")
