from ..exceptions import General as _RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS as _updateLoggerNameInKWARGS

class General(_RootGeneral):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('pages', kwargs)
        super().__init__(message, **kwargs)

class Incorrect(General):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('incorrect', kwargs)
        super().__init__(message, **kwargs)