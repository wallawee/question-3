# Import socket module import socket 
 
 
def Main(): 
    # local host IP '127.0.0.1'   
    host = "10.0.2.6" 
 
    # Define the port on which you want to connect 
    port = 8888 
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
    # connect to server on local computer    
    s.connect((host, port)) 
 
    # message you send to server     
    message = "QOTD Request"    
    for i in range(1): 
 
        # message sent to server 
        s.send(message.encode()) 
 
        # message received from server 
        data = s.recv(1024) 
 
        # print the received message 
        # here it would be a reverse of sent message        
        print("From server : ", str(data.decode("ascii"))) 
 
    s.close() 
 
 
if __name__ == "__main__": 
    Main() 
