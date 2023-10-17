#Author: Jorge Guzman Nader
#Date: 12/17/2019
#Info: This program match compatible donor and receiver blood types

bType = ['AB+','AB-','A+','A-','B+','B-','O+','O-']

def abo(): #Blood type function
    print("Enter a Blood Type in uppercase ex. A+: ")
    bUser = input()

    if(bUser==bType[0]):#AB+
        print('You can donate blood to:\n' +  str(bType[0]))
        print('\nYou can receive blood from:\n' + str(bType[0:8])) # needs to be type str
    elif(bUser==bType[1]):#AB-
        print('You can donate blood to:\n' +  str(bType[0:2]))
        print('\nYou can receive blood from:\n' + str(bType[1:8:2]))
    elif(bUser==bType[2]):#A+
        print('You can donate blood to:\n' +  str(bType[0:3:2]))
        print('\nYou can receive blood from:\n' + str(bType[2:4]+ bType[6:8])) 
    elif(bUser==bType[3]):#A-
        print('You can donate blood to:\n' +  str(bType[0:4]))
        print('\nYou can receive blood from:\n' + str(bType[3:8:4]))  
    elif(bUser==bType[4]):#B+
        print('You can donate blood to:\n' +  str(bType[0:5:4]))
        print('\nYou can receive blood from:\n' + str(bType[4:8]))  
    elif(bUser==bType[5]):#B-
        print('You can donate blood to:\n' +  str(bType[0:2]+ bType[4:6]))
        print('\nYou can receive blood from:\n' + str(bType[5:8:2])) 
    elif(bUser==bType[6]):#O+
        print('You can donate blood to:\n' +  str(bType[0:8:2]))
        print('\nYou can receive blood from:\n' + str(bType[6:8])) 
    elif(bUser==bType[7]):#O-
        print('You can donate blood to:\n' +  str(bType[0:8]))
        print('\nYou can receive blood from:\n' + str(bType[7]))
    else:
        print('\nINVALID BLOOD TYPE, please try again.\n') 
        abo()
    

#Call site
abo()
input("\nClick enter to close ") #use to prevent scrip to close