from ..exceptions import General as RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('api', kwargs)

        super().__init__(message, **kwargs)

class IncorectInputArguments(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('IncorectInputArguments', kwargs)
        super().__init__(message, **kwargs)