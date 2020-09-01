signature = ' ~Bocik 0.08v'


def went_sleep(hour_when_wake_up=None):
    message = 'Poszedłem spać. '
    if hour_when_wake_up is None or hour_when_wake_up == '':
        message += ' Nie wiem o której wstanę.' + signature
        return message
    else:
        if not hour_when_wake_up.isdigit():
            print('Write proper time in int: ', end='')
        else:
            if 0 < int(hour_when_wake_up) and int(hour_when_wake_up) > 24:
                print('Write proper time between 0-24: ', end='')
            else:
                message += ' Prawdopodbnie wstanę około ' + hour_when_wake_up + signature
                return message
        return went_sleep(input())


def unique_message():
    print("Write your message here: ", end='')
    message = input() + signature
    return message


def go_work(end_of_work=None):
    message = 'Nie mogę teraz rozmawiać. Pracuję w tym momencie.'
    if end_of_work is None or end_of_work == '':
        message += signature
        return message
    else:
        if not end_of_work.isdigit():
            print('Write proper time in int: ', end='')
        else:
            if 0 < int(end_of_work) and int(end_of_work) > 24:
                print('Write proper time between 0-24: ', end='')
            else:
                message += ' Skończę pracę około ' + end_of_work + signature
                return message
        return go_work(input())


print(type(input()))
print('hour when you wake up: ', end='')
text = went_sleep((input()))
print(text)
print('---------------')
print('hour when you end work: ', end='')
text = go_work(input())
print(text)
print('---------------')
print(go_work())
