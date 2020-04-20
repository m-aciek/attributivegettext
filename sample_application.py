from gettext import translation
from translations import AttributiveTranslations
from translations import NoContextFallbackTranslations

pl = translation('messages', 'locale', ['pl'], AttributiveTranslations)
pl.add_fallback(
    translation('messages', 'locale', ['pl'], NoContextFallbackTranslations)
)
pl.install(('pgettext',))


user = _('user')
pgettext('nominative', 'user')  # noop

group = _('group')
pgettext('nominative', 'group')  # noop

list = []

for o in (user, group):
    print(_('Select {} to change').format(o))
    list.append(input(f'{o.title()}: '))

# translation cycle:
# make changes
# run ``xgettext sample_application.py --keyword=pgettext:1c,2`` to regenerate PO file
# specify UTF-8 charset by replacing CHARSET text
# translate the file
# run ``msgfmt messages.po --output locale/pl/LC_MESSAGES/messages.mo`` to compile translation into proper location
# run localized application
