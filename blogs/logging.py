import logging

'''
日志级别：
critical > error > warning > info > debug,notset
级别越高打印的日志越少，反之亦然，即
debug    : 打印全部的日志(notset等同于debug)
info     : 打印info,warning,error,critical级别的日志
warning  : 打印warning,error,critical级别的日志
error    : 打印error,critical级别的日志
critical : 打印critical级别
'''

handler=logging.FileHandler("/nuoxiao-django/TNLOG-error.log")

def log(level):
    logger = logging.getLogger()
    #不能重复创建handler,否则会重复写入同样的记录?
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical\n")

if __name__ == "__main__":
    log(logging.NOTSET)
    log(logging.DEBUG)
    log(logging.INFO)
    log(logging.WARNING)
    log(logging.ERROR)
    log(logging.CRITICAL)