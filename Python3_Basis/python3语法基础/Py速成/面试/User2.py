# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 22:57

class User2:
    __slots__ = ['id', 'name', 'sex', 'status']

    def __init__(self, id, name, sex, status):
        self.id = id
        self.name = name
        self.sex = sex
        self.status = status
