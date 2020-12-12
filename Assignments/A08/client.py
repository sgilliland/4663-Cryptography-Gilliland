"""
Sarah Gilliland
CMPS 4663 - cryptography
Program 08 - RSA Public Key Encryption

https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import base64
# Used to Generate Keys
from crypto_class import Crypto
#Used to Store Keys and Read in Keys
from cryptography.hazmat.primitives import serialization

# Global Variables
TOKEN = 'a29c40228b3be56a4732a12db7f2d8c5'
UID = '5147600'
API = 'http://msubackend.xyz/api/?route='
USERS = {}
PUBKEYS = {}


# Method to load the public key
def loadPubKey(pubkey):
    return serialization.load_pem_public_key(pubkey)


# Method to get all users public keys from the server
def pubKey():
    global PUBKEYS
    route = 'getPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        keys = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for key in keys['data']:
        PUBKEYS[key['uid']] = key


# Method to get Users data from server
def getUsers():
    global USERS
    global PUBKEYS

    route = 'getUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        users = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for user in users['data']:
        if user['uid'] in PUBKEYS:
            user['pubkey'] = PUBKEYS[user['uid']]['pubkey']
            USERS[user['uid']] = user


# Method to get Active users from server
def getActive():
    route = 'getActive'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    active_users = r.json()
    active_users = active_users['data']

    real_active_users = []
    for active in active_users:
        active['fname'] = USERS[active['uid']]['fname']
        active['lname'] = USERS[active['uid']]['lname']
        active['email'] = USERS[active['uid']]['email']
        active['pubkey'] = PUBKEYS[active['uid']]
        real_active_users.append(active)

    return real_active_users


# Method to encrypt a message and publish the encrypted message to server
def postMessage(message,to_uid):
    print(f"Posting message to {USERS[to_uid]['fname']} {USERS[to_uid]['lname']}...")

    route = 'postMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    A = Crypto()
    A.load_keys(PUBKEYS[to_uid]['pubkey'])

    encrypted = A.encrypt(message)
    encrypted_bytes = base64.b64encode(encrypted)
    message = encrypted_bytes.decode('utf-8')

    payload = {
       'uid':UID,
       'to_uid':to_uid,
       'message':message,
       'token':TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()


# Method to publish the public key to the server
def publishKey(pubkey):
    route = 'postPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    payload = {
        'pub_key':pubkey,
        'uid':UID,
        'token':TOKEN
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post( url, headers=headers, json=payload)
    return r.json()


# Method to get the users messages from the server
# count = how many messages, starting from the most recent
def getMessages(count=1, latest=True):
    """ Gets decrypted messages from the server. """

    print("Checking for new messages...")

    route = 'getMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}&count={count}"
    r = requests.get(url)

    D = Crypto()
    D.load_keys(priv_file="my_private_key.txt")

    messages = r.json()
    messages = messages['data']         # get all the messages received from other users

    for message in messages:
        fid, received = message['fid'], message['message']         # grabs most recent message and user's id
        received_bytes = received.encode('utf-8')               # prepares message
        received = base64.decodebytes(received_bytes)           # for decryption

        try:
            decrypted = D.decrypt(received)         #decrypts message
            print(f"\nfrom: {USERS[fid]['fname']} {USERS[fid]['lname']}")
            print("message:", decrypted, '\n')
        except ValueError:
            print(f"\nfrom: {USERS[fid]['fname']} {USERS[fid]['lname']}")
            print("message:", received, '\n')



if __name__ == '__main__':
    # intial commands to retrieve information
    pubKey()
    getUsers()

    '''
    # Generating new keys
    C = Crypto()
    public_key = C.generate_keys()
    C.store_keys()
    publishKey(public_key)
    '''

    # print a menu
    choice = input("\nEnter the number of the action you would like to take:\n1. Check for messages\n2.Send a message\n3.Quit\n")

    while (choice != "3" and choice != "3."):
      ############################## Check the messages
      if (choice == '1' or choice == "1."):
        message_count = input("How many messages would you like to see? ")
        # now get the message and decode it
        getMessages(count = message_count)
        
      ############################## Send a message
      elif(choice == '2' or choice == "2."):
        # get and display the active users
        active = getActive()
        print("Here are the active users right now: ")
        for a in active:
          print(a)

        uidSend = input("Who do you want to send a message to? Enter their uid: ");
        uidSend_firstName = USERS[uidSend]['fname']
        
        print("Message to ", uidSend_firstName)
        newMessage = input("Type your message here: ");

        postMessage(newMessage, uidSend)

      
      ############################## Display the menu again
      choice = input("\nEnter the number of the action you would like to take:\n1. Check for messages\n2.Send a message\n3.Quit\n")

    #5147600 - my uid
    #5217300 - chad's uid
