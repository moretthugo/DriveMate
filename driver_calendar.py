
class Calendar:
    def __init__(self):
        # This class is stateless; it simply provides methods to interact with the driver's weekly layout.
        pass

    def display_weekly_layout(self, driver):
        
        print(f"Weekly Layout for {driver.name}:")
        for day, duty in driver.weekly_layout.items():
            if duty is None:
                print(f"{day}: No duty assigned")
            else:
                print(f"{day}: Duty {duty}")

    def add_duty_to_calendar(self, driver, day, duty_id):
        """
        Add or update a duty in the driver's weekly layout.
        """
        driver.add_duty(day, duty_id)

    def view_duty_details(self, driver, day):
   
        if day in driver.weekly_layout:
            duty = driver.weekly_layout[day]
            if duty is None:
                print(f"No duty assigned for {day}.")
            else:
                # Assuming driver.get_duty_info returns a string with duty details.
                details = driver.get_duty_info(duty)
                print(f"Duty details for {day}: {details}")
        else:
            print("Invalid day.")
