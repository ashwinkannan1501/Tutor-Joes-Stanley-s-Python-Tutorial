# datetime module

# Import the 'datetime' module
import datetime
import time

print("----------------------------- Date Class ----------------------------\n")
# Example 1 :- Date object representing date in python
date = datetime.date(2022, 12, 15)
print("Date Constructor :- ", date)
# print("Date Constructor :- ", datetime.date(2020, 30, 15))
# print("Date Constructor :- ", datetime.date("2020", 12, 15))

# Example 2 :- Get Current Date
print("Current date : ", datetime.date.today())

# Example 3 :- Get Today's day, month and year
print("Current day : ", datetime.date.today().day)
print("Current month : ", datetime.date.today().month)
print("Current Year : ", datetime.date.today().year)

# Example 4 :- Get date from timestamp
print("fromtimestamp(timestamp, tz=None) method :- ", datetime.datetime.fromtimestamp(1234567890))

# Example 5 :- Convert the date object to string
today_date = datetime.date.today()
date_to_string = datetime.date.isoformat(today_date)
print('Date to String :- ', date_to_string)
print(type(date_to_string))

# Date class Methods :-
print("datetime.date.ctime() function :- ", datetime.date(2022, 12, 15).ctime())

print("datetime.date.weekday(date) function :- ", datetime.date.weekday(datetime.date.today()))

print("datetime.date.timetuple() function :- ", datetime.date.timetuple(today_date))
print("datetime.date.isoformat() function :- ", datetime.date.isoformat(today_date))
print("datetime.date.stftime(format) function :- ", datetime.date.today().strftime("%d / %m / %Y"))

days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
weekday = datetime.date.isoweekday(
    today_date)  # It returns an integer of the respective day when 1 is 'Monday' and 7 is 'Sunday'
print("datetime.date.isoweekday() (It returns an integer) :- ", days[weekday])

print("datetime.date.isocalendar() function :- ", datetime.date.isocalendar(today_date))
print('datetime.date.fromisocalendar() function :- ', datetime.date.fromisocalendar(today_date.year, 5, 2))

print('datetime.date.replace() function :- ', today_date.replace(year=2020, month=3, day=1))

current_time = time.time()
print('datetime.date.fromtimestamp(timestamp) function :- ', datetime.date.fromtimestamp(current_time))

print('datetime.date.fromisoformat(date_string) function :- ', datetime.date.fromisoformat("2022-12-15"))
print('datetime.date.fromordinal(ordinal) function :- ', datetime.date.fromordinal(1))
print('datetime.date.toordinal() function :- ', today_date.toordinal())

print("datetime.date.min :- ", datetime.date.min)
print("datetime.datetime.max :- ", datetime.date.max)
print("datetime.date.day :- ", datetime.date.today().day)
print("datetime.date.month :- ", datetime.date.today().month)
print("datetime.date.year :- ", datetime.date.today().year)
print('datetime.date.resolution :- ', datetime.date.resolution)

print("\n----------------- Time Class ----------------------\n")
# Example 1 :- Time Object representing time in python
print("Entered Time :- ", datetime.time(15, 12, 3, 60000))  # Calling the 'time' constructor
print("Calling 'time' constructor with 'hour' argument :- ", datetime.time(hour=23))
print("Calling 'time' constructor with 'minute' argument :- ", datetime.time(minute=59))
print("Calling 'time' constructor with 'second' argument :- ", datetime.time(second=59))
print("Calling 'time' constructor with 'microsecond' argument :- ", datetime.time(microsecond=23689))
print("Calling 'time' constructor with no argument :- ", datetime.time())
# print(datetime.time(hour=24)) # It raises a ValueError
# print(datetime.time(hour='26')) # It raises a TypeError

# Example 2 :- Get hours, minutes, seconds, and microseconds
current_time = datetime.datetime.today()
print("Hours :- ", current_time.hour)
print("Minutes :- ", current_time.minute)
print("Seconds :- ", current_time.second)
print("Microseconds :- ", current_time.microsecond)

# Example 3 :- Convert time object to string
print("datetime.time.isoformat() method :- ", current_time.isoformat())
print("24 hours format :- strftime() :- ", current_time.strftime("%H : %M : %S : %f"))
print("12 hours format :- strftime() :- ", current_time.strftime("%I : %M : %S : %f %p"))

print("----------- Time class methods and it's attributes -------------")
# Methods
print("datetime.time.dst() method :- ", current_time.time().dst())
print("datetime.time.replace() method :- ", current_time.replace(hour=15, minute=15, second=15, microsecond=15))
print("datetime.time.isoformat() method :- ", current_time.isoformat())
print("datetime.time.strftime() method :- ", current_time.strftime("%H : %M : %S : %f"))
print("datetime.time.tzname() method :- ", current_time.time().tzname())
print("datetime.time.fromisoformat(string) method :- ", current_time.time().fromisoformat(current_time.time().isoformat()))
print("datetime.time.utcoffset() method :- ", current_time.time().utcoffset())

# Attributes
print("datetime.time.hour attribute :- ", current_time.hour)
print("datetime.time.minute attribute :- ", current_time.minute)
print("datetime.time.second attribute :- ", current_time.second)
print("datetime.time.microsecond attribute :- ", current_time.microsecond)
print("datetime.time.min attribute :- ", current_time.time().min)
print("datetime.time.max attribute :- ", current_time.time().max)
print("datetime.time.resolution attribute :- ", current_time.time().resolution)
print("datetime.time.tzinfo attribute :- ", current_time.time().tzinfo)
print("datetime.time.fold attribute :- ", current_time.time().fold)

print("----------- Datetime class --------------")
# Example 1 :- DateTime object representing DateTime in Python
print("Datetime class Constructor:- ", datetime.datetime(2022, 3, 15, 23, 53, 59, 15236))
# Example 2: Get year, month, hour, minute, and timestamp
current_date_and_time = datetime.datetime.today()
print("Day : ", current_date_and_time.day)
print("Month : ", current_date_and_time.month)
print("Year : ", current_date_and_time.year)
print("Hours : ", current_date_and_time.hour)
print("Minutes : ", current_date_and_time.minute)
print("Seconds : ", current_date_and_time.second)
print("Microseconds : ", current_date_and_time.microsecond)
print("timestamp : ", current_date_and_time.timestamp())

# Example 3: Current date and time
print("Current date and time using 'now()' function :- ", datetime.datetime.now())
print("Current date and time using 'today()' function :- ", datetime.datetime.today())

# Example 4: Convert Python Datetime to String
date_to_string = datetime.datetime.isoformat(current_date_and_time)
print("Datetime to string using 'isoformat()' function :- ", date_to_string)
print(type(date_to_string))
date_to_string = datetime.datetime.strftime(current_date_and_time, "Date :- %d / %m / %Y Time :- %I : %M : %S : %f : %p")
print("Datetime to string using 'strftime()' function :- ", date_to_string)
print(type(date_to_string))

# List of datetime class methods and it's attributes
print("now() function :- ", datetime.datetime.now())
print("today() function :- ", datetime.datetime.today())
print("isoformat() function :- ", current_date_and_time.isoformat())
print("isocalendar() function :- ", current_date_and_time.isocalendar())
print("isoweekday() function :- ", current_date_and_time.isoweekday())
print("strftime(string) function :- ", datetime.datetime.strftime(current_date_and_time, "Date :- %d / %m / %Y \n Time :- %I : %M : %S : %f : %p"))
# print(current_date_and_time.strptime(date_to_string, "%H / %M / %S"))
print("fromtimestamp(timestamp) function :- ", current_date_and_time.fromtimestamp(current_date_and_time.timestamp()))
print("timestamp : ", current_date_and_time.timestamp())
print("date() function :- ", current_date_and_time.date())
print("time() function :- ", current_date_and_time.time())
print("tzname() function :- ", current_date_and_time.tzname())
print("timetz() function :- ", current_date_and_time.timetz())
print("fromordinal(n) function :- ", current_date_and_time.fromordinal(1))
print("toordinal() function :- ", current_date_and_time.toordinal())
print("timetuple() function :- ", current_date_and_time.timetuple())
print("utctimetuple() function :- ", current_date_and_time.utctimetuple())
print("utcoffset() function :- ", current_date_and_time.utcoffset())
print("utcfromtimestamp(timestamp) function :- ", current_date_and_time.utcfromtimestamp(current_date_and_time.timestamp()))
print("utcnow() function :- ", current_date_and_time.utcnow())
print("ctime() function :- ", current_date_and_time.ctime())
print("replace() function :- ", current_date_and_time.replace(current_date_and_time.year, current_date_and_time.month, current_date_and_time.day, current_date_and_time.hour, current_date_and_time.minute, current_date_and_time.second, current_date_and_time.microsecond, current_date_and_time.tzinfo))
print("dst() function :- ", current_date_and_time.dst())
print("astimezone() function :- ", current_date_and_time.astimezone(current_date_and_time.tzinfo))
print("combine() function :- ",current_date_and_time.combine(current_date_and_time.date(), current_date_and_time.time(), current_date_and_time.tzinfo))

# Attributes
print("Day : ", current_date_and_time.day)
print("Month : ", current_date_and_time.month)
print("Year : ", current_date_and_time.year)
print("Hours : ", current_date_and_time.hour)
print("Minutes : ", current_date_and_time.minute)
print("Seconds : ", current_date_and_time.second)
print("Microseconds : ", current_date_and_time.microsecond)
print("resolution :- ", current_date_and_time.resolution)
print("min :- ", current_date_and_time.min)
print("max :- ", current_date_and_time.max)
print("tzinfo :- ", current_date_and_time.tzinfo)
print("fold :- ", current_date_and_time.fold)

print("\n------------------------ Time delta class --------------------\n")
# Example 1: Add days to datetime object
future_date = datetime.datetime(2024, 12, 15, 15, 12, 16, 123)
print("Add days to datetime object : ", current_date_and_time + datetime.timedelta(days=730))

# Example 2: Difference between two date and times
print("Difference between two date and time :- ", future_date - current_date_and_time)

# Time delta class function and it's attributes
timedelta = datetime.timedelta(373, 123654, 123654789, 15263.39, 4523, 1523, 756)
print(datetime.timedelta.min)
print(datetime.timedelta.max)
print(datetime.timedelta.resolution)
print(timedelta.days)
print(timedelta.total_seconds())
print(timedelta.microseconds)
print(timedelta.seconds)

# Operators
print(current_date_and_time + datetime.timedelta(days=730))
print(current_date_and_time - datetime.timedelta(days=730))
