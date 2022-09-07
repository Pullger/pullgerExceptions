from ..exceptions import General as seleniumGeneral
from pullgerExceptions import updateLoggerNameInKWARGS

class General(seleniumGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('chrome', kwargs)

        super().__init__(message, **kwargs)

class DriverVersionDifferences(seleniumGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('chrome', kwargs)

        super().__init__(message, **kwargs)