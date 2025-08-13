import socket, json

HOST = '127.0.0.1'
PORT_P1 = 6001  
PORT_P0 = 6000  

x1 = 4
y1 = 2
print("[P1] x1=",x1)
print("[P1] y1=",y1)

def recv_json(conn):
    return json.loads(conn.recv(1024).decode())

def send_json(conn, obj):
    conn.sendall(json.dumps(obj).encode())

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT_P1))
srv.listen(5)
print("[P1] Listening on", PORT_P1)


# Receive Beaver triple from p2
conn_p2, address = srv.accept()
t = recv_json(conn_p2)
a1 = t['a1']
b1 = t['b1']
c1 = t['c1']
print("[P1] a1,b1,c1 =",a1,b1,c1)
conn_p2.close()

# Compute d1, e1 
d1 = x1 - a1
e1 = y1 - b1
print("[P1] d1,e1 =", d1, e1)

# Receive d0,e0 from P0 
conn_p0, address = srv.accept()
de_rev = recv_json(conn_p0)
d0 = de_rev['d0']
e0 = de_rev['e0']


# send d1 and e1 to p0
send_json(conn_p0, {'d1': d1, 'e1': e1})
conn_p0.close()

# Compute d,e
d = d0 + d1
e = e0 + e1

z1 = c1 + d * b1 + e * a1  

print("[P1] z1 =", z1)

srv.close()
