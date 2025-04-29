
import bcrypt  # type: ignore

class Driver:
    def __init__(self, driver_number, name, email, phone, password):
        self.driver_number = driver_number  # 6-digit unique identifier, e.g., "941174"
        self.name = name                    # Full name of the driver
        self.email = email                  # Contact email
        self.phone = phone                  # Contact phone number
        self.weekly_layout = {              # Initialize weekly layout for duties
            "Monday": None,
            "Tuesday": None,
            "Wednesday": None,
            "Thursday": None,
            "Friday": None,
            "Saturday": None,
            "Sunday": None
        }
        # Hash the password (if not already hashed)
        self.password = self.hash_password(password)

    def hash_password(self, plain_text_password):
        return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    
    def check_password(self, plain_text_password):
        return bcrypt.checkpw(plain_text_password.encode('utf-8'), self.password)
    
    def add_duty(self, day, duty_number):
        if day in self.weekly_layout:
            self.weekly_layout[day] = duty_number
            print(f"Duty {duty_number} added for {day}.")
        else:
            print("Invalid day. Please enter a valid day of the week.")
    
    def view_duties(self):
        print("Weekly Duties Layout:")
        for day, duty in self.weekly_layout.items():
            duty_info = duty if duty is not None else "No duty assigned."
            print(f"{day}: {duty_info}")
    
    def edit_profile(self, name=None, email=None, phone=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        print("Profile updated successfully.")
    
    def retrieve_password(self):
        print("Password reset instructions have been sent to your email/phone.")
    
    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.password = self.hash_password(new_password)
            print("Password changed successfully.")
        else:
            print("Old password is incorrect.")
    
    def get_duty_info(self, duty_number):
        print(f"Fetching info for duty {duty_number}...")
        return f"Detailed info for duty {duty_number}."
    
    @classmethod
    def from_db_row(cls, row):
        """
        Create a Driver object from a database row (sqlite3.Row).
        Assumes the stored password is already hashed (stored as string).
        """
        driver = cls(row['driver_number'], row['name'], row['email'], row['phone'], row['password'])
        # Overwrite the password with the stored hash as bytes
        driver.password = row['password'].encode('utf-8')
        return driver
