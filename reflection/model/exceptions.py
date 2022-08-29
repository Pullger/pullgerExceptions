from ..exceptions import General as RootGeneral

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('model', kwargs)

        super().__init__(message, **kwargs)

class Error(General):
    def __init__(self, message, **kwargs):
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('error', kwargs)
        super().__init__(message, **kwargs)

class Dublication(General):
    def __init__(self, message, **kwargs):
        from pullgerExceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('dublication', kwargs)
        super().__init__(message, **kwargs)