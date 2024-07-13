# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 23:09
import logging.config

if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')

    logging.debug('debug message')
    logging.info("info message")
    logging.warning('warn message')
    logging.error("error message")
    logging.critical('critical message')
