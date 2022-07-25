import socket
target = input('Ingresa la IP: ')
rangopuertos = input('ingresa el rango de puertos a escanear(0-65000): ')

lowport = int(rangopuertos.split('-')[0])
highport = int(rangopuertos.split('-')[1])

print('Scaneando puertos en host ', target, ' desde ',lowport, ' hasta ', highport )

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print('*** Puerto', port,'- ABIERTO ***')
    # else:
       # print('Puerto', port,'-- CERRADO')
    s.close()
