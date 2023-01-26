# import socket programming library import socket import random 
 
# import thread module from _thread import * import threading 
 
# import array as arr 
 
print_lock = threading.Lock() quote = [ 
  "No one will save you, you save yourself – Gut”,
  “I have life but when in with you I can enjoy it - Amon”,
  “You know what I mean – K”,
  “I save everyone but who save me - Superman”,
  “It is what it is - Me”,
]
] 
host = "" port = 8888 # thread function def threaded(c):    
while True: 
 
        # data received from client       
        data = c.recv(1024)       
        if not data: 
            print("Bye") 
            # lock released on exit            
            print_lock.release() 
            break 
 
        # reverse the given string from client 
        data = quote[random.randint(0, 6)].encode() 
 
        # send back reversed string to client     
        c.send(data) 
 
    # connection closed  
    c.close() 
 
 
def Main(): 
    # reserve a port on your computer 
    # in our case it is 12345 but it    
    # can be anything 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
 
    # put the socket into listening mode    
    s.listen(5) 
    print("socket is listening") 
 
    # a forever loop until client wants to exit    
    while True: 
 
        # establish connection with client        
        c, addr = s.accept() 
 
        # lock acquired by client 
        print_lock.acquire() 
        print("Connected to :", addr[0], ":", addr[1]) 
 
        # Start a new thread and return its identifier        
        
        start_new_thread(threaded, (c,))  
        s.close() 
 
 
if __name__ == "__main__": 
    Main() 
 
