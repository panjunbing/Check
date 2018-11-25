class Host(object):
    def __init__(self, ip, port, username, password, cmd, re):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd
        self.re = re
