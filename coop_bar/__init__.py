# -*- coding: utf-8 -*-

VERSION = (1, 3, 0)


def get_version():
    """version"""
    return '%s.%s.%s' % (VERSION[0], VERSION[1], VERSION[2])

__version__ = get_version()
