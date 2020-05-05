Extension of Python gettext that lets you use context translations as
attributes.

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

Languages that use grammatical cases of nouns are: Armenian, Assamese, most 
Balto-Slavic languages, Basque, most Caucasian languages, most Dravidian
languages, German, Icelandic, Japanese, Korean, Latin, Sanskrit, Tibetan, the
Turkic languages and the Uralic languages.
    
#### Fallback

OK, but let's say we not yet have a context translation:

    msgid "user"
    msgstr "użytkownik"

    msgctxt "accusative"
    msgid "user"
    msgstr ""  # <-- missing translation

Our translation class will fallback accusative of user to original English
string:

    >>> user = AttributiveTranslations(…).gettext('user')
    >>> 'Wybierz {.accusative} do zmiany'.format(user)
    'Wybierz user do zmiany'

``NoContextFallbackTranslations`` class will make us fall back to no-context
translation which makes a bit better user experience:

    >>> translations = AttributiveTranslations(…)
    >>> translations.add_fallback(NoContextFallbackTranslations(…))
    >>> user = translations.gettext('user')
    >>> 'Wybierz {.accusative} do zmiany'.format(user)
    'Wybierz użytkownik do zmiany'

### Example installation

    from gettext import translation
    from translations import AttributiveTranslations
    from translations import NoContextFallbackTranslations

    pl = translation('messages', 'locale', ['pl'], AttributiveTranslations)
    pl.add_fallback(
        translation('messages', 'locale', ['pl'], NoContextFallbackTranslations)
    )
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
