import re
import sys



def dayOfProgrammer(year):
    # Write your code here
    if 1700 <= year <= 1917:
        # follows the Julian calendar
        if year % 4 == 0:
            feb_days = 29
        else:
            feb_days = 28
        
    elif 1919 <= year <= 2700:
        # follows the Gregorian calendar
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            feb_days = 29
        else:
            feb_days = 28
        
    elif year == 1918:
        # follows transition year
        feb_days = 15
        
    days_in_month = [31, feb_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_count = 0
    for i in range(12):
        day_count += days_in_month[i]
        if day_count >= 256:
            month = i + 1
            day = 256 - (day_count - days_in_month[i])
            break

    return f"{day:02d}.{month:02d}.{year}"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
