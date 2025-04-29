
from datetime import datetime

class Duty:
    def __init__(self, duty_id, roster, route, report_time, depart_time, start_location,
                 start_of_break, break_location, resume_time, post_break_location, post_break_route,
                 finish_time, finish_location, sign_off_time, rota):
        """
        Initialize a new Duty with the required attributes.
        Time strings are converted to datetime objects (using a common dummy date).
        Durations are calculated as float hours.
        
        New fields:
          - break_location: where the break starts
          - resume_time: when duty resumes after the break (i.e. start after break)
          - post_break_location: the location after break where work resumes
          - post_break_route: the route after break (if different)
        """
        self.duty_id = duty_id            
        self.roster = roster              
        self.route = route  # Initial route before break
        
        common_date = "2023-01-01"
        self.report_time = datetime.strptime(f"{common_date} {report_time}", "%Y-%m-%d %H:%M")
        self.depart_time = datetime.strptime(f"{common_date} {depart_time}", "%Y-%m-%d %H:%M")
        self.start_location = start_location
        
        self.start_of_break = datetime.strptime(f"{common_date} {start_of_break}", "%Y-%m-%d %H:%M")
        self.break_location = break_location  # Where break begins
        
        self.resume_time = datetime.strptime(f"{common_date} {resume_time}", "%Y-%m-%d %H:%M")
        self.post_break_location = post_break_location
        self.post_break_route = post_break_route  # Route after break
        
        self.finish_time = datetime.strptime(f"{common_date} {finish_time}", "%Y-%m-%d %H:%M")
        self.finish_location = finish_location
        self.sign_off_time = datetime.strptime(f"{common_date} {sign_off_time}", "%Y-%m-%d %H:%M")
        self.rota = rota
        
        # Calculate durations:
        self.total_time_on_duty = (self.finish_time - self.report_time).total_seconds() / 3600
        # Break duration calculated as time from start_of_break to resume_time
        self.break_duration = (self.resume_time - self.start_of_break).total_seconds() / 3600
        self.driving_time = self.total_time_on_duty - self.break_duration
        
        # For clarity, map to your desired terms:
        self.spread = self.total_time_on_duty   # Total duty time
        self.work = self.driving_time           # Driving time (work)
        self.relief = self.break_duration       # Break duration (relief)

    @staticmethod
    def format_duration(hours):
        """
        Convert a float (hours) to an HH:MM formatted string.
        """
        total_minutes = int(round(hours * 60))
        hh = total_minutes // 60
        mm = total_minutes % 60
        return f"{hh:02d}:{mm:02d}"

    def detailed_view(self):
        """
        Display detailed information about the duty.
        """
        print(f"Duty ID: {self.duty_id}")
        print(f"Roster: {self.roster}")
        print(f"Initial Route (before break): {self.route}")
        print(f"Report Time: {self.report_time.strftime('%H:%M')}")
        print(f"Departure Time: {self.depart_time.strftime('%H:%M')}")
        print(f"Start Location: {self.start_location}")
        print(f"Start of Break: {self.start_of_break.strftime('%H:%M')}")
        print(f"Break Location: {self.break_location}")
        print(f"Resume Time (Start After Break): {self.resume_time.strftime('%H:%M')}")
        print(f"Post-Break Location: {self.post_break_location}")
        print(f"Post-Break Route: {self.post_break_route}")
        print(f"Finish Time: {self.finish_time.strftime('%H:%M')}")
        print(f"Finish Location: {self.finish_location}")
        print(f"Sign Off Time: {self.sign_off_time.strftime('%H:%M')}")
        print(f"Spread (Total Duty Time): {self.format_duration(self.spread)}")
        print(f"Work (Driving Time): {self.format_duration(self.work)}")
        print(f"Relief (Break Duration): {self.format_duration(self.relief)}")
        print(f"Rota: {self.rota}")

    def summary_view(self):
        """
        Display a brief summary of the duty.
        """
        print(f"Duty ID: {self.duty_id} | Initial Route: {self.route} | Report: {self.report_time.strftime('%H:%M')} | Depart: {self.depart_time.strftime('%H:%M')}")
