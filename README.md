Extension of Python gettext that makes gettext function return object which
behave as string with translation, except you can access [context translations](https://docs.python.org/3/library/gettext.html#gettext.pgettext)
through its attributes.

Let's say your translation file looks as below:

    msgid "user"
    msgstr "użytkownik"

    msgctxt "accusative"
    msgid "user"
    msgstr "użytkownika"

With ``AttributiveTranslation`` class you can access ``accusative`` context
translation through attribute of no-context translation:

    >>> user = AttributiveTranslations(…).gettext('user')
    >>> user
    'użytkownik'
    >>> user.accusative
    'użytkownika'
    
"OK, and what's cool about that?"

Format string syntax introduced in Python 3 allows accessing arguments'
attributes in format strings. Therefore following is possible:

    >>> 'Wybierz {.accusative} do zmiany'.format(user)
    'Wybierz użytkownika do zmiany'

We are able to parametrize translation strings with e.g. nouns, which then can
change grammatical cases in translation. Above example being a gettext
translation:

    msgid "Select {} to change"
    msgstr "Wybierz {.accusative} do zmiany"

Some of the languages that use grammatical cases for nouns are: Armenian,
Assamese, most Balto-Slavic languages, Basque, most Caucasian languages, most
Dravidian languages, German, Icelandic, Japanese, Korean, Latin, Sanskrit,
Tibetan, the Turkic languages and the Uralic languages.
    
#### Fallback

OK, but let's say we miss a context translation:

    msgid "user"
    msgstr "użytkownik"

    msgctxt "accusative"
    msgid "user"
    msgstr ""  # <-- missing translation

``AttributiveTranslation`` class by default falls back to no-context
translation of the original English string:

    >>> user = AttributiveTranslations(…).gettext('user')
    >>> 'Wybierz {.accusative} do zmiany'.format(user)
    'Wybierz użytkownik do zmiany'

### Example installation

    from gettext import translation
    from translations import AttributiveTranslations

    pl = translation('messages', 'locale', ['pl'], AttributiveTranslations)
    pl.install(('pgettext',))

### Example usage

Code (installation of translation omitted):

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
