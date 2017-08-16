# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    total_years = year2 - year1
    leap_years  = total_years/4
    norm_years   = total_years - leap_years
    leap_days   = leap_years * 366
    norm_days    = norm_years * 365
    
    print("total years", total_years)
    print("leap years", leap_years)
    
    def get_days_in_month(month1):
        if (month1 == 1):
            days_in_month1 = 31
        if (month1 == 2 and leap_years == 0 and (year2%4 == 0 or year1%4 == 0)):
            days_in_month1 = 29
        if (month1 == 2 and (year2%4 != 0 or year1%4 != 0)):
            days_in_month1 = 28
        if (month1 == 3):
            days_in_month1 = 31
        if (month1 == 4):
            days_in_month1 = 30
        if (month1 == 5):
            days_in_month1 = 31
        if (month1 == 6):
            days_in_month1 = 30
        if (month1 == 7):
            days_in_month1 = 31
        if (month1 == 8):
            days_in_month1 = 31
        if (month1 == 9):
            days_in_month1 = 30
        if (month1 == 10):
            days_in_month1 = 31
        if (month1 == 11):
            days_in_month1 = 30
        if (month1 == 12):
            days_in_month1 = 31
        return days_in_month1
    
    
        
    
    days_in_month1 = get_days_in_month(month1)    
    rem_days = (days_in_month1-day1) 
    print("rem_days", rem_days)
    
    
    while(True):
        if(month1<month2):
            break
        if(month1>month2):
            print("month1 > month2")
            if(month1 == 12):
                month1 = 0
        month1 = month1 + 1
        if(month1 == month2):
            rem_days = rem_days + day2
            break
        else:
            days_in_month1 = get_days_in_month(month1)
            rem_days = rem_days + days_in_month1
    
    while(True): 
        if(month1>month2):
            break
        if(month1<month2):
            print("month1<month2")
            month1 = month1 + 1
        if(month1 == month2):
           rem_days = rem_days + day2
           break
        else:
           days_in_month1 = get_days_in_month(month1)
           rem_days = rem_days + days_in_month1
                
    print("rem days", rem_days)
    print("leap_days", leap_days)
    print("norm_days", norm_days)
    age_in_days = rem_days + leap_days + norm_days
    
    print (age_in_days)
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
