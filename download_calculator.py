# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(time_seconds):
#    print "Entering convert seconds"
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
    if ( pos != -1 and time_seconds[(pos+1):] != 0):
        seconds = seconds + "." + time_seconds[(pos+1):]
#    print seconds
#    seconds = float(seconds)
    
    hours = str(hours)
    minutes = str(minutes)
    
    if hours=='1' or hours == '1.0':
        hours = hours + " hour"
    else:
        hours = hours + " hours"
    if minutes=='1' or minutes == '1.0':
        minutes = minutes + " minute"
    else:
        minutes = minutes + " minutes"
    if seconds=='1' or seconds == '1.0':
        seconds = seconds + " second"
    else:
        seconds = seconds + " seconds"
        
    timelist.append(hours)
    timelist.append(minutes)
    timelist.append(seconds)
    time = timelist[0]+', '+timelist[1]+', '+timelist[2]
    return time


def download_time(fs,fu,bw,bu):
#    print "download time"
    time = 0
    time_words = 0
    
    if fu == bu:
#        print "when units are same "
        time = fs*1.0/bw
        print "time", time
        
    if fu[1] != bu[1]:
#        print " b and B difference"
        if fu[1] == 'b':
            fs = (fs*1.0)/8
        else:
            fs = fs*1.0*8
        
    if fu[0] == bu[0] and fu[1] != bu[1]:
#        print "when everything except b and B are same"
        time = fs*1.0/bw
        print "time", time
    
    if fu[0] != bu[0]:
#        print"if the first letters arent the same"
        if fu[0] == 'k'  and bu[0] == 'M':
            fs = fs*1.0/(1024)
        if fu[0] == 'k'  and bu[0] == 'G':
            fs = fs*1.0/(1024*1024)
        if fu[0] == 'k'  and bu[0] == 'T':
            fs = fs*1.0/(1024*1024*1024)
        if fu[0] == 'M'  and bu[0] == 'k':
            fs = fs*1.0*1024
        if fu[0] == 'M'  and bu[0] == 'G':
            fs = fs*1.0/(1024)
        if fu[0] == 'M'  and bu[0] == 'T':
            fs = fs*1.0/(1024*1024)
        if fu[0] == 'G'  and bu[0] == 'k':
            fs = fs*1.0*1024*1024
        if fu[0] == 'G'  and bu[0] == 'M':
            fs = fs*1.0*1024
        if fu[0] == 'G'  and bu[0] == 'T':
            fs = fs*1.0/(1024)
        if fu[0] == 'T'  and bu[0] == 'k':
            fs = fs * 1.0 *1024*1024*1024
        if fu[0] == 'T'  and bu[0] == 'M':
            fs = fs * 1.0 *1024*1024
        if fu[0] == 'T'  and bu[0] == 'G':
            fs = fs * 1.0 *1024
    
    
    time = fs/bw
#    print "time",time
    time_words = convert_seconds(time)
#    print "time_words", time_words
    return time_words
    
            



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

#print download_time(1,'Tb', 100, 'MB')
