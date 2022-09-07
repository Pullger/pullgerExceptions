from ..exceptions import General as RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('structures', kwargs)
        super().__init__(message, **kwargs)

class IncorrectInputData(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('IncorrectInputData', kwargs)
        super().__init__(message, **kwargs)