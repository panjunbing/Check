import time
import xlrd
import xlwt
import re

from Data import Data
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
        ip = sheet.cell(i + 1, 0).value
        port = int(sheet.cell(i + 1, 1).value)
        username = sheet.cell(i + 1, 2).value
        if sheet.cell(i + 1, 3).ctype == 1:
            password = sheet.cell(i + 1, 3).value
        else:
            password = str(int(sheet.cell(i + 1, 3).value))
        cmd_file = sheet.cell(i + 1, 4).value

        # 读取主机对应CMD文件中的数据
        # 执行命令列表
        cmd = []
        # 执行命令结果使用的正则表达式列表
        cmd_re = []
        # 执行命令的描述列表
        desc = []
        workbook_cmd = xlrd.open_workbook("CMD/" + cmd_file)
        sheet_cmd = workbook_cmd.sheet_by_index(0)
        for j in range(sheet_cmd.nrows - 1):
            cmd.append(sheet_cmd.cell(j + 1, 0).value)
            if sheet_cmd.cell(j + 1, 1).value != '':
                cmd_re.append(sheet_cmd.cell(j + 1, 1).value)
            else:
                cmd_re.append(None)
            desc.append(sheet_cmd.cell(j + 1, 2).value)
        # 初始化单台主机并加入主机列表中
        host = Host(ip, port, username, password, cmd, cmd_re, desc)
        host_list.append(host)

    # 循环登录host并执行对应代码
    for i in range(len(host_list)):
        conn = SSHConnection(host_list[i])
        conn.connect()
        # 返回结果
        data = []
        # 返回结果的描述
        desc = []
        # 批量执行命令并将返回值通过正则表达式取出想要的返回值
        for j in range(len(host_list[i].cmd)):
            return_value = conn.exec_command(host_list[i].cmd[j]).decode('utf-8')
            test = re.search(r'.*', return_value)
            re_str = re.search(host_list[i].cmd_re[j], return_value).group()
            data.append(re_str)
            desc.append(host_list[i].desc[j])
        data_list.append(Data(host_list[i].ip, desc, data))
        conn.close()

    # 输出返回值

    print(data_list)

    # 写入excel
    workbook = xlwt.Workbook()
    # 新建表格
    sheet = workbook.add_sheet("执行结果")
    # 为样式创建字体
    font = xlwt.Font()
    # 字体样式
    font.name = 'name Times New Roman'
    font.height = 20 * 11
    font.bold = False
    font.underline = False
    font.italic = False
    # 单元格样式
    alignment = xlwt.Alignment()
    alignment.horz = 0x02  # 设置水平居中
    alignment.vert = 0x01  # 设置垂直居中
    alignment.wrap = 1
    # 边框样式
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    # 样式
    style = xlwt.easyxf()
    style.alignment = alignment
    style.font = font
    style.borders = borders

    sheet.write(0, 0, 'IP', style)
    # 写入返回值描述
    for i in range(len(data_list[0].desc)):
        sheet.write(0, i + 1, data_list[0].desc[i], style)
        sheet.col(i).width = 21 * 256
    # 写入ip和返回值
    for i in range(len(data_list)):
        sheet.write(i + 1, 0, data_list[i].ip, style)
        for j in range(len(data_list[0].data)):
            sheet.write(i + 1, j + 1, data_list[i].data[j], style)
    workbook.save("out.xls")

    print("脚本执行完毕")
    time.sleep(60)
