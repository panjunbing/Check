# 基于paramiko实现的自动化运维工具

## 1、部署：

```
pip3 install paramiko
pip3 install xlrd
pip3 install xlwt
```

## 2、使用方法
### 在host.xls文件中填入主机信息主机IP、SSH端口、主机用户名、主机密码、执行命令的文件名
例如：

 IP  | Port  | UserName  | Password  | CMD_File |
 :----:  | :----:  | :----:  | :----:  | :----: |
 192.168.1.109  | 22  | root  | 1234  | linux_check.xls |
 192.168.1.110  | 22  | root  | 1234  | linux_check.xls |

### 在CMD文件夹下新建执行命令的文件，填入执行的命令、返回结果的正则表达式、返回结果的描述，可参照下列格式：

 CMD  | CMD_RE  | Desc |
 :----  | :----:  | :----:  |
 df -h / &#124; awk 'NR==2 {print $5}'  | .*  | /文件系统使用率 |
 sum=`free -m &#124; grep Mem &#124; awk '{print $2}'`;use=`free -m &#124; grep Mem &#124; awk '{print $3}'`;awk 'BEGIN{printf"%.2f%\n",('$use'/'$sum')*100}'  | .*  | 内存使用率 |
 uptime &#124; awk '{print $10}'  | .*  | 系统15分钟内的负载 |

如果不需要通过正则表达式来筛选返回值，则填入 `.*`表示取所有内容

### 运行main.py，生成out.xls文件，如果按照上述的例子执行，则返回的结果格式如下所示：

 IP  | /文件系统使用率  | 内存使用率  | 系统15分钟内的负载  |
 :----:  | :----:  | :----:  | :----:  |
 192.168.1.109  | 28%  | 76.54%  | 0.27  |
 192.168.1.110  | 52%  | 72.52%  | 0.01  |
 
 ^_^

