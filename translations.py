from collections import UserString
from gettext import GNUTranslations


class AttributiveTranslations(GNUTranslations):
    def gettext(self, message):
        gettext = super().gettext
        pgettext = self.pgettext

        class AttributableTranslationString(UserString):
            def __init__(self, data):
                super().__init__(gettext(data))
                self.raw_data = data

            def __getattr__(self, item):
                return pgettext(item, self.raw_data)

        return AttributableTranslationString(message)


class NoContextFallbackTranslations(GNUTranslations):
    def pgettext(self, context, message):
        return self.gettext(message)
