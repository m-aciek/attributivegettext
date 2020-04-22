Extension of Python gettext that lets you use contexts as attributes in
translation strings.

It consists of two classes, ``AttributiveTranslations`` which holds attributes
logic.

    msgid "user"
    msgstr "użytkownik"

    msgctxt "accusative"
    msgid "user"
    msgstr "użytkownika"

    msgid "Select {} to change"
    msgstr "Wybierz {.accusative} do zmiany"
    
Second class, ``NoContextFallbackTranslations`` in case of lacking context
translation makes gettext fall back to translation of message without context.
In example above if ``msgstr`` for ``user/accusative`` would be empty, it would
 prefer ``"użytkownik"`` over not translated ``user/accusative`` ``"user"``.

#### Example installation

    from gettext import translation
    from translations import AttributiveTranslations
    from translations import NoContextFallbackTranslations

    pl = translation('messages', 'locale', ['pl'], AttributiveTranslations)
    pl.add_fallback(
        translation('messages', 'locale', ['pl'], NoContextFallbackTranslations)
    )
    pl.install(('pgettext',))

#### Example usage

Code (installation of translation ommited):

    user = _('user')
    group = _('group')

    list = []

    for o in (user, group):
        print(_('Select {} to change').format(o))
        list.append(input(f'{o.title()}: '))
        
With translation file:

    msgid "user"
    msgstr "użytkownik"

    msgctxt "accusative"
    msgid "user"
    msgstr "użytkownika"

    msgid "group"
    msgstr "grupa"

    msgctxt "accusative"
    msgid "group"
    msgstr "grupę"

    msgid "Select {} to change"
    msgstr "Wybierz {.accusative} do zmiany"

Will produce:
    
    Wybierz użytkownika do zmiany
    Użytkownik: …
    Wybierz grupę do zmiany
    Grupa: …
