from ..exceptions import General as RootGeneral

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('TT', kwargs)
        super().__init__(message, **kwargs)

class LinkCreate(General):
    def __init__(self, message, **kwargs):
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('LinkCreate', kwargs)
        super().__init__(message, **kwargs)

class IncorrectInputDATA(General):
    def __init__(self, message, **kwargs):
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('IncorrectInputDATA', kwargs)
        super().__init__(message, **kwargs)

class Integration(General):
    def __init__(self, message, **kwargs):
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('Integration', kwargs)
        super().__init__(message, **kwargs)
        pass