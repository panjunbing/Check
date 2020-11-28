import re

str = 'Filesystem      Size  Used Avail Use% Mounted on \n /dev/nvme0n1p3   18G  4.9G   13G  28% /'
test = re.search(r'.*', str).string
print(test)