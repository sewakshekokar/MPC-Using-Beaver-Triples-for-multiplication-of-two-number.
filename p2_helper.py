import socket, json, random

HOST = '127.0.0.1'
PORT_P0 = 6000
PORT_P1 = 6001

# Beaver triple
a = 6
b = 3
c = a * b

# Shares of P0 and P1
a0, a1 = 3, 3
b0, b1 = 2, 1
c0, c1 = 10, 8

def send_json(conn, obj):
    conn.sendall(json.dumps(obj).encode())

print(f"[P2] Beaver triple: a={a}, b={b}, c={c}")

# Send to P0
s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s0.connect((HOST, PORT_P0))
send_json(s0, {'a0': a0, 'b0': b0, 'c0': c0})
s0.close()

# Send to P1
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((HOST, PORT_P1))
send_json(s1, {'a1': a1, 'b1': b1, 'c1': c1})
s1.close()
