from ..exceptions import General as _RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS as _updateLoggerNameInKWARGS

class General(_RootGeneral):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('Authorization', kwargs)
        super().__init__(message, **kwargs)

class InputProcess(General):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('InputProcess', kwargs)
        super().__init__(message, **kwargs)

class ResultCheck(General):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('InputProcess', kwargs)
        super().__init__(message, **kwargs)

