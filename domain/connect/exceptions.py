from ..exceptions import General as RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS as _updateLoggerNameInKWARGS

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('Connection', kwargs)
        super().__init__(message, **kwargs)

class System(General):
    def __init__(self, message, **kwargs):
        _updateLoggerNameInKWARGS('System', kwargs)
        super().__init__(message, **kwargs)