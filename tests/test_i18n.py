"""Tests for the Chinese localisation.

These tests fail when the source and ``beeref/i18n/zh_CN.py`` drift apart,
which is the main maintenance risk of a dict based translation.
"""

import ast
import os.path
import re

from beeref.i18n import _
from beeref.i18n.zh_CN import zh_CN

SRC_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'beeref')
PLACEHOLDER = re.compile(r'%[sd]|\{\w+\}')


def get_source_keys():
    """Collect every string literal passed to ``_(...)`` in the package."""
    keys = set()
    for dirpath, dirnames, filenames in os.walk(SRC_DIR):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            path = os.path.join(dirpath, filename)
            with open(path, encoding='utf-8') as f:
                tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if (isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Name)
                        and node.func.id == '_'
                        and node.args
                        and isinstance(node.args[0], ast.Constant)
                        and isinstance(node.args[0].value, str)):
                    keys.add(node.args[0].value)
    return keys


def test_every_translated_string_is_in_the_dict():
    missing = get_source_keys() - set(zh_CN)
    assert not missing, 'Missing translations: %r' % sorted(missing)


def test_the_dict_has_no_unused_entries():
    unused = set(zh_CN) - get_source_keys()
    assert not unused, 'Unused translations: %r' % sorted(unused)


def test_placeholders_match_the_original():
    for key, value in zh_CN.items():
        assert sorted(PLACEHOLDER.findall(key)) == \
            sorted(PLACEHOLDER.findall(value)), \
            'Placeholder mismatch: %r -> %r' % (key, value)


def test_unknown_strings_fall_back_to_the_original():
    assert _('Some String That Is Not In The Dict') == \
        'Some String That Is Not In The Dict'


def test_known_strings_are_translated():
    assert _('&File') == '文件(&F)'
    assert _('[Untitled]') == '[未命名]'
