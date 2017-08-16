# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    def get_days_in_month(month,year):
#        print("in get_days_in_month")
        if(month == 1):
            days_in_month = 31
            return days_in_month
        if(month == 2 and year%4 == 0):
            days_in_month = 29
            print("days_in_month", days_in_month)
            return days_in_month
        if(month == 2 and year%4 != 0):
            days_in_month = 28
            print("days_in_month", days_in_month)
            return days_in_month
        if(month == 3):
            days_in_month = 31
            return days_in_month
        if(month == 4):
            days_in_month = 30
            return days_in_month
        if(month == 5):
            days_in_month = 31
            return days_in_month
        if(month == 6):
            days_in_month = 30
            return days_in_month
        if(month == 7):
            days_in_month = 31
            return days_in_month
        if(month == 8):
            days_in_month = 31
            return days_in_month
        if(month == 9):
            days_in_month = 30
            return days_in_month
        if(month == 10):
            days_in_month = 31
            return days_in_month
        if(month == 11):
            days_in_month = 30
            return days_in_month
        if(month == 12):
            days_in_month = 31
            return days_in_month
        else:
            days_in_month = 30
            return days_in_month

    if(year1 == year2 and month1 != month2):
#        print("1.Birth date and current date are in same year")
        if(year1%4 ==0):
#            print("1.We have a leap year")
            days_in_month1 = get_days_in_month(month1,year1)
            rem_days = days_in_month1 - day1
            while(True):
                if(month1<month2):
#                    print("1. We are in month1 < month2")
                    month1 = month1 + 1
                    if(month1 == month2):
                        rem_days = rem_days + day2
                        break
                    else:
                        days_in_month1 = get_days_in_month(month1,year1)
                        rem_days = days_in_month1 + rem_days
        print("rem_days", rem_days)
        return rem_days
    if(year1 == year2 and month1 == month2):
#        print("We are in month1 == month2")
        rem_days = day2 - day1
        print("rem_days", rem_days)
        return rem_days
    
    if(year1 != year2):
#        print("2.We are in year1 != year2")
        if(year2-year1 == 1 and month2 <= month1):
#            print("2. Difference of years is less than one")
            days_in_month1 = get_days_in_month(month1,year1)
            rem_days = days_in_month1 - day1
            while(True):
                if(month1 == 12):
                    month1 = 0
                    year1 = year1 + 1
                month1 = month1 + 1
                if(month1 == month2):
                    rem_days = rem_days + day2
                    break
                else:
                    days_in_month1 = get_days_in_month(month1,year1)
                    rem_days = days_in_month1 + rem_days
            print("rem_days", rem_days)
            return rem_days
        
        else:
            print("Difference of years is more than one")
            total_years = year2 - year1
            if(total_years%4 == 0):
                leap_years = total_years/4
                norm_years = total_years - leap_years
                leap_days = leap_years * 366
                nom_days = norm_years * 365
            else:
                if(total_years/4 < 1):
                    leap_years = 0
                    norm_years = year2 - year1
                    leap_days = 0
                    norm_days = norm_years * 365
                else:
                    leap_years = total_years/4
                    norm_years = total_years - leap_years
                    leap_days = leap_years * 366
                    norm_days = norm_years *365
                    print("leap_days", leap_days)
                    print("norm_days", norm_days)
            if(month1<month2):
                days_in_month1 = get_days_in_month(month1,year1)
                rem_days = days_in_month1 - day1
                while(True):
                    month1 = month1 + 1
                    if(month1 == month2):
                        rem_days = rem_days + day2
                        break
                    else:
                        days_in_month1 = get_days_in_month(month1,year2)
                        rem_days = days_in_month1 + rem_days
            else:
                days_in_month1 = get_days_in_month(month1,year1)
                rem_days = days_in_month1 - day1
                while(True):
                    print("in month1>month2")
                    month1 = month1 + 1
                    if(month1 == 12):
                        month1 = 0
                        year1 = year1 + 1
                    if(month1 == month2):
                        rem_days = rem_days + day2
                        break
                    else:
                        days_in_month1 = get_days_in_month(month1,year1)
                        rem_days = rem_days + days_in_month1
                        
            rem_days = rem_days + norm_days+leap_days
            print("rem_days", rem_days)
            return rem_days
                    
                    
            
                
                        
                        
    ##
    # Your code here.
    ##


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
