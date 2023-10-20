#Kali4Mac, Written by Scott Garcia


import os
import sys, traceback


#Declaring arrays of hacking tools
array1 = ['sudo -u $SUDO_USER brew install acccheck', 'sudo -u $SUDO_USER brew install ace', 'sudo -u $SUDO_USER brew install amap', 'sudo -u $SUDO_USER brew install automater', 'sudo -u $SUDO_USER brew install braa', 'sudo -u $SUDO_USER brew install casefile', 'sudo -u $SUDO_USER brew install cdpsnarf', 'sudo -u $SUDO_USER brew install cisco-torch', 'sudo -u $SUDO_USER brew install cookie-cadger', 'sudo -u $SUDO_USER brew install copy-router-config', 'sudo -u $SUDO_USER brew install dmitry', 'sudo -u $SUDO_USER brew install dnmap', 'sudo -u $SUDO_USER brew install dnsenum', 'sudo -u $SUDO_USER brew install dnsmap', 'sudo -u $SUDO_USER brew install dnsrecon', 'sudo -u $SUDO_USER brew install dnstracer', 'sudo -u $SUDO_USER brew install dnswalk', 'sudo -u $SUDO_USER brew install dotdotpwn', 'sudo -u $SUDO_USER brew install enum4linux', 'sudo -u $SUDO_USER brew install enumiax', 'sudo -u $SUDO_USER brew install exploitdb', 'sudo -u $SUDO_USER brew install fierce', 'sudo -u $SUDO_USER brew install firewalk', 'sudo -u $SUDO_USER brew install fragroute', 'sudo -u $SUDO_USER brew install fragrouter', 'sudo -u $SUDO_USER brew install ghost-phisher', 'sudo -u $SUDO_USER brew install golismero', 'sudo -u $SUDO_USER brew install goofile', 'sudo -u $SUDO_USER brew install lbd', 'sudo -u $SUDO_USER brew install maltego-teeth', 'sudo -u $SUDO_USER brew install masscan', 'sudo -u $SUDO_USER brew install metagoofil', 'sudo -u $SUDO_USER brew install miranda', 'sudo -u $SUDO_USER brew install nmap', 'sudo -u $SUDO_USER brew install p0f', 'sudo -u $SUDO_USER brew install parsero', 'sudo -u $SUDO_USER brew install recon-ng', 'sudo -u $SUDO_USER brew install set', 'sudo -u $SUDO_USER brew install smtp-user-enum', 'sudo -u $SUDO_USER brew install snmpcheck', 'sudo -u $SUDO_USER brew install sslcaudit', 'sudo -u $SUDO_USER brew install sslsplit', 'sudo -u $SUDO_USER brew install sslstrip', 'sudo -u $SUDO_USER brew install sslyze', 'sudo -u $SUDO_USER brew install thc-ipv6', 'sudo -u $SUDO_USER brew install theharvester', 'sudo -u $SUDO_USER brew install tlssled', 'sudo -u $SUDO_USER brew install twofi', 'sudo -u $SUDO_USER brew install urlcrazy', 'sudo -u $SUDO_USER brew install wireshark', 'sudo -u $SUDO_USER brew install wol-e', 'sudo -u $SUDO_USER brew install xplico', 'sudo -u $SUDO_USER brew install ismtp', 'sudo -u $SUDO_USER brew install intrace', 'sudo -u $SUDO_USER brew install hping']
array2 = ['sudo -u $SUDO_USER brew install bbqsql', 'sudo -u $SUDO_USER brew install bed', 'sudo -u $SUDO_USER brew install cisco-auditing-tool', 'sudo -u $SUDO_USER brew install cisco-global-exploiter', 'sudo -u $SUDO_USER brew install cisco-ocs', 'sudo -u $SUDO_USER brew install cisco-torch', 'sudo -u $SUDO_USER brew install copy-router-config', 'sudo -u $SUDO_USER brew install doona', 'sudo -u $SUDO_USER brew install dotdotpwn', 'sudo -u $SUDO_USER brew install greenbone-security-assistant', 'sudo -u $SUDO_USER brew install hexorbase', 'sudo -u $SUDO_USER brew install jsql', 'sudo -u $SUDO_USER brew install lynis', 'sudo -u $SUDO_USER brew install nmap', 'sudo -u $SUDO_USER brew install ohrwurm', 'sudo -u $SUDO_USER brew install openvas-administrator', 'sudo -u $SUDO_USER brew install openvas-cli', 'sudo -u $SUDO_USER brew install openvas-manager', 'sudo -u $SUDO_USER brew install openvas-scanner', 'sudo -u $SUDO_USER brew install oscanner', 'sudo -u $SUDO_USER brew install powerfuzzer', 'sudo -u $SUDO_USER brew install sfuzz', 'sudo -u $SUDO_USER brew install sidguesser', 'sudo -u $SUDO_USER brew install siparmyknife', 'sudo -u $SUDO_USER brew install sqlmap', 'sudo -u $SUDO_USER brew install sqlninja', 'sudo -u $SUDO_USER brew install sqlsus', 'sudo -u $SUDO_USER brew install thc-ipv6', 'sudo -u $SUDO_USER brew install tnscmd10g', 'sudo -u $SUDO_USER brew install unix-privesc-check', 'sudo -u $SUDO_USER brew install yersinia']
array3 = ['sudo -u $SUDO_USER brew install aircrack-ng', 'sudo -u $SUDO_USER brew install asleap', 'sudo -u $SUDO_USER brew install bluelog', 'sudo -u $SUDO_USER brew install blueranger', 'sudo -u $SUDO_USER brew install bluesnarfer', 'sudo -u $SUDO_USER brew install bully', 'sudo -u $SUDO_USER brew install cowpatty', 'sudo -u $SUDO_USER brew install crackle', 'sudo -u $SUDO_USER brew install eapmd5pass', 'sudo -u $SUDO_USER brew install fern-wifi-cracker', 'sudo -u $SUDO_USER brew install ghost-phisher', 'sudo -u $SUDO_USER brew install giskismet', 'sudo -u $SUDO_USER brew install kalibrate-rtl', 'sudo -u $SUDO_USER brew install killerbee', 'sudo -u $SUDO_USER brew install kismet', 'sudo -u $SUDO_USER brew install mdk3', 'sudo -u $SUDO_USER brew install mfcuk', 'sudo -u $SUDO_USER brew install mfoc', 'sudo -u $SUDO_USER brew install mfterm', 'sudo -u $SUDO_USER brew install multimon-ng', 'sudo -u $SUDO_USER brew install pixiewps', 'sudo -u $SUDO_USER brew install reaver', 'sudo -u $SUDO_USER brew install redfang', 'sudo -u $SUDO_USER brew install rtlsdr-scanner', 'sudo -u $SUDO_USER brew install spooftooph', 'sudo -u $SUDO_USER brew install wifi-honey', 'sudo -u $SUDO_USER brew install wifitap', 'sudo -u $SUDO_USER brew install wifite']
array4 = ['sudo -u $SUDO_USER brew install apache-users', 'sudo -u $SUDO_USER brew install arachni', 'sudo -u $SUDO_USER brew install bbqsql', 'sudo -u $SUDO_USER brew install blindelephant', 'sudo -u $SUDO_USER brew install burpsuite', 'sudo -u $SUDO_USER brew install cutycapt', 'sudo -u $SUDO_USER brew install davtest', 'sudo -u $SUDO_USER brew install deblaze', 'sudo -u $SUDO_USER brew install dirb', 'sudo -u $SUDO_USER brew install dirbuster', 'sudo -u $SUDO_USER brew install fimap', 'sudo -u $SUDO_USER brew install funkload', 'sudo -u $SUDO_USER brew install grabber', 'sudo -u $SUDO_USER brew install jboss-autopwn', 'sudo -u $SUDO_USER brew install joomscan', 'sudo -u $SUDO_USER brew install jsql', 'sudo -u $SUDO_USER brew install maltego-teeth', 'sudo -u $SUDO_USER brew install padbuster', 'sudo -u $SUDO_USER brew install paros', 'sudo -u $SUDO_USER brew install parsero', 'sudo -u $SUDO_USER brew install plecost', 'sudo -u $SUDO_USER brew install powerfuzzer', 'sudo -u $SUDO_USER brew install proxystrike', 'sudo -u $SUDO_USER brew install recon-ng', 'sudo -u $SUDO_USER brew install skipfish', 'sudo -u $SUDO_USER brew install sqlmap', 'sudo -u $SUDO_USER brew install sqlninja', 'sudo -u $SUDO_USER brew install sqlsus', 'sudo -u $SUDO_USER brew install ua-tester', 'sudo -u $SUDO_USER brew install uniscan', 'sudo -u $SUDO_USER brew install vega', 'sudo -u $SUDO_USER brew install w3af', 'sudo -u $SUDO_USER brew install webscarab', 'sudo -u $SUDO_USER brew install websploit', 'sudo -u $SUDO_USER brew install wfuzz', 'sudo -u $SUDO_USER brew install wpscan', 'sudo -u $SUDO_USER brew install xsser', 'sudo -u $SUDO_USER brew install zaproxy']
array5 = ['sudo -u $SUDO_USER brew install burpsuite', 'sudo -u $SUDO_USER brew install dnschef', 'sudo -u $SUDO_USER brew install fiked', 'sudo -u $SUDO_USER brew install hamster-sidejack', 'sudo -u $SUDO_USER brew install hexinject', 'sudo -u $SUDO_USER brew install iaxflood', 'sudo -u $SUDO_USER brew install inviteflood', 'sudo -u $SUDO_USER brew install ismtp', 'sudo -u $SUDO_USER brew install mitmproxy', 'sudo -u $SUDO_USER brew install ohrwurm', 'sudo -u $SUDO_USER brew install protos-sip', 'sudo -u $SUDO_USER brew install rebind', 'sudo -u $SUDO_USER brew install responder', 'sudo -u $SUDO_USER brew install rtpbreak', 'sudo -u $SUDO_USER brew install rtpinsertsound', 'sudo -u $SUDO_USER brew install rtpmixsound', 'sudo -u $SUDO_USER brew install sctpscan', 'sudo -u $SUDO_USER brew install siparmyknife', 'sudo -u $SUDO_USER brew install sipp', 'sudo -u $SUDO_USER brew install sipvicious', 'sudo -u $SUDO_USER brew install sniffjoke', 'sudo -u $SUDO_USER brew install sslsplit', 'sudo -u $SUDO_USER brew install sslstrip', 'sudo -u $SUDO_USER brew install thc-ipv6', 'sudo -u $SUDO_USER brew install voiphopper', 'sudo -u $SUDO_USER brew install webscarab', 'sudo -u $SUDO_USER brew install wifi-honey', 'sudo -u $SUDO_USER brew install wireshark', 'sudo -u $SUDO_USER brew install xspy', 'sudo -u $SUDO_USER brew install yersinia', 'sudo -u $SUDO_USER brew install zaproxy']
array6 = ['sudo -u $SUDO_USER brew install cryptcat', 'sudo -u $SUDO_USER brew install cymothoa', 'sudo -u $SUDO_USER brew install dbd', 'sudo -u $SUDO_USER brew install dns2tcp', 'sudo -u $SUDO_USER brew install http-tunnel', 'sudo -u $SUDO_USER brew install httptunnel', 'sudo -u $SUDO_USER brew install intersect', 'sudo -u $SUDO_USER brew install nishang', 'sudo -u $SUDO_USER brew install polenum', 'sudo -u $SUDO_USER brew install powersploit', 'sudo -u $SUDO_USER brew install pwnat', 'sudo -u $SUDO_USER brew install ridenum', 'sudo -u $SUDO_USER brew install sbd', 'sudo -u $SUDO_USER brew install u3-pwn', 'sudo -u $SUDO_USER brew install webshells', 'sudo -u $SUDO_USER brew install weevely']
array7 = ['sudo -u $SUDO_USER brew install casefile', 'sudo -u $SUDO_USER brew install cutycapt', 'sudo -u $SUDO_USER brew install dos2unix', 'sudo -u $SUDO_USER brew install dradis', 'sudo -u $SUDO_USER brew install keepnote', 'sudo -u $SUDO_USER brew install magictree', 'sudo -u $SUDO_USER brew install metagoofil', 'sudo -u $SUDO_USER brew install nipper-ng', 'sudo -u $SUDO_USER brew install pipal']
array8 = ['sudo -u $SUDO_USER brew install armitage', 'sudo -u $SUDO_USER brew install backdoor-factory', 'sudo -u $SUDO_USER brew install beef-xss', 'sudo -u $SUDO_USER brew install cisco-auditing-tool', 'sudo -u $SUDO_USER brew install cisco-global-exploiter', 'sudo -u $SUDO_USER brew install cisco-ocs', 'sudo -u $SUDO_USER brew install cisco-torch', 'sudo -u $SUDO_USER brew install crackle', 'sudo -u $SUDO_USER brew install jboss-autopwn', 'sudo -u $SUDO_USER brew install linux-exploit-suggester', 'sudo -u $SUDO_USER brew install maltego-teeth', 'sudo -u $SUDO_USER brew install set', 'sudo -u $SUDO_USER brew install shellnoob', 'sudo -u $SUDO_USER brew install sqlmap', 'sudo -u $SUDO_USER brew install thc-ipv6', 'sudo -u $SUDO_USER brew install yersinia']
array9 = ['sudo -u $SUDO_USER brew install binwalk', 'sudo -u $SUDO_USER brew install bulk-extractor', 'sudo -u $SUDO_USER brew install chntpw', 'sudo -u $SUDO_USER brew install cuckoo', 'sudo -u $SUDO_USER brew install dc3dd', 'sudo -u $SUDO_USER brew install ddrescue', 'sudo -u $SUDO_USER brew install dumpzilla', 'sudo -u $SUDO_USER brew install extundelete', 'sudo -u $SUDO_USER brew install foremost', 'sudo -u $SUDO_USER brew install galleta', 'sudo -u $SUDO_USER brew install guymager', 'sudo -u $SUDO_USER brew install iphone-backup-analyzer', 'sudo -u $SUDO_USER brew install p0f', 'sudo -u $SUDO_USER brew install pdf-parser', 'sudo -u $SUDO_USER brew install pdfid', 'sudo -u $SUDO_USER brew install pdgmail', 'sudo -u $SUDO_USER brew install peepdf', 'sudo -u $SUDO_USER brew install volatility', 'sudo -u $SUDO_USER brew install xplico']
array10 = ['sudo -u $SUDO_USER brew install dhcpig', 'sudo -u $SUDO_USER brew install funkload', 'sudo -u $SUDO_USER brew install iaxflood', 'sudo -u $SUDO_USER brew install inviteflood', 'sudo -u $SUDO_USER brew install ipv6-toolkit', 'sudo -u $SUDO_USER brew install mdk3', 'sudo -u $SUDO_USER brew install reaver', 'sudo -u $SUDO_USER brew install rtpflood', 'sudo -u $SUDO_USER brew install slowhttptest', 'sudo -u $SUDO_USER brew install t50', 'sudo -u $SUDO_USER brew install termineter', 'sudo -u $SUDO_USER brew install thc-ipv6', 'sudo -u $SUDO_USER brew install thc-ssl-dos ']
array11 = ['sudo -u $SUDO_USER brew install acccheck', 'sudo -u $SUDO_USER brew install burpsuite', 'sudo -u $SUDO_USER brew install cewl', 'sudo -u $SUDO_USER brew install chntpw', 'sudo -u $SUDO_USER brew install cisco-auditing-tool', 'sudo -u $SUDO_USER brew install cmospwd', 'sudo -u $SUDO_USER brew install creddump', 'sudo -u $SUDO_USER brew install crunch', 'sudo -u $SUDO_USER brew install findmyhash', 'sudo -u $SUDO_USER brew install gpp-decrypt', 'sudo -u $SUDO_USER brew install hash-identifier', 'sudo -u $SUDO_USER brew install hexorbase', 'sudo -u $SUDO_USER brew install john', 'sudo -u $SUDO_USER brew install johnny', 'sudo -u $SUDO_USER brew install keimpx', 'sudo -u $SUDO_USER brew install maltego-teeth', 'sudo -u $SUDO_USER brew install maskprocessor', 'sudo -u $SUDO_USER brew install multiforcer', 'sudo -u $SUDO_USER brew install ncrack', 'sudo -u $SUDO_USER brew install oclgausscrack', 'sudo -u $SUDO_USER brew install pack', 'sudo -u $SUDO_USER brew install patator', 'sudo -u $SUDO_USER brew install polenum', 'sudo -u $SUDO_USER brew install rainbowcrack', 'sudo -u $SUDO_USER brew install rcracki-mt', 'sudo -u $SUDO_USER brew install rsmangler', 'sudo -u $SUDO_USER brew install statsprocessor', 'sudo -u $SUDO_USER brew install thc-pptp-bruter', 'sudo -u $SUDO_USER brew install truecrack', 'sudo -u $SUDO_USER brew install webscarab', 'sudo -u $SUDO_USER brew install wordlists', 'sudo -u $SUDO_USER brew install zaproxy']
array12 = ['sudo -u $SUDO_USER brew install apktool', 'sudo -u $SUDO_USER brew install dex2jar', 'sudo -u $SUDO_USER brew install python-diStorm3', 'sudo -u $SUDO_USER brew install edb-debugger', 'sudo -u $SUDO_USER brew install jad', 'sudo -u $SUDO_USER brew install javasnoop', 'sudo -u $SUDO_USER brew install JD', 'sudo -u $SUDO_USER brew install OllyDbg', 'sudo -u $SUDO_USER brew install smali', 'sudo -u $SUDO_USER brew install Valgrind', 'sudo -u $SUDO_USER brew install YARA']
array13 = ['sudo -u $SUDO_USER brew install android-sdk', 'sudo -u $SUDO_USER brew install apktool', 'sudo -u $SUDO_USER brew install arduino', 'sudo -u $SUDO_USER brew install dex2jar', 'sudo -u $SUDO_USER brew install sakis3g', 'sudo -u $SUDO_USER brew install smali']
array14 = ['sudo -u $SUDO_USER brew install squid3']




def main():
        print ('''

 oooo    oooo           oooo   o8o        .o   ooo        ooooo                     
`888   .8P'            `888   `"'      .d88   `88.       .888'                     
 888  d8'     .oooo.    888  oooo    .d'888    888b     d'888   .oooo.    .ooooo.  
 88888[      `P  )88b   888  `888  .d'  888    8 Y88. .P  888  `P  )88b  d88' `"Y8 
 888`88b.     .oP"888   888   888  88ooo888oo  8  `888'   888   .oP"888  888       
 888  `88b.  d8(  888   888   888       888    8    Y     888  d8(  888  888   .o8 
o888o  Scott `Garcia8o o888o o888o     o888o  o8o        o888o `Y888""8o `Y8bod8P' 

 \033[1;32m+ -- -- +=[ Author: Scott Garcia | Github: https://github.com/scottdgarciajr[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m


\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid potential issues .\033[1;m
		''')
        
        disp()

def disp():
    while True:
        print('''
1) Add All Kali repositories
2) View Categories
3) Help

        ''')
        choice = input("\033[1;36mkali4mac > \033[1;m")
        if choice == "1":  # add kali repo
            installAll()
        elif choice == "2":  # view categories
            showCategories()
        elif choice == "3":
            print('''
****************** +Commands+ ******************

\033[1;32mback\033[1;m     \033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m   \033[1;33mGo to the main menu\033[1;m
            ''')
        elif choice == "back":
            disp()
        elif choice == "gohome":
            disp()
        else:
            print("\033[1;31mSorry, that was an invalid command!\033[1;m")

                                            
def printArray(tools):
    # Create a 2D array with 2 columns and the required number of rows
    num_rows = (len(tools) + 1) // 2
    tool_array = [[None for _ in range(2)] for _ in range(num_rows)]

    # Fill the 2D array with the tools
    for i in range(len(tools)):
        row = i // 2
        col = i % 2
        tool_name = tools[i].split()[-1].replace("sudo -u $SUDO_USER brew install ", "")
        tool_array[row][col] = f"{i+1}) {tools[i].split()[-1]:<30}" if tools[i] is not None else ""

    # Print the 2D array
    for row in tool_array:
        print("".join(row))
        

def disp1():
    print("\033[1;36m=+[ Information Gathering\033[1;m\n")
    printArray(array1)
    print("\n0) Install all Information Gathering tools")   

    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    print()
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array1)
    elif int(choice) >= 0 and int(choice) <= len(array1):
        runCommand(array1, int(choice))





def disp2():
    print ("\033[1;36m=+[ Vulnerability Analysis\033[1;m")

    printArray(array2)
    
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array2)
    elif int(choice) >= 0 and int(choice) <= len(array2):
        runCommand(array2, int(choice))






def disp3():
    print("\033[1;36m=+[ Wireless Attacks\033[1;m\n")
    printArray(array3)
    print("\n0) Install all Wireless Attack tools")   

    
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array3)
    elif int(choice) >= 0 and int(choice) <= len(array3):
        runCommand(array3, int(choice))





def disp4():
    print("\033[1;36m=+[ Web Application\033[1;m\n")
    printArray(array4)
    print("\n0) Install all Web Application tools")   

    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array4)
    elif int(choice) >= 0 and int(choice) <= len(array4):
        runCommand(array4, int(choice))




def disp5():
    print("\033[1;36m=+[ Sniffing & Spoofing\033[1;m\n")
    printArray(array5)
    print("\n0) Install all Sniffing & Spoofing")   

						
    
    						
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array5)
    elif int(choice) >= 0 and int(choice) <= len(array5):
        runCommand(array5, int(choice))







def disp6():
    print("\033[1;36m=+[ Sniffing & Spoofing\033[1;m\n")
    printArray(array6)
    print("\n0) Install all Sniffing & Spoofing") 

    				
    
    
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array6)
    elif int(choice) >= 0 and int(choice) <= len(array6):
        runCommand(array6, int(choice))

def disp7():
    print("\033[1;36m=+[ Reporting Tools\033[1;m\n")
    printArray(array7)
    print("\n0) Install all Reporting Tools") 
    					
    						
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array7)
    elif int(choice) >= 0 and int(choice) <= len(array7):
        runCommand(array7, int(choice))


def disp8():
    print("\033[1;36m=+[ Exploitation Tools\033[1;m\n")
    printArray(array8)
    print("\n0) Install all Exploitation Tools") 
    				
     						
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array8)
    elif int(choice) >= 0 and int(choice) <= len(array8):
        runCommand(array8, int(choice))

def disp9():
    print("\033[1;36m=+[ Forensics Tools\033[1;m\n")
    printArray(array9)
    print("\n0) Install all Forensics Tools") 
    				
    						
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array9)
    elif int(choice) >= 0 and int(choice) <= len(array9):
        runCommand(array9, int(choice))

def disp10():
    print("\033[1;36m=+[ Stress Testing\033[1;m\n")
    printArray(array5)
    print("\n0) Install all Stress Testing") 
    		
    						
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array10)
    elif int(choice) >= 0 and int(choice) <= len(array10):
        runCommand(array10, int(choice))

def disp11():
    print("\033[1;36m=+[ Password Attacks\033[1;m\n")
    printArray(array11)
    print("\n0) Install all Password Attacks") 
						
    				
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array11)
    elif int(choice) >= 0 and int(choice) <= len(array11):
        runCommand(array11, int(choice))

def disp12():
    print("\033[1;36m=+[ Reverse Engineering\033[1;m\n")
    printArray(array12)
    print("\n0) Install all Reverse Engineering") 
						
    				
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array12)
    elif int(choice) >= 0 and int(choice) <= len(array12):
        runCommand(array12, int(choice))

def disp13():
    print("\033[1;36m=+[ Hardware Hacking\033[1;m\n")
    printArray(array13)
    print("\n0) Install all hardware hacking") 
    				
    						
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array13)
    elif int(choice) >= 0 and int(choice) <= len(array13):
        runCommand(array13, int(choice))

def disp14():
    print("\033[1;36m=+[ Extra\033[1;m\n")
    printArray(array14)
    print("\n0) Install all Extra") 
    				
    						
    print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
    
    choice = input("\033[1;36mkali4mac > \033[1;m")
    
    if choice == "back":
        showCategories()
    elif choice == "gohome":
        disp()
    elif choice == "0":
        runCommands(array14)
    elif int(choice) >= 0 and int(choice) <= len(array14):
        runCommand(array14, int(choice))



							
def runCommands(commands): #run commands in an array
    for command in commands:
        os.system(command)

def runCommand(commands, index):
    if index == 0:
        installAll()
    elif index > 0 and index <= len(commands):
        command = commands[index - 1]
        os.system(command)
    else:
        print("Invalid index number")
def installAll():
    for i in range(1, 15):
        array_name = "array" + str(i)
        if array_name in globals():
            commands = globals()[array_name]
            runCommands(commands)
        else:
            print("Array", i, "not found")
        
def showCategories():
    categories = {
        "1": disp1,
        "2": disp2,
        "3": disp3,
        "4": disp4,
        "5": disp5,
        "6": disp6,
        "7": disp7,
        "8": disp8,
        "9": disp9,
        "10": disp10,
        "11": disp11,
        "12": disp12,
        "13": disp13,
        "14": disp14,
        "0": installAll
    }

    print('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

			 ''')
    print("\033[1;32mSelect a category or press (0) to install all Kali linux tools.\n\033[1;m")

    choice1 = input("\033[1;36mkali4mac > \033[1;m")
    if choice1 == "back" or choice1 == "gohome":
        disp1()
    else:
        disp_func = categories.get(choice1)
        if disp_func:
            disp_func()
        else:
            print("\033[1;31mInvalid choice. Please try again.\033[1;m")
            showCategories()



    

if os.getuid() != 0: #making sure that the program is run with super user priveledges
    print ("Sorry. This script requires sudo privledges")
    sys.exit()
else:
    main()
