from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class FormData:
    ## Variables
    day_name: str
    time_spent: str 
    start_time: str 
    impact_on_learning: str
    ## Constants
    activity_start_date: datetime = datetime(2024, 2, 6)
    activity_end_date: datetime = datetime(2024, 5, 3)
    activity_type: str = "Traditional face-to-face session"
    course: str = "Aerospace Software Development Engineer (ST0013, V1.0)"
    unit: str = "Knowledge"
    otj: str = "Off the job"

        
    ## Take a start date and add 14 days (+= timedelta(days=14)) until we exceed the end date
    def generate_dates(self):
        
        self.dates = []
        ## Find the correct day
        current_date = self.activity_start_date
        while current_date.strftime("%A") != self.day_name:
            current_date += timedelta(days=1)
        ## Gather all instances of that day's dates 
        while current_date < self.activity_end_date:
            self.dates.append(current_date)
            current_date += timedelta(days=14)
            
        print(f'\nNumber of this day: {len(self.dates)}\n\n')
        print(f'\nAll dates for this day: {self.dates}\n\n')
        
        return self.dates