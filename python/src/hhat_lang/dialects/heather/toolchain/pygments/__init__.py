"""
Pygments lexer and style for H-hat's Heather dialect.

This module provides syntax highlighting support for Heather dialect code
in documentation and other tools that use Pygments.
"""

from hhat_lang.dialects.heather.toolchain.pygments.lexer import (
    HeatherLexer,
    HhatLexer,
)

__all__ = ["HeatherLexer", "HhatLexer"]
