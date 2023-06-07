# Đề 3
'''
Câu 1: Mô tả phương thức truyền dữ liệu theo giao thức TCP
Câu 2: Viết chương trình đọc header của 1 trang web
Câu 3: Xây dựng chương trình theo mô hình Client-Server sử dụng
    socket theo giao thức TCP và thực hiện các công việc sau:
    a, Client: gửi tín hiệu kết nối đến Server
    - Gửi lệnh Max(hoặc Min) và hai số nguyên a, b, đến Server
    - Nhận kết quả trả về
    b, Server: Chấp nhận kết nối
    - Hiển thị thông tin Client
    - Kiểm tra xem lệnh nhận được là lệnh gì? (Max/Min)
    - Nhận 2 số nguyên từ Client
    - Thực hiện tìm Max/Min
    - Trả về kết quả cho Client
'''
#=============================================================================
# Câu 1:

#=============================================================================
# Câu 2:
import requests

url = 'https://facebook.com'
# Tạo yêu cầu
respone = requests.get(url)
# Lấy header từ respone, header là 1 dictionary
header = respone.headers

# In
for key, value in header.items():
    print(f'{key}: {value}')
    print()
#=============================================================================
# Câu 3:
                        # -----SERVER-----
import socket

host='localhost'
port = 9050

def create_connect(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host, port))
    sk.listen(5)
    return sk

def create_data(mes):
    data = mes + '\0'
    return data

def send_data(sk, mes):
    message = create_data(mes)
    sk.sendall(message.encode('utf-8'))

def recv_data(sk):
    data = bytearray()
    msg = ''
    while not msg:
        data1 = sk.recv(1024)
        if not data1:
            raise ConnectionError()
        data = data+data1
        if b'\0' in data1:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

if __name__=='__main__':
    sk = create_connect(host, port)
    client_sk, client_addr = sk.accept()
    print(f'Dia chi client: {client_addr}')
    while True:
        # Nhan 1:
        data = recv_data(client_sk)
        print('Client: %s'%data)
        if data=='bye':
            client_sk.close()
            break
        # Gui 2
        lenh, a, b = data.split('|')
        result = ''
        if lenh.upper() == 'MAX':
            maxx = max(int(a), int(b))
            result = f'Max({a}, {b}) = {maxx}'
        else:
            minn = min(int(a), int(b))
            result = f'Min({a}, {b}) = {minn}'
        send_data(client_sk, result)
        print('Server: %s'%result)

                        # -----CLIENT-----
# import socket

# host='localhost'
# port = 9050

# def send_data(sk, mes):
#     # Tao data:
#     data = mes+'\0'
#     sk.sendall(data.encode('utf-8'))

# def recv_data(sk):
#     data = bytearray()
#     msg = ''
#     while not msg:
#         data1 = sk.recv(1024)
#         if not data1: raise ConnectionError()
#         data = data + data1
#         if b'\0' in data1:
#             msg = data.rstrip(b'\0')
#     return msg.decode('utf-8')

# if __name__=='__main__':
#     sk=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sk.connect((host, port))
    
#     while True:
#         # Gui 1
#         data = input('Nhap lenh|a|b:')
#         send_data(sk, data)
#         if data =='bye':
#             sk.close()
#             break
#         print(f'Client: {data}')
#         #Nhan 2
#         data = recv_data(sk)
#         print("Server: %s"%data)