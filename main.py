# coding=utf-8
import time
import xlrd
import xlwt
import re

from Host import Host
from SSHConnection import SSHConnection

if __name__ == "__main__":

    # 主机列表
    host_list = []

    # 返回数据列表
    return_list = []

    # 筛选数据列表
    data_list = []

    # 批量读取主机列表
    workbook = xlrd.open_workbook("host.xls")
    sheet = workbook.sheet_by_index(0)
    for i in range(sheet.nrows - 1):
        ip = sheet.cell(i + 1, 0).value.encode('utf-8')
        port = int(sheet.cell(i + 1, 1).value)
        username = sheet.cell(i + 1, 2).value.encode('utf-8')
        if sheet.cell(i + 1, 3).ctype == 1:
            password = sheet.cell(i + 1, 3).value
        else:
            password = str(int(sheet.cell(i + 1, 3).value))
        cmd_file = sheet.cell(i + 1, 4).value.encode('utf-8')
        # 命令
        cmd = []
        # 返回值名称
        text = []

        workbook_cmd = xlrd.open_workbook("/CMD/" + cmd_file)
        sheet_cmd = workbook.sheet_by_index(0)

        if sheet.cell(i + 1, 5).value.encode('utf-8') is not '':
            cmd_re = sheet.cell(i + 1, 5).value.encode('utf-8')
        else:
            cmd_re = None
        host = Host(ip, port, username, password, cmd, cmd_re)
        host_list.append(host)

    # 循环登录host并执行对应代码
    for i in range(len(host_list)):
        conn = SSHConnection(host_list[i])
        conn.connect()
        return_list.append(conn.exec_command(host_list[i].cmd))
        conn.close()

    # 用正则表达式筛选出数据
    for i in range(len(return_list)):
        if host_list[i].cmd_re is not None:
            data_list.append(re.search(host_list[i].cmd_re, return_list[i], ).group(0))
    print data_list

    # 写入excel
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("out sheet")
    style = xlwt.easyxf("font:name Times New Roman,color-index black,bold on", num_format_str="#,##0.00")
    sheet.write(0, 0, 'IP')
    sheet.write(0, 1, 'CMD')
    sheet.write(0, 2, 'OUT')
    for i in range(len(data_list)):
        sheet.write(i + 1, 0, host_list[i].ip)
        sheet.write(i + 1, 1, host_list[i].cmd)
        sheet.write(i + 1, 2, data_list[i])
    workbook.save("out.xls")

    time.sleep(60)
