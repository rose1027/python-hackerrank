# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
# Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#
def timeConversion(s):
    hour = s[0:2]
    min = s[3:5]
    senc = s[6:8]
    time = s[-2:]
    newS = ''
    if hour == '12' and time == 'AM':
        hour = '00'
        newS = hour + ':' +min+':'+senc
    elif hour == '12' and time == 'PM':
        newS = hour + ':' +min+':'+senc
    elif time == 'PM':
        Hour = int(hour)
        Hour += 12
        hour = str(Hour)
        newS = hour + ':' +min+':'+senc
    else:
        newS = hour + ':' +min+':'+senc
    return newS
s = timeConversion('12:05:45AM')
print(s)