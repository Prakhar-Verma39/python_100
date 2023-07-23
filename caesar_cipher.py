CC = '''
                                                   .__       .__                  
  ____ _____    ____   ___________ _______    ____ |__|_____ |  |__   ___________ 
_/ ___\\__  \ _/ __ \ /  ___/\__  \\_  __ \ _/ ___\|  \____ \|  |  \_/ __ \_  __ \\
\  \___ / __ \\  ___/ \___ \  / __ \|  | \/ \  \___|  |  |_> >   Y  \  ___/|  | \/
 \___  >____  /\___  >____  >(____  /__|     \___  >__|   __/|___|  /\___  >__|   
     \/     \/     \/     \/      \/             \/   |__|        \/     \/       
'''

def caesar_cipher(m,s,f):
    ret = ""
    if f == 1:
        for x in m:
            if x == " " or x == "." or x == "!":
                ret += x
            else:
                ret += chr(ord(x) + s) 
    if f == 0:
        for x in m:
            if x == " ":
                ret += " "
            else:
                ret += chr(ord(x) - s) 
    return ret

print(CC)
while True:
    opt = input( "\n Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if(opt == 'encode'):
        m = input("Type your message:\n").lower()
        s = int(input("Type the shift number:")) % 26
        print(f"Here's the encoded result: {caesar_cipher(m,s, 1)}")
    elif(opt == 'decode'):
        m = input("Type your message:\n").lower()
        s = int(input("Type the shift number:")) % 26
        print(f"Here's the decoded result: {caesar_cipher(m,s, 0)}")

    if(input('Type "yes" if you want to go again. Otherwise type "no".') == 'no'):
        break
    else:
        continue