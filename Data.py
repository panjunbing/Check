class Data(object):
    def __init__(self, ip, desc, data):
        self.ip = ip
        # 执行命令的描述
        self.desc = desc
        # 执行命令返回的结果
        self.data = data
