import contextvars
import gettext
import os.path
from glob import glob

from app.t_string import TString

BASE_DIR = ""
LOCALE_DEFAULT = "en_US"
LOCALE_DIR = "locale"
locales = frozenset(
    map(
        os.path.basename,
        filter(os.path.isdir, glob(os.path.join(BASE_DIR, LOCALE_DIR, "*"))),
    )
)

gettext_translations = {
    locale: gettext.translation(
        "bot",
        languages=(locale,),
        localedir=os.path.join(BASE_DIR, LOCALE_DIR),
    )
    for locale in locales
}

gettext_translations["en_US"] = gettext.NullTranslations()
locales |= {"en_US"}


def use_current_gettext(*args, **kwargs) -> str:
    """Translate a string using the proper gettext based
    on the current_locale context var.

    :return: The gettext for the current locale
    :rtype: str
    """
    if not gettext_translations:
        return gettext.gettext(*args, **kwargs)

    locale = current_locale.get()
    return gettext_translations.get(
        locale, gettext_translations[LOCALE_DEFAULT]
    ).gettext(*args, **kwargs)


def translate(string: str) -> str:
    """Translates text.

    :param string: The text that needs translation
    :type string: str
    :return: The translated text
    :rtype: str
    """
    tstring = TString(string, use_current_gettext)
    return str(tstring)  # translate immediatly


def lazy_translate(string: str) -> TString:
    """Lazy translates text.

    :param string: The text that needs translation
    :type string: str
    :return: The TString object that can be translated later
    :rtype: TString
    """
    tstring = TString(string, use_current_gettext)
    return tstring


current_locale: contextvars.ContextVar = contextvars.ContextVar("i18n")


def set_current_locale():
    """Sets the locale to the LOCALE_DEFAULT."""
    current_locale.set(LOCALE_DEFAULT)


set_current_locale()
