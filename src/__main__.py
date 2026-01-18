from utils.logger import logger
from config import Config

def main():
    logger.info("HIL Test System starting...")
    logger.info(f"Connecting to PostgreSQL → {Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}")
    logger.success("First run successful! Ready for GPIO & DUT magic.")
    logger.info(f'hello: {1+3}')
if __name__ == "__main__":
    main()