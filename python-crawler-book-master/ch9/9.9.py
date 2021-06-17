import logging
import logging.handlers

# 로거 생성
logger = logging.getLogger('test_log1')
logger.setLevel(logging.DEBUG)

# 로그 포멧팅 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 파일 용량 설정
file_max_bytes = 10 * 1024 # 수치를 바꿔가면서 실행해보세요.(10 * 1024 =1 0Mb)

# 파일 핸들러 생성
fileHandler = logging.handlers.RotatingFileHandler(filename='ch.9.9.log', maxBytes=file_max_bytes, backupCount=10)
fileHandler.setLevel(logging.ERROR)
fileHandler.setFormatter(formatter)

# 핸들러 등록
logger.addHandler(fileHandler)

logger.debug("debug")        # 5 단계
logger.info("info")          # 4 단계
logger.warning("warning")    # 3 단계
logger.error("error")        # 2 단계
logger.critical("critical")  # 1 단계
