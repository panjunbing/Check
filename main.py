# coding=utf-8
import paramiko

from SSHConnection import SSHConnection


if __name__ == "__main__":
    conn = SSHConnection('192.168.1.1', '22', 'root', '1234')
    conn.exec_command('df -h')
    conn.exec_command('free')
    conn.close()

