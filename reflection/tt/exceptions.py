from ..exceptions import General as RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('TT', kwargs)
        super().__init__(message, **kwargs)

class LinkCreate(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('LinkCreate', kwargs)
        super().__init__(message, **kwargs)

class IncorrectInputDATA(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('IncorrectInputDATA', kwargs)
        super().__init__(message, **kwargs)

class Integration(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('Integration', kwargs)
        super().__init__(message, **kwargs)