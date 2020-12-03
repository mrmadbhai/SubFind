import requests


red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# Logo of SUbFind

print(red+"  ______ _____  _____ ______  ________ _____ ____  _____ ______    "+red)
print(red+".' ____ \_   _||_   _|_   _ \|_   __  |_   _|_   \|_   _|_   _ `.  "+red)
print(red+"| (___ \_|| |    | |   | |_) | | |_ \_| | |   |   \ | |   | | `. \ "+red)
print(cyan+" _.____`. | '    ' |   |  __'. |  _|    | |   | |\ \| |   | |  | | "+cyan)
print(cyan+"| \____) | \ \__/ /   _| |__) || |_    _| |_ _| |_\   |_ _| |_.' / "+cyan)
print(cyan+" \______.'  `.__.'   |_______/_____|  |_____|_____|\____|______.'  "+cyan)
print(lgreen+"                                                             V1.0 \n"+lgreen)



print (lgreen+bold+"             <===[[ coded by Mr. Mad Bhai ]]===> "+clear)
print (yellow+bold+"        <===(( search on youtube Mr. Mad Bhai ))===> "+clear)
print (lgreen+bold+"   <==={{ This helps you to Find Subdomain for Victim Site }}===> "+clear)
print (red+bold+"<===[( This Tool is Only For Educational Purpose Only. )]===> \n"+clear)
print (yellow+bold+'''How to put link?

=> Yo have to put link with out http or htttps. Eg. example.com \n'''+clear)


domain = input(cyan+"Put Domain Here: "+clear)

file = open('sub.txt', 'r')

content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url= f'http://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(yellow+'Subdomain Finded: ', url+clear)