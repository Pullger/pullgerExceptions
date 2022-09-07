from pullgerExceptions import updateLoggerNameInKWARGS

class General(BaseException):
    def __init__(self, message, **kwargs):
        super().__init__(message)
        # Logger initialization
        import logging
        updateLoggerNameInKWARGS('pullgerDomain', kwargs)

        logger = logging.getLogger(kwargs['loggerName'])

        # Write internal error discription
        if 'exception' in kwargs:
            logMessage = f"{message} Internal discription: [{str(kwargs['exception'])}]"
        else:
            logMessage = message
        # Logger level
        if 'level' in kwargs and type(kwargs['level']) == int:
            logger.log(kwargs['level'], logMessage)
        else:
            logger.critical(logMessage)

class Initialization(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('Initialization', kwargs)
        super().__init__(message, **kwargs)

class Processing(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('Processing', kwargs)
        super().__init__(message, **kwargs)

