
from driver import Driver
from duty import Duty
from admin import Admin
from driver_calendar import Calendar  # Renamed from calendar.py to avoid conflict with stdlib calendar
from auth import Auth
from database import init_db, add_driver, add_duty, get_all_drivers

def driver_menu(driver, calendar_system):
    """
    Display and handle the driver-specific menu.
    """
    while True:
        print("\n--- Driver Menu ---")
        print("1. View Profile")
        print("2. Add Duty")
        print("3. View Weekly Layout")
        print("4. Edit Profile")
        print("5. View Duty Details")
        print("6. Logout")
        choice = input("Select an option: ")
        
        if choice == "1":
            print("\nDriver Profile:")
            print(f"Driver Number: {driver.driver_number}")
            print(f"Name: {driver.name}")
            print(f"Email: {driver.email}")
            print(f"Phone: {driver.phone}")
        elif choice == "2":
            day = input("Enter the day to add duty (e.g., Monday): ")
            duty_number = input("Enter duty number: ")
            driver.add_duty(day, duty_number)
        elif choice == "3":
            calendar_system.display_weekly_layout(driver)
        elif choice == "4":
            name = input("Enter new name (or press Enter to keep current): ")
            email = input("Enter new email (or press Enter to keep current): ")
            phone = input("Enter new phone (or press Enter to keep current): ")
            driver.edit_profile(name if name else None,
                                email if email else None,
                                phone if phone else None)
        elif choice == "5":
            day = input("Enter the day to view duty details (e.g., Monday): ")
            calendar_system.view_duty_details(driver, day)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def admin_menu(admin_user):
    """
    Display and handle the admin-specific menu.
    """
    while True:
        print("\n--- Admin Panel ---")
        print("1. View All Duties")
        print("2. Add New Duty")
        print("3. Edit Duty Info")
        print("4. View Driver Info")
        print("5. Logout Admin Panel")
        choice = input("Select an option: ")
        
        if choice == "1":
            admin_user.view_all_duties()
        elif choice == "2":
            print("\nEnter details for the new duty:")
            duty_id = input("Duty ID: ")
            roster = input("Roster (e.g., HZ2/03): ")
            route = input("Initial Route (before break): ")
            report_time = input("Report Time (HH:MM): ")
            depart_time = input("Departure Time (HH:MM): ")
            start_location = input("Start Location: ")
            start_of_break = input("Start of Break (HH:MM): ")
            break_location = input("Break Location (where break starts): ")
            resume_time = input("Resume Time (HH:MM) [when duty resumes after break]: ")
            post_break_location = input("Post-Break Location: ")
            post_break_route = input("Post-Break Route: ")
            finish_time = input("Finish Time (HH:MM): ")
            finish_location = input("Finish Location: ")
            sign_off_time = input("Sign Off Time (HH:MM): ")
            rota = input("Rota info: ")
            new_duty = Duty(
                duty_id, roster, route, report_time, depart_time,
                start_location, start_of_break, break_location,
                resume_time, post_break_location, post_break_route,
                finish_time, finish_location, sign_off_time, rota
            )
            admin_user.add_duty_info(new_duty)
            add_duty(new_duty)  # Save the new duty to the database.
        elif choice == "3":
            duty_id = input("Enter the duty ID to edit: ")
            new_route = input("Enter the new route: ")
            admin_user.edit_duty_info(duty_id, route=new_route)
        elif choice == "4":
            driver_number = input("Enter driver number to view info: ")
            admin_user.view_driver_info(driver_number)
        elif choice == "5":
            print("Exiting Admin Panel.")
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    """
    Main menu for the DriveMate app. Allows login, registration,
    password reset, and admin panel access.
    """
    init_db()  # Initialize the database and create tables if they don't exist.
    auth_system = Auth()
    calendar_system = Calendar()
    admin_user = Admin(admin_id="A001", name="Admin User", email="admin@drivemate.com")
    
    # Populate drivers from the database.
    drivers_from_db = get_all_drivers()
    for row in drivers_from_db:
        driver = Driver.from_db_row(row)
        auth_system.registered_drivers[driver.driver_number] = driver
        admin_user.drivers[driver.driver_number] = driver

    while True:
        print("\n--- DriveMate App ---")
        print("1. Login")
        print("2. Register")
        print("3. Password Reset")
        print("4. Admin Panel")
        print("5. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            identifier = input("Enter driver number or email: ")
            password = input("Enter password: ")
            driver = auth_system.login(identifier, password)
            if driver:
                driver_menu(driver, calendar_system)
        elif choice == "2":
            driver_number = input("Enter a 6-digit driver number: ")
            name = input("Enter your full name: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number: ")
            password = input("Enter a password: ")
            new_driver = Driver(driver_number, name, email, phone, password)
            auth_system.register(new_driver)
            add_driver(new_driver)  # Save new driver to the database.
            admin_user.drivers[new_driver.driver_number] = new_driver  # Add to admin's in-memory records.
        elif choice == "3":
            contact = input("Enter your email or phone for password reset: ")
            auth_system.password_reset(contact)
        elif choice == "4":
            admin_identifier = input("Enter admin email: ")
            if admin_identifier == admin_user.email:
                print("Welcome to the Admin Panel!")
                admin_menu(admin_user)
            else:
                print("Invalid admin credentials.")
        elif choice == "5":
            print("Exiting DriveMate. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
