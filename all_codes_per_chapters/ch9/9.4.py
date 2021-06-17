import logging

logging.basicConfig(filename='ch.9.4.log', level=logging.DEBUG)

logging.debug("debug")        # 5 단계
logging.info("info")          # 4 단계
logging.warning("warning")    # 3 단계
logging.error("error")        # 2 단계
logging.critical("critical")  # 1 단계
