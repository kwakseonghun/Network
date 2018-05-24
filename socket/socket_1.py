import socket
from binascii import hexlify
from time import ctime
from pack import ntplib
class host:
    def __init__(self):
        pass
    #host와 ip출력
    def myhostnameandip(self):
        host_name= socket.gethostname()
        print(host_name)
        print(socket.gethostbyname(host_name))
    #외부 host
    def otherhost(self):
        remote_host='www.github.com'
        try:
            print(remote_host,socket.gethostbyname(remote_host))
        except socket.error as e:
            print(remote_host,e)
    #ip 주소 형변환
    def ip4to16(self):
        for ip_addr in ['192.30.255.112']:
            packed_ip=socket.inet_aton(ip_addr)
            unpacked_ip=socket.inet_ntoa(packed_ip)
            print(hexlify(packed_ip),unpacked_ip)
    #ntp 서버의 시간
    def hosttime(self):
        ntp_client=ntplib.NTPClient()
        response=ntp_client.request('pool.ntp.org')
        print(ctime(response.tx_time))






