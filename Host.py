class Host(object):
    def __init__(self, ip, port, username, password, cmd, cmd_re, text):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd
        self.cmd_re = cmd_re
        self.text = text
