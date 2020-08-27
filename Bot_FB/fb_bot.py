from getpass import getpass
import fbchat
from fbchat import log, Client
from fbchat.models import *
import Bot_FB.messages as messages

song_lyric = open("shooting_star.txt", "r")
message = ''

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


def login():
    usr = input('Enter Email ID: ')
    pwd = getpass('Enter Password: ')
    client = fbchat.Client(usr, pwd)
    return client

def check_info(client):

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

    # client.send(Message('to jest test bota, zignoruj to'), user.uid)
    # client.send(Message('Hi Me!'), client.uid)


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
        log.info('{} from in {}'.format(message_object, thread_id, ))

        if author_id != self.uid:
            self.send(Message(song_lyric.readline()), thread_id=thread_id, )
            if song_lyric.readline() == "":
                Client.logout()


class Song_even(Client):
    i = 1

    def onMessage(self, author_id, message_object, thread_id, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        log.info('{} from in {}'.format(message_object, thread_id, ))

        if author_id != self.uid:
            self.send(Message(song_lyric.readline()), thread_id=thread_id, )
            if song_lyric.readline() == "":
                Client.logout()



class I_went_sleep(Client):
    print('Write hour when you wake up: ', end='')
    message = messages.went_sleep(input())

    def onMessage(self, author_id, message_object, thread_id, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        log.info('{} from in {}'.format(message_object, thread_id, ))

        if author_id != self.uid:
            if author_id not in listofauthors:
                self.send(Message(message), thread_id=thread_id, )
                listofauthors.append(author_id)


# send_mesange_fbchat()
# login()

# client = Dissbot(login, password)

# client = Song_even(login,password)
# client2 = Song_odd(login2,password2)

# client.listen()
# client2.listen()
# check_info()
# for line in song_lyric:
#    print(line)
listofauthors = []

usr = input('Enter Email ID: ')
pwd = getpass('Enter Password: ')
client = I_went_sleep(usr, pwd)
client.listen()












