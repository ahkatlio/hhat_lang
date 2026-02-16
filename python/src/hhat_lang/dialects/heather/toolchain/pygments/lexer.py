from __future__ import annotations

from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
    Whitespace,
)

__all__ = ["HeatherLexer"]


class HeatherLexer(RegexLexer):
    """
    Pygments lexer for H-hat's Heather dialect.
    
    The Heather dialect is a reference implementation of the H-hat quantum
    programming language, designed to bridge classical and quantum computing
    paradigms with a unified syntax.
    
    .. versionadded:: 2.18
    """

    name = "Heather"
    url = "https://docs.hhat-lang.org/"
    aliases = ["heather", "hhat", "hhat-heather"]
    filenames = ["*.hhat", "*.hat"]
    mimetypes = ["text/x-heather", "text/x-hhat"]

    # Keywords for control flow and definitions
    keywords_decl = (
        "const",
        "fn",
        "main",
        "meta-fn",
        "metafn",
        "modifier",
        "metamod",
        "type",
        "use",
    )

    # Type-related keywords
    keywords_type = (
        "bdn_t",
        "fn_t",
        "ir_t",
        "opbdn_t",
        "opn_t",
        "optn_t",
    )

    # Built-in classical types
    builtin_types_classical = (
        "bool",
        "f32",
        "f64",
        "float",
        "hashmap",
        "i32",
        "i64",
        "imag",
        "int",
        "sample_t",
        "str",
        "u32",
        "u64",
    )

    # Built-in quantum types (prefixed with @)
    builtin_types_quantum = (
        "@bell_t",
        "@bool",
        "@false",
        "@int",
        "@true",
        "@u2",
        "@u3",
        "@u4",
    )

    # Boolean literals
    bool_literals = ("false", "true")

    # Quantum boolean literals
    quantum_bool_literals = ("@false", "@true")

    # Reserved keywords
    keywords_reserved = ("self",)

    tokens = {
        "root": [
            # Whitespace
            (r"[ \t\r\n,;]+", Whitespace),
            # Comments
            (r"//[^\n]*\n", Comment.Single),
            (r"/\*", Comment.Multiline, "comment"),
            # Keywords
            (words(keywords_decl, suffix=r"\b"), Keyword.Declaration),
            (words(keywords_type, suffix=r"\b"), Keyword.Type),
            (words(keywords_reserved, suffix=r"\b"), Keyword.Reserved),
            # Types
            (words(builtin_types_classical, suffix=r"\b"), Name.Builtin),
            (words(builtin_types_quantum, suffix=r"\b"), Name.Builtin.Quantum),
            # Boolean literals
            (words(bool_literals, prefix=r"\b", suffix=r"\b"), Name.Constant),
            (words(quantum_bool_literals, prefix=r"\b", suffix=r"\b"), Name.Constant.Quantum),
            # Return operator
            (r"::", Operator.Word),
            # Cast operator
            (r"\*(?=\s)", Operator.Word),
            # Reference operator
            (r"&", Operator.Word),
            # Operators
            (r"\.\.\.(?=\s|\)|\]|\})", Operator),  # Variadic
            (r"\.\.(?=\s|\)|\]|\}|[a-zA-Z0-9])", Operator),  # Range
            (r":", Operator),
            (r"=", Operator),
            (r"\.", Operator),
            # Punctuation
            (r"[(){}\[\]]", Punctuation),
            # Trait identifier (starts with # and uppercase)
            (r"#\[", Punctuation, "trait-list"),
            (r"#@?[A-Z][a-zA-Z0-9\-_]*", Name.Decorator),
            # Modifiers (inside angle brackets)
            (r"<", Punctuation, "modifier"),
            # Numbers
            # Quantum integer (prefixed with @)
            (r"@-?(?:[1-9]\d*|0)\b", Number.Quantum),
            # Float
            (r"-?\d+\.\d+", Number.Float),
            # Integer
            (r"-?(?:[1-9]\d*|0)\b", Number.Integer),
            # Strings
            (r'"[^"]*"', String),
            # Identifiers
            # Quantum identifiers (prefixed with @)
            (r"@[a-zA-Z][a-zA-Z0-9\-_]*", Name.Variable.Quantum),
            # Type identifiers (start with uppercase)
            (r"[A-Z][a-zA-Z0-9\-_]*", Name.Class),
            # Regular identifiers
            (r"[a-z][a-zA-Z0-9\-_]*", Name),
        ],
        "comment": [
            (r"[^*/]", Comment.Multiline),
            (r"/\*", Comment.Multiline, "#push"),
            (r"\*/", Comment.Multiline, "#pop"),
            (r"[*/]", Comment.Multiline),
        ],
        "trait-list": [
            (r"\s+", Whitespace),
            (r"@?[A-Z][a-zA-Z0-9\-_]*", Name.Decorator),
            (r"\]", Punctuation, "#pop"),
        ],
        "modifier": [
            (r"\s+", Whitespace),
            (r"&", Operator.Word),
            (r"\*", Operator.Word),
            (r"\.\.\.", Operator),
            (r":", Operator),
            (r"=", Operator),
            (r"@?[a-zA-Z][a-zA-Z0-9\-_]*", Name.Attribute),
            (r"-?(?:[1-9]\d*|0)\b", Number.Integer),
            (r">", Punctuation, "#pop"),
        ],
    }


# Legacy alias for backwards compatibility
HhatLexer = HeatherLexer
