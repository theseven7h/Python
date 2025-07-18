class TimeWithProperties:
    def __init__(self, hour=0, minute=0, second=0):
        self.__validate_time(hour, minute, second)
        self._hour = hour
        self._minute = minute
        self._second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, new_hour):
        self.__validate_minute(new_hour)
        self._hour = new_hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, new_minute):
        self.__validate_minute(new_minute)
        self._minute = new_minute

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, new_second):
        self.__validate_second(new_second)
        self._second = new_second

    @staticmethod
    def __validate_second(second):
        if second < 0 or second > 59:
            raise (ValueError('Second must be between 0 and 59'))

    @staticmethod
    def __validate_minute(minute):
        if minute < 0 or minute > 59:
            raise ValueError('Minute must be between 0 and 59')

    @staticmethod
    def __validate_hour(hour):
        if hour < 0 or hour > 23:
            raise ValueError('Hour must be between 0 and 23')

    @staticmethod
    def __validate_time(new_hour, new_minute, new_second):
        TimeWithProperties.__validate_hour(new_hour)
        TimeWithProperties.__validate_minute(new_minute)
        TimeWithProperties.__validate_second(new_second)

    def __str__(self):
        return f'{self._hour:02}:{self._minute:02}:{self._second:02}'


# print("Second is",time1.second)
time1 = TimeWithProperties(0,0,88)
print(time1)
try:
    time1.second = 65
except ValueError as e:
    print(e)

print(time1)