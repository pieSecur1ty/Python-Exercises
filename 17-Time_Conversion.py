# user input
from time import time

# user input
input_time = input("Enter the time in 12-hour format : ")


# time conversion
hour = int(input_time[0:2])
if input_time[8:10].upper() == "PM":
    if hour < 12:
        hour += 12
    else:
        pass

elif input_time[8:10].upper() == "AM":
    if hour == 12:
        hour = "00"
    else:
        pass

else:
    print("Invalid Option!")


# output
converted_time = str(hour) + input_time[2:8]
print(f"Converted time in 24-hour format : {converted_time}")
