signature = ' ~Bocik 0.08v'


def went_sleep(hour_when_wake_up):
    if not hour_when_wake_up.isdigit():
        print('Write proper time in int: ', end='')
    else:
        if 0 < int(hour_when_wake_up) and int(hour_when_wake_up) > 24:
            print('Write proper time between 0-24: ', end='')
        else:
            message = 'Poszedłem spać. Prawdopodbnie wstanę około ' + hour_when_wake_up + signature
            return message
    went_sleep(input())


print('hour when you wake up: ', end='')
text = went_sleep((input()))
print(text)
