class General(BaseException):
    def __init__(self, message, **kwargs):
        super().__init__(message)
        # Logger initialization
        import logging
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('pullgerSquirrel', kwargs)

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