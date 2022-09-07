from ..exceptions import General as RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('Authorization', kwargs)
        super().__init__(message, **kwargs)

class InputProcess(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('InputProcess', kwargs)
        super().__init__(message, **kwargs)

class ResultCheck(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('InputProcess', kwargs)
        super().__init__(message, **kwargs)

