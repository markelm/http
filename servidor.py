#HTTP/1.1 server template
import socket
from datetime import datetime


#array with name that will be posted on the site
visitante = ''

#source code of the webpage hosted in the server
page = f'<!DOCTYPE HTML>\n<html><body><h1>This is THE WEB PAGE</h1><br><form name="name" method="POST">Digite o seu nome:<input type="text" name="your_name"><br><input type="submit" value="Submit"></form><br>Visitante:<br>{visitante}</body></html>\r\n\r\n'

page404 = '<!DOCTYPE HTML>\n<html><body><h1>ERRO 404<br>Pagina nao encontrada</h1></body></html>\r\n\r\n'

#get current time
currentTime = datetime.now()

#formatted date and time
d = currentTime.ctime()
date_array = d.split()
date_formatted = f'Date: {date_array[0]}, {d[4:]} BRT\r\n'

#listening to socket...
serverPort = 8081


#create socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to a specific port
serverSocket.bind(('', serverPort))

#start listening
serverSocket.listen(1)

print("Server HTTP/1.1 Initialized")
print(f'Listening to port {serverPort}')

#loop for receiving clients' requests

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client {} connected to server".format(addr))
    
    #Receives clients' requests
    request = connectionSocket.recv(1024).decode('utf-8')

    #breaks each word in the request
    splitted_request = request.split()
    if splitted_request[0] == "GET":
       # performs action pertaining to the GET command
       params = splitted_request[1]
       if splitted_request[1] == '/' and len(splitted_request) > 4:
           params = splitted_request[4]
       print(splitted_request)
       print("Get type request, searching for {} resource".format(params))
       #assuming the request was successful
       if params == f'localhost:{serverPort}':
           response = "\nHTTP/1.1 200 OK\r\n"
       else:
           response = "\nHTTP/1.1 404\r\n"
       response += 'Transfer-Encoded: chunked\r\n'
       response += date_formatted 
       response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
       if params == f'localhost:{serverPort}':
          response += f'<!DOCTYPE HTML>\n<html><body><h1>This is THE WEB PAGE</h1><br><form name="name" method="POST">Digite o seu nome:<input type="text" name="your_name"><br><input type="submit" value="Submit"></form><br>Visitante:<br><h2>{visitante}</h2></body></html>\r\n\r\n'
       else:
           response += page404
       connectionSocket.send(response.encode())

   
    if splitted_request[0] == "POST":
       # performs action pertaining to the GET command
       params = splitted_request[1]
       if splitted_request[1] == '/' and len(splitted_request) > 4:
           params = splitted_request[4]
       print(splitted_request)
       params2 = splitted_request[-1]
       params_post = params2[params2.find('=') + 1:]
       visitante = params_post
       print("Post type request, posting to {}".format(params))
       #assuming the request was successful
       if params == f'localhost:{serverPort}':
           response = "\nHTTP/1.1 200 OK\r\n"
       else:
           response = "\nHTTP/1.1 404\r\n"
       response += date_formatted 
       response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
       if params == f'localhost:{serverPort}':
           response += f'<!DOCTYPE HTML>\n<html><body><h1>This is THE WEB PAGE</h1><br><form name="name" method="POST">Digite o seu nome:<input type="text" name="your_name"><br><input type="submit" value="Submit"></form><br>Visitante:<br><h2>{visitante}</h2></body></html>\r\n\r\n'
       else:
           response += page404
       connectionSocket.send(response.encode())

    if splitted_request[0] == "OPTIONS":
       # performs action pertaining to the GET command
       params = splitted_request[2]
       print(splitted_request)
       if splitted_request[2] == 'HTTP/1.1': 
           response = "\nHTTP/1.1 200 OK\r\n"
           response += 'Transfer-Encoded: chunked\r\n'
           response += date_formatted
           response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
           response += f"GET function:\n\tGET localhost:{serverPort}\nOPTIONS function:\n\tOPTIONS / HTTP/1.1\nHEAD function:\n\tHEAD / HTTP/1.1\nPOST function:\n\t*Available only through browser\r\n\r\n"
       connectionSocket.send(response.encode())
   
    if splitted_request[0] == "HEAD":
       # performs action pertaining to the HEAD command
       params = splitted_request[2]
       print(splitted_request)
       if splitted_request[2] == 'HTTP/1.1': 
           response = "\nHTTP/1.1 200 OK\r\n"
           response += 'Transfer-Encoded: chunked\r\n'
           response += date_formatted
           response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
       connectionSocket.send(response.encode())


    connectionSocket.close()

