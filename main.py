# coding=utf-8
import xlrd

from Host import Host
from SSHConnection import SSHConnection

if __name__ == "__main__":

    # 主机列表
    host_list = []

    data_list = []

    # 批量读取主机列表
    workbook = xlrd.open_workbook("host.xls")
    sheet = workbook.sheet_by_index(0)
    for i in range(sheet.nrows-1):
        ip = sheet.cell(i+1, 0).value.encode('utf-8')
        port = int(sheet.cell(i+1, 1).value)
        username = sheet.cell(i+1, 2).value.encode('utf-8')
        password = ""
        if sheet.cell(i+1, 3).ctype == 1:
            password = sheet.cell(i+1, 3).value
        elif sheet.cell(i+1, 3).ctype == 2:
            password = str(int(sheet.cell(i + 1, 3).value))
        cmd = sheet.cell(i+1, 4).value.encode('utf-8')
        re = sheet.cell(i+1, 5).value.encode('utf-8')
        host = Host(ip, port, username, password, cmd, None)
        host_list.append(host)

    # 循环登录host并执行对应代码
    for i in range(len(host_list)):
        conn = SSHConnection(host)
        conn.connect()
        data_list.append(conn.exec_command(host.cmd))
        conn.close()

    print data_list
