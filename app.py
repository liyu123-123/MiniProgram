import logging.handlers, os


def log_conf():
    """初始化日志配置"""
    # 日志文件位置
    logPath = "./Log"
    # 日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 处理器 -控制台
    sh = logging.StreamHandler()
    # 处理器 -文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logPath + os.sep + "mini.log",
    # trfh = logging.handlers.TimedRotatingFileHandler(filename=r"E:\pyproject\MiniProgram\log\mini.log",
                                                     when="midnight", interval=1,
                                                     backupCount=7, encoding="utf-8")
    # 格式化字符串
    f = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 格式化器
    formatter = logging.Formatter(f)

    # 处理器添加格式化器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)

    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "033CEl0w3CGl7V2XaA2w3wDFDH1CEl0B"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": "d10f99a7fb7396a77b4772b8d3db27dc"
}

