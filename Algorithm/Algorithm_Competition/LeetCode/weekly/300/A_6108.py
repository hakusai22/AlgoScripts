# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/3 16:08


def decodeMessage(key: str, message: str) -> str:
    mm = {}
    val = 0
    for idx in key:
        if idx.isalpha() and idx not in mm:
            mm[idx] = chr(ord('a') + val)
            val += 1
    res = []
    for i in message:
        res.append(mm.get(i, " "))
    return "".join(res)


if __name__ == '__main__':
    print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
