#!/usr/bin/env python3

#above is the shebang line, which specifies the location of the python interpreter on the system.

#subprocess is used to run shell commands
import subprocess
#socket is used to communicate with network connections
import socket 
#os is used to communicate with system related operations
import os

#this is used to clear the terminal when a program is run.
os.system('clear')

#print functions to show the user the prompt they will input into.
print("")
print("")
print("Script written by: Mina Ramez Farag")
print("")
print("       **************************************")
print("       *******PING TEST TROUBLESHOOTER*******")
print("       **************************************")
print("")
print("Enter Selection:")
print("")
print("       1 - Test connectivity to your gateway.")
print("       2 - Test for remote connectivity.")
print("       3 - Test for DNS resolution.")
print("       4 - Display gateway IP address.")
print("")


#defining a function to check the gateway connection using the gateway address of pfsense and port 80, which will try to connect to the socket 
#or else print to the user that the connection could not be established
def gateway_connection():
    gateway_address= '192.168.1.254'
    gateway_port= 80
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.settimeout(5)
            result = connection.connect_ex((gateway_address,gateway_port))
            if result == 0:
                print("Successfully connected to the gateway!")
                return True
            else:
                print("Could not connect to the gateway!")
                return False
    except socket.error as error:
        print(f"Socket error: {error}")
        return False




#defining a function to test for remote connections using the google/rit host network 8.8.8.8.
def remote_connection():
    host= "8.8.8.8"
    port= 443

    #function to create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #function to stop the socket at a certain timeframe
    sock.settimeout( 5 )

    try:
        #function to connect to the host and port
        sock.connect((host, port))
    except socket.error as e:
        print(f"Connection to {host}:{port} failed: {e}!")
        return False

    print(f"Successfully connected to {host}:{port}!")
    return True




#defining a function to test for dns resolution using the google host 
def dns_resolution( ):
    hostname= "www.google.com"

    try:
        #function to resolve the hostname into an IP address
        ip_address= socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f"DNS resolution for {hostname} failed: {e}!")
        return False

    print(f"Successfully resolved {hostname} to {ip_address}!")
    return True




#defining a function to pring the gateway for the user which is automatically extracted from the system by grabbing the ip r information of 
#a linux machine, and navigating through the terminal output to the gateway, and only printing the desired information. 
def print_gateway():
    p= subprocess.Popen(["ip r"], stdout=subprocess.PIPE, shell=True)
    out =p.stdout.read( ).decode("utf-8")

    #function to split the entire output into lines. 
    lines=  out.split("\n" )

    #function to loop through the lines to find the gateway
    for line in lines:
        if "default" in line:
            #function to split the lines into fields
            fields = line.split( )
            #function to call the second field as the gateway is in that field
            global gateway_address
            gateway_address = fields[2]
            break
    else:
        print("Default gateway not found!")
        return

    print(f"Default gateway: {gateway_address}!")




#defining a function to run the above codes based on the users choice by calling the function. 
def run_code(user_entry):
    if user_entry == 1:
        gateway_connection()

    elif user_entry == 2:
        remote_connection()
        
    elif user_entry == 3:
        dns_resolution()
        
    elif user_entry == 4:
        print_gateway()
        

while True:
    print("")
    user_input = input("Enter a number from 1 - 4, or 'Q/q' to exit: ")
    if user_input.lower() == 'q':
        break
    try:
        user_entry = int(user_input)
        if user_entry >= 1 and user_entry <= 4:
            run_code(user_entry)
        
        else:
            print("please enter a number from 1 - 4.")
    except ValueError:
        print("please enter a number from 1 - 4")