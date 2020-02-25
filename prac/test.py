def twelveto24(time_to_convert):
    hour = []
    minutes = ''
    ampm = ''
    parts = time_to_convert.split(':')
    hour = parts[0]
    temp = parts[1]
    for t in temp:
        if t.isdigit() == True:
            minutes += t
        else:
            ampm += t

    if ampm == 'pm':
        hour = int(hour) + 12

    time_coverted = str(hour) + ':' + minutes

    return time_coverted

print(twelveto24('11:23am'))

