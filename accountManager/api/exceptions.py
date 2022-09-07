from ..exceptions import General as _RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS as _updateLoggerNameInKWARGS

class General(_RootGeneral):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('api', kwargs)
        super().__init__(message, **kwargs)

class IncorrectInputData(General):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('IncorrectInputData', kwargs)
        super().__init__(message, **kwargs)