# coding=utf-8
import paramiko

from SSHConnection import SSHConnection
from Host import Host

if __name__ == "__main__":
    host = Host('192.168.1.1', '22', 'root', '1234', 'df -h', None)

    # 循环登录host并执行对应代码
    conn = SSHConnection(host.ip, host.port, host.username, host.password)
    conn.connect()
    conn.exec_command(host.cmd)
    conn.close()
