# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(time_seconds):
    seconds = int(time_seconds)
    timelist = []
    pos = 0 
    hour_to_sec = 3600
    minute_to_sec = 60
    time = 0
    
    hours = seconds/hour_to_sec
    seconds = seconds - (hours * hour_to_sec)
    minutes = seconds/minute_to_sec
    seconds = seconds - (minutes * minute_to_sec)
    seconds = str(seconds)
    time_seconds = str(time_seconds)
    pos = time_seconds.find(".")
    if ( pos != -1):
        seconds = seconds + "." + time_seconds[(pos+1):]
#    print seconds
#    seconds = float(seconds)
    
    hours = str(hours)
    minutes = str(minutes)
    
    if hours=='1':
        hours = hours + " hour"
    else:
        hours = hours + " hours"
    if minutes=='1':
        minutes = minutes + " minute"
    else:
        minutes = minutes + " minutes"
    if seconds=='1':
        seconds = seconds + " second"
    else:
        seconds = seconds + " seconds"
        
    timelist.append(hours)
    timelist.append(minutes)
    timelist.append(seconds)
    time = timelist[0]+', '+timelist[1]+', '+timelist[2]
    return time
    
print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
