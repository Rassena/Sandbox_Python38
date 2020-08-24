from getpass import getpass
import fbchat
from fbchat import log, Client
from fbchat.models import *

usr=input('Enter Email ID: ')
pwd=getpass('Enter Password: ')


shooting_star = """It's late and I'm awake
Staring at the wall
Open up my window
Head falls out the door
No one else around
And a shimmer takes my eye
I lift my head
Blinded by the sky
Feel my weight in front
Following the sound
Moves away so fast
Falling to the ground
I know what is more to come
Jump back to my feet
Now I only see ahead of me
Chasing down the street (down the street, down the street, down the street)
Give my love to a shooting star
But she moves so fast
That I can't keep up
I'm chasing
I'm in love with a shooting star
But she moves so fast
When she falls then
I'll be waiting
Give my love to a shooting star
But she moves so fast
That I can't keep up
I'm chasing
I'm in love with a shooting star
But she moves so fast
When she falls then
I'll be waiting
Give my love to a shooting star
But she moves so fast
That I can't keep up
I'm chasing
I'm in love with a shooting star
But she moves so fast
When she falls then
I'll be waiting
Give my love to a shooting star
But she moves so fast
That I can't keep up
I'm chasing
I'm in love with a shooting star
But she moves so fast
When she falls then
I'll be waiting"""


def send_mesange_fbchat():
    client = fbchat.Client(str(input('Email: ')), getpass())
    no_of_friends = int(input('number of friends: '))
    for i in range(no_of_friends):
        send_to = input('Send to (name and surname): ')
        messange = input('Messange: ')
        users = client.searchForUsers(send_to)
        user = users[0]
        sent = client.send(messange, user.uid)
        if sent:
            print('Message sent successfully!')


def just_login(username, passw):
    client = fbchat.Client(username, passw)


def check_info():
    client = fbchat.Client(usr, pwd)
    """
    users = client.searchForUsers(input('Name to search: '))
    user = users[0]
    print('User ID: {}'.format(user.uid))
    print('user name: {}'.format(user.name))
    print('user profile pictore URL: {}'.format(user.photo))
    print('user main URL {}'.format(user.url))
    print('user Email: {]'.format(user.email))
    """
    users = client.searchForUsers(input('Name to search: '))
    user = users[0]
    print('{}'.format(user.name) + ': ')
    for x in range(len(client.getEmails())):
        print('{}'.format(client.getEmails()[x]))

    #client.send(Message('to jest test bota, zignoruj to'), user.uid)
    #client.send(Message('Hi Me!'), client.uid)


class Echobot(Client):
    def onMessage(self, author_id, message_object, thread_id, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info('{} from in {}'.format(message_object, thread_id, ))

        if author_id != self.uid:
            self.send(message_object, thread_id, )


class Dissbot(Client):
    def onMessage(self, author_id, message_object, thread_id, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info('{} from in {}'.format(message_object, thread_id, ))

        if author_id != self.uid:
            # self.send(Message('*** *'), thread_id,)
            self.sendLocalImage('C:/Users/Użytkownik/Downloads/beep-boop.jpg', message='', thread_id=thread_id)


class Song_odd(Client):
    i = 0

    def onMessage(self, author_id, message_object, thread_id, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        song = shooting_star.split('\n')
        log.info('{} from in {}'.format(message_object, thread_id, ))

        if author_id != self.uid:
            self.send(Message(song[Song_odd.i]), thread_id=thread_id, )
            Song_odd.i += 2
            if Song_odd.i >= len(song):
                Client.logout()


class Song_even(Client):
    i = 1

    def onMessage(self, author_id, message_object, thread_id, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        song = shooting_star.split('\n')
        log.info('{} from in {}'.format(message_object, thread_id, ))

        if author_id != self.uid:
            self.send(Message(song[Song_even.i]), thread_id=thread_id, )
            Song_even.i += 2
            if Song_even.i >= len(song):
                Client.logout()


# send_mesange_fbchat()
# just_login()

#client = Dissbot(login, password)

#client = Song_even(login,password)
#client2 = Song_odd(login2,password2)

#client.listen()
#client2.listen()
check_info()
