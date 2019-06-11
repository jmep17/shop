# Problem: check shop opening times
# Input: day - as week, sat or sun
# Input: hour, an integer from 0 to 23 inclusive

day = 'sat'
hour = 8

# Output: a string, either 'open' or 'closed'

if day == 'week':
    if 9 <= hour < 17:
        print ('open1')
    else:
        print ('closed1')

elif day == 'sat':
    if 9 <= hour < 13:
        print ('open2')
    else:
        print ('closed2')

elif day == 'sun':
    print ('closed3')
