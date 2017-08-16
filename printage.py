# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    norm_days = 0
    leap_days = 0
    days_in_month1 = 0 
    days_in_month = 0
    
    total_years = year2 - year1
    leap_years  = total_years/4
    norm_years   = total_years - leap_years
    leap_days   = leap_years * 366
    norm_days    = norm_years * 365
    print("norm_days", norm_days)
    print("leap_days", leap_days)
    def get_days_in_month(month,year):
        print("in get_days_in_month")
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

        
    days_in_month1 = get_days_in_month(month1,year1)
    rem_days = days_in_month1 - day1
    print("rem_days", rem_days)
    while(True):
        if(month1>month2):
            print("in month1>month2")
            month1 = month1 + 1
            if(month1 == 12):
                month1 = 0
                year1 = year1 + 1
            if(month1 == month2):
                rem_days = rem_days + day2
                print 
                break
            else:
                days_in_month1 = get_days_in_month(month1,year1)
                rem_days = rem_days + days_in_month1
        if(month1<month2):
            print("in month1<month2")
            month1 = month1 + 1
            if(month1 == month2):
                rem_days = rem_days + day2
                break
            else:
                days_in_month1 = get_days_in_month(month1,year2)
                rem_days = rem_days + days_in_month1
        else:
            if(month1 == month2):
                print("in month1 == month2")
                if(year1 == year2):
                    print("in year1 == year2")
                    age_in_days = day2-day1
                    break
                else:
                    print("in year1 != year2")
                    if(day1 == day2):
                        if(month1 > 2 and year2-year1 == 1):
                            rem_days = rem_days + 1
                        break
                    else:
                        if(day2 < day1 and year2-year1 == 1):
                            while(True):
                                norm_days = 0
                                leap_days = 0
                                month1 = month1 + 1
                                if(month1 == month2):
                                    rem_days = rem_days + day2
                                    break
                                else:
                                    days_in_month1 = get_days_in_month(month1,year1)
                                    rem_days = rem_days + days_in_month1
                                
                                
                                
                        
                                    
                                
                            
    
    age_in_days = norm_days+ leap_days + rem_days
    print("age in days", age_in_days)        

        
        
        
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
