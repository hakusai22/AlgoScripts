# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 23:06

import loggingDemo

if __name__ == '__main__':
    # logging.basicConfig(filename='test.log', level=logging.INFO)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename="test.log"
    )

    logging.debug('debug message')
    logging.info("info message")
    logging.warning('warn message')
    logging.error("error message")
    logging.critical('critical message')
