import socket

def tcp_header(data):
  storeobj=struct.unpack('!HHLLBBHHH',data)
  _source_port =storeobj[0] 
  _destination_port  =storeobj[1]
  _sequence_number  =storeobj[2]
  _acknowledge_number  =storeobj[3]
  _offset_reserved  =storeobj[4]
  _tcp_flag  =storeobj[5]
  _window  =storeobj[6]
  _checksum  =storeobj[7]
  _urgent_pointer =storeobj[8]
  data={"Source Port":_source_port,
  "Destination Port":_destination_port,
  "Sequence Number":_sequence_number,
  "Acknowledge Number":_acknowledge_number,
  "Offset & Reserved":_offset_reserved,
  "Tcp Flag":_tcp_flag,
  "Window":_window,
  "CheckSum":_checksum,
  "Urgent Pointer":_urgent_pointer
  }
  return data

port = 3125
localhost = '127.0.0.1'
sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
sniffer.bind((localhost,port))
sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

while True:
    print (tcp_header(sniffer.recvfrom(port)))

sniffer.close()