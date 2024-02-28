import socket
import sys


if len(sys.argv) < 3:
    print("""How to use:
    python smtp.py <IP> <PORT> <WORDLIST>""")

host = sys.argv[1]
porta = sys.argv[2]
wordlist = sys.argv[3]


with open(wordlist, 'r') as usernames:
    ola = usernames.readlines()

for usuario in ola:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,int(porta)))
    
    s.recv(2048)
    
    conteudo = f"VRFY {usuario.strip()}\r\n"
    
    s.send(conteudo.encode())    
    
    conteudo = s.recv(2048)
    
    busca = "252 2.0.0"
    index = conteudo.find(busca.encode())

    if index != -1:
        print(f"Found {conteudo.decode()}")
        
        
        s.close()

