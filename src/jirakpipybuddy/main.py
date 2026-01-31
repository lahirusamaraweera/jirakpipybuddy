from jirakpipybuddy.logger import get_logger

def main():
    logger = get_logger(name=__name__)
    logger.info("Hello, world!")


if __name__ == "__main__":
    main()
