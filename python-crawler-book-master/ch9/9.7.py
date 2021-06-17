import logging

# 로거 생성
logger = logging.getLogger('test_log1')
logger.setLevel(logging.DEBUG)

# 로그 포멧팅 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 파일 핸들러 생성
fileHandler = logging.FileHandler('ch.9.7_debug.log')
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

fileHandler1 = logging.FileHandler('ch.9.7_warning.log')
fileHandler1.setLevel(logging.WARNING)

# 핸들러 등록
logger.addHandler(fileHandler)
logger.addHandler(fileHandler1)

logger.debug("debug")        # 5 단계
logger.info("info")          # 4 단계
logger.warning("warning")    # 3 단계
logger.error("error")        # 2 단계
logger.critical("critical")  # 1 단계
