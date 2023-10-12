class DateError(Exception):
    pass

class DateString:
    def __init__(self, date):
        self.day, self.month, self.year = self.is_valid_date(date)


    def is_valid_date(self, date):
        day, month, year = list(map(int, date.split('.')))
        if not 1 <= day <= 31:
            raise DateError
        if not 1 <= month <= 12:
            raise DateError
        if not 1 <= year <= 3000:
            raise DateError
        return day, month, year

    def __str__(self):
        day = str(self.day).zfill(2)
        month = str(self.month).zfill(2)
        year = str(self.year).zfill(4)
        return '.'.join([day, month, year])


date_string = input()

date = DateString(date_string)
print(date)