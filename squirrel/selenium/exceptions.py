from ..exceptions import General as RootGeneral
from pullgerExceptions import updateLoggerNameInKWARGS

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('selenium', kwargs)

        super().__init__(message, **kwargs)

class GetPage(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('GetPage', kwargs)
        super().__init__(message, **kwargs)

class PageOperation(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('PageOperation', kwargs)
        super().__init__(message, **kwargs)

class FindElements(General):
    def __init__(self, message, **kwargs):
        updateLoggerNameInKWARGS('PageOperation', kwargs)
        super().__init__(message, **kwargs)