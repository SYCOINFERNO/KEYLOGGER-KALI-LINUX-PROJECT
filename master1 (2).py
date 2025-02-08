import time
import sys
import socket
import os

s=socket.socket()
host = ""  #Enter the ip address of the machine in which you are wishing to run this script.
port = 8080
s.bind ((host,port))
print ("")
print ("Waiting for incoming connection.....")
print ("")
s.listen(10)
conn, addr =s.accept()

print("")
print ("Client is connected to the server now....")
print(" ")

while True:
    choice =input("1.Shutdown\n2.Restart\n3.DOS Attack")
    if (choice == "1"):
        cmmd = "shutdown"
        conn.sendall(cmmd.encode())
        print ("Command has been sent succesfully.Waiting for confirmation")
        print ("")
        data =conn.recv(1024)
        if data:
            print ("shutdown command has been received and executed")
            print ("")
            
    elif (choice == "2"):
        command="restart";
        conn.sendall(command.encode())
        print("Command has been sent successfully. Waiting for confirmation")
        print ("")
        data =conn.recv(1024)
        if data:
            print ("Restart command has been received and executed")
            print ("")
            
            
    elif (choice == "3"):
        command="DOS Attack";
        conn.sendall(command.encode())
        print("Command has been sent successfully. Waiting for confirmation")
        print ("")
        data =conn.recv(1024)
        if data:
            print ("DOS Attack command has been received and executed")
            print ("")
    else:
        print("Enter valid choice")
        cmmd=raw_input("1.Shutdown\n2.Restart\n3.DOS Attack")
