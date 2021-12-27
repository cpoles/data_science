class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    @property
    def __calculate_time__(self):
        quot, rem = divmod(self.minute, 60)

        final_hour = (quot + self.hour) % 24
        final_mins = rem
        
        return final_hour, final_mins

    def __repr__(self):
        final_hour, final_mins = self.__calculate_time__
        
        if final_hour < 10:
            hour_str = "0" + str(final_hour)
        else:
            hour_str = str(final_hour)

        if final_mins < 10:
            min_str = "0" + str(final_mins)
        else:
            min_str = str(final_mins)
            
        return f'{hour_str}:{min_str}'
            

    def __eq__(self, other):
        self_hour, self_min = self.__calculate_time__
        other_hour, other_min = other.__calculate_time__

        return self_hour == other_hour and self_min == other_min


    def __add__(self, minutes):
        self.minute = self.minute + minutes
        final_hour, final_minutes = self.__calculate_time__
        self.hour = final_hour
        self.minute = final_minutes        
        return self.__repr__()

    def __sub__(self, minutes):
        self.minute = self.minute - minutes
        final_hour, final_minutes = self.__calculate_time__
        self.hour = final_hour
        self.minute = final_minutes        
        return self.__repr__()