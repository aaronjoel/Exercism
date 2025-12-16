class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = self._validate_time(hour, minute)

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute+minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute-minutes)
    
    def _validate_time(self, hour, minute):
        hr_in_mins = minute // 60
        rem_mins = minute % 60
        tot_hour = (hr_in_mins + hour) % 24
        return (tot_hour, rem_mins)
    

    
    
        