from ..exceptions import General as RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('model', kwargs)

        super().__init__(message, **kwargs)

class Error(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('error', kwargs)
        super().__init__(message, **kwargs)

class Dublication(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('dublication', kwargs)
        super().__init__(message, **kwargs)