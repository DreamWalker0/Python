#Author: Jorge Guzman Nader
#Date: 5/21/2019
#Description: This program creates a list with all possible combinations of avecotr elements
#Sample output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x = int(input("Input X: "))
y = int(input("Input Y: "))
z = int(input("Input Z: "))
n = int(input("Input N: "))


print ([[i,j,k] for i in range(0,x+1)
                for j in range(0,y+1)
                for k in range(0,z+1)
                if i + j + k != n ])



input("Click any key to close ") #use to prevent scrip to close
