
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('drivemate.db')
    conn.row_factory = sqlite3.Row  # Allow accessing columns by name.
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drivers (
            driver_number TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS duties (
            duty_id TEXT PRIMARY KEY,
            roster TEXT,
            route TEXT,
            report_time TEXT,
            depart_time TEXT,
            start_location TEXT,
            start_of_break TEXT,
            break_location TEXT,
            resume_time TEXT,
            post_break_location TEXT,
            post_break_route TEXT,
            finish_time TEXT,
            finish_location TEXT,
            sign_off_time TEXT,
            rota TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_driver(driver):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO drivers (driver_number, name, email, phone, password)
        VALUES (?, ?, ?, ?, ?)
    ''', (driver.driver_number, driver.name, driver.email, driver.phone, driver.password.decode('utf-8')))
    conn.commit()
    conn.close()

def add_duty(duty):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO duties (duty_id, roster, route, report_time, depart_time, start_location,
            start_of_break, break_location, resume_time, post_break_location, post_break_route,
            finish_time, finish_location, sign_off_time, rota)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        duty.duty_id,
        duty.roster,
        duty.route,
        duty.report_time.strftime('%H:%M'),
        duty.depart_time.strftime('%H:%M'),
        duty.start_location,
        duty.start_of_break.strftime('%H:%M'),
        duty.break_location,
        duty.resume_time.strftime('%H:%M'),
        duty.post_break_location,
        duty.post_break_route,
        duty.finish_time.strftime('%H:%M'),
        duty.finish_location,
        duty.sign_off_time.strftime('%H:%M'),
        duty.rota
    ))
    conn.commit()
    conn.close()

def get_all_drivers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drivers')
    drivers = cursor.fetchall()
    conn.close()
    return drivers
