def convert(number):
    msg = ''

    if number % 3 == 0:
        msg += 'Pling'
    
    if number % 5 == 0:
        msg += 'Plang'
    
    if number % 7 ==0:
        msg += 'Plong'
    
    if msg == '':
        return str(number)
    else:
        return msg
