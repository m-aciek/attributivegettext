from gettext import translation, gettext as _, pgettext
from translations import AttributiveTranslations

pl = translation('messages', 'locale', ['pl'], AttributiveTranslations)
pl.install(('pgettext',))


user = _('user')
pgettext('accusative', 'user')  # noop

group = _('group')
pgettext('accusative', 'group')  # noop

list = []

for o in (user, group):
    print(_('Select {} to change').format(o))
    list.append(input(f'{o.title()}: '))

# translation cycle:
# make changes
# run ``xgettext sample_application.py --keyword=pgettext:1c,2 --omit-header`` to regenerate PO file
# specify UTF-8 charset by adding empty msgid with msgstr equal to "Content-Type: charset=UTF-8"
# translate the file
# run ``msgfmt messages.po --output locale/pl/LC_MESSAGES/messages.mo`` to compile translation into proper location
# run localized application
