# coding=utf-8
import xlrd

from Host import Host
from SSHConnection import SSHConnection

if __name__ == "__main__":

    # 主机列表
    host_list = []

    # 批量读取主机列表
    workbook = xlrd.open_workbook("host.xls")
    sheet = workbook.sheet_by_index(0)
    for i in range(sheet.nrows-1):
        ip = sheet.cell(i+1, 0)
        port = sheet.cell(i+1, 1)
        username = sheet.cell(i+1, 2)
        password = sheet.cell(i+1, 3)
        cmd = sheet.cell(i+1, 4)
        re = sheet.cell(i+1, 5)
        host = Host(ip, port, username, password, cmd, None)
        host_list.append(host)

    # 循环登录host并执行对应代码
    for i in range(len(host_list)):
        conn = SSHConnection(host)
        conn.connect()
        data = conn.exec_command(host.cmd)
        conn.close()
        print data
