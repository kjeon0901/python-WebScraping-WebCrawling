import logging

logging.basicConfig(filename='ch.9.5_debug.log', level=logging.DEBUG)

logging.debug("debug")        # 5 단계
logging.info("info")          # 4 단계
logging.warning("warning")    # 3 단계
logging.error("error")        # 2 단계
logging.critical("critical")  # 1 단계

logging.basicConfig(filename='ch.9.5_warning.log', level=logging.warning)

logging.debug("debug1")        # 5 단계
logging.info("info1")          # 4 단계
logging.warning("warning1")    # 3 단계
logging.error("error1")        # 2 단계
logging.critical("critical1")  # 1 단계
