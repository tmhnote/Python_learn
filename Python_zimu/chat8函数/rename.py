import os
import re

path = "./"
files = os.listdir(path)

for name in files:
    if name.endswith(".py") or name == ".gitkeep":
        # 匹配 8-X / 8-XX 这类编号
        res = re.match(r"(示例8-)(\d+)(.*)", name)
        if res:
            prefix, num, suffix = res.groups()
            new_num = num.zfill(3)  # 不足三位前面补0
            new_name = prefix + new_num + suffix
            os.rename(name, new_name)
print("重命名完成")
