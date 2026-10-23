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

"""Chinese localisation for BeeRef.

Wrap every user visible string with ``_(...)`` and add the translation to
``zh_CN.py``. Missing keys fall back to the English original, and
``tests/test_i18n.py`` fails if the dict and the source drift apart.
"""

from beeref.i18n.translator import _, install_qt_translations

__all__ = ['_', 'install_qt_translations']
