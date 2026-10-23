# This file is part of BeeRef.
#
# BeeRef is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BeeRef is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BeeRef.  If not, see <https://www.gnu.org/licenses/>.

from PyQt6.QtCore import QLibraryInfo, QTranslator

from beeref.i18n.zh_CN import zh_CN


class Translator:
    """Look up UI strings in a dict, fall back to the English original.

    Keys are the untranslated strings as they appear in the source, so the
    English UI keeps working if a key is missing.
    """

    def __init__(self, translations):
        self.translations = translations

    def translate(self, text):
        return self.translations.get(text, text)


translator = Translator(zh_CN)


def _(text):
    """Translate a UI string."""
    return translator.translate(text)


def install_qt_translations(app):
    """Install Qt's own Chinese translation for standard widgets.

    Without this, buttons of QMessageBox, QFileDialog and QColorDialog
    ('OK', 'Cancel', 'Yes', 'No', ...) stay English, because those strings
    live inside Qt and are not covered by our own dict.
    """
    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    installed = []
    for name in ('qtbase_zh_CN', 'qt_zh_CN'):
        qt_translator = QTranslator(app)
        if qt_translator.load(name, path):
            app.installTranslator(qt_translator)
            installed.append(name)
    return installed
