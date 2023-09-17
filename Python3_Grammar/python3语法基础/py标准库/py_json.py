# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 17:34
import json

if __name__ == '__main__':
    info_string = """
    {
        "name": "echo",
        "age": 24,
        "coding skills": ["python", "matlab", "java", "c", "c++", "ruby", "scala"],
        "ages for school": { 
            "primary school": 6,
            "middle school": 9,
            "high school": 15,
            "university": 18
        },
        "hobby": ["sports", "reading"],
        "married": false
    }
    """

    data = json.loads(info_string)
    print(data)
    print(json.dumps(info_string))

    # 写JSON文件：
    with open("info1.json", "w") as f:
        json.dump(data, f)

    # 查看文件内容：
    with open("info.json") as f:
        print(f.read())

    # 读JSON文件：
    with open("info.json") as f:
        info = json.load(f)

    # %rm info.json
