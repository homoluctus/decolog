from log import log, get_logger


logger = get_logger()


def raise_error():
    raise Exception('Error!!!!')


@log(logger)
def main():
    """デコレーターの呼び出し元

    @log(logger)
    def main()       <=====>    log(logger)(main)()
    """
    logger.info('Hello world')
    return raise_error()


if __name__ == '__main__':
    main()
