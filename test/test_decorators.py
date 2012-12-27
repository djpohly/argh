# -*- coding: utf-8 -*-
"""
Unit Tests For Decorators
~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import argh


def test_aliases():
    @argh.aliases('one', 'two')
    def func():
        pass

    attr = getattr(func, argh.constants.ATTR_ALIASES)
    assert attr == ('one', 'two')


def test_arg():
    @argh.arg('foo', help='help', nargs='+')
    @argh.arg('--bar', default=1)
    def func():
        pass

    attrs = getattr(func, argh.constants.ATTR_ARGS)
    assert attrs == [
        dict(option_strings=('foo',), help='help', nargs='+'),
        dict(option_strings=('--bar',), default=1),
    ]


def test_named():
    @argh.named('new-name')
    def func():
        pass

    attr = getattr(func, argh.constants.ATTR_NAME)
    assert attr == 'new-name'


def test_command():
    @argh.command
    def func():
        pass

    attr = getattr(func, argh.constants.ATTR_INFER_ARGS_FROM_SIGNATURE)
    assert attr == True


def test_wrap_errors():
    @argh.wrap_errors(KeyError, ValueError)
    def func():
        pass

    attr = getattr(func, argh.constants.ATTR_WRAPPED_EXCEPTIONS)
    assert attr == (KeyError, ValueError)