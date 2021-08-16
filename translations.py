from collections import UserString
from gettext import GNUTranslations


class AttributiveTranslations(GNUTranslations):
    def gettext(self, message):
        gettext = super().gettext
        CONTEXT_SEPARATOR = '\x04'

        class AttributiveTranslationString(UserString):
            def __init__(self, data):
                super().__init__(gettext(data))
                self.raw_data = data

            def __getattr__(self, item):
                msg_with_ctxt = f'{item}{CONTEXT_SEPARATOR}{self.raw_data}'
                if CONTEXT_SEPARATOR not in (result := gettext(msg_with_ctxt)):
                    return result
                return self.data

        return AttributiveTranslationString(message)
