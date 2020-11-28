import paramiko


class SSHConnection(object):
    def __init__(self, host):
        self.host = host
        self.transport = None
        self.sftp = None
        self.client = None
        # self.connect()

    def connect(self):
        transport = paramiko.Transport(self.host.ip, self.host.port)
        transport.connect(username=self.host.username, password=self.host.password)
        self.transport = transport

    # 下载
    def download(self, remotepath, localpath):
        if self.sftp is None:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        self.sftp.get(remotepath, localpath)

    # 上传
    def put(self, localpath, remotepath):
        if self.sftp is None:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        self.sftp.put(localpath, remotepath)

    # 执行命令
    def exec_command(self, command):
        if self.client is None:
            self.client = paramiko.SSHClient()
            self.client._transport = self.transport
        stdin, stdout, stderr = self.client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            # print data.strip()  # 打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            # print err.strip()  # 输出错误结果
            return err

    def close(self):
        if self.transport:
            self.transport.close()
        if self.client:
            self.client.close()
