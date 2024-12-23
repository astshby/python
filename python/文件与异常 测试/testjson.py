from pathlib import Path
import json
# 输出
information={'name':'hby','birthday':'20050515'}
path=Path('test_work/testjson.json')
contents=json.dumps(information)
path.write_text(contents)

# 读取
# path=Path('test_work/testjson.json')
# information=path.read_text()
# contents=json.loads(information) 
# #相当于把information的内容经过一次“解压缩”，不用也可以
# print(information)