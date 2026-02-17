# Pygments Lexer for Heather Dialect

This module provides syntax highlighting support for H-hat's Heather dialect using [Pygments](https://pygments.org/).

## Features

- **Complete syntax support**: Keywords, operators, types, functions, modifiers, casts
- **Quantum-aware highlighting**: Special highlighting for quantum types and identifiers (prefixed with `@`)
- **Comment support**: Single-line (`//`) and multi-line (`/* */`) comments
- **Type distinction**: Different highlighting for classical and quantum types
- **Trait and modifier support**: Highlights traits (`#Trait`) and modifiers (`<mut>`)

## Installation

The lexer is automatically available when the `hhat_lang` package is installed with the `[pygments]` extra:

```bash
pip install -e ".[pygments]"
```

Or install Pygments separately:

```bash
pip install pygments
```

## Usage in MkDocs

To use the Heather lexer in MkDocs, update your `mkdocs.yml`:

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: heather
          class: heather
          format: !!python/name:pymdownx.superfences.fence_code_format
        - name: hhat
          class: heather
          format: !!python/name:pymdownx.superfences.fence_code_format
```

Then use in your markdown files:

````markdown
```heather
// A simple Heather program
main { print("Hello quantum world!") }

fn factorial(n:u32) u32 {
    if(
        eq(n 0): ::1
        true: ::mul(n factorial(sub(n 1)))
    )
}
```
````

## Aliases

The lexer can be referenced by any of these aliases:

- `heather` (recommended)
- `hhat`
- `hhat-heather`

## Syntax Examples

### Basic Program

```heather
// Hello world program
main { print("Hello quantum!") }
```

### Function Definition

```heather
fn add(a:i32 b:i32) i32 {
    ::sum(a b)
}
```

### Type Definition

```heather
type point { x:i32 y:i32 }

type status_t { ON OFF }
```

### Quantum Types

```heather
@q:@bool = @true
@state:@bell_t = prepare_bell_state()
```

### Constants

```heather
const pi:f64 = 3.141592653589793
const localhost:str = "127.0.0.1"
```

### Meta-functions

```heather
metafn if(options:[opt-body_t]) ir_t {
    // Implementation
}
```

### Modifiers

```heather
var<mut>:u32 = 42
ref<&>:point = &p
```

### Cast Operations

```heather
classical:bool = quantum_bit * bool
```

## Token Types

The lexer provides the following token categories:

- **Keywords**: `fn`, `type`, `main`, `metafn`, `modifier`, `const`, `use`
- **Operators**: `:`, `=`, `.`, `..`, `...`, `::`, `*`, `&`
- **Types**: Built-in classical (`i32`, `f64`, `str`) and quantum (`@bool`, `@int`) types
- **Numbers**: Integers, floats, and quantum integers (`@42`)
- **Strings**: Double-quoted strings
- **Comments**: Single-line and multi-line
- **Identifiers**: Regular, quantum (`@var`), and type names
- **Decorators**: Traits (`#Printable`)

## Testing

To verify the lexer is working:

```bash
python -m hhat_lang.dialects.heather.toolchain.pygments.setup_pygments
```

This will:
1. Register the lexer with Pygments
2. Run a verification test
3. Display sample highlighted code
4. Show usage instructions

## Custom Themes

The lexer uses standard Pygments token types, so it works with any Pygments theme. For H-hat-specific themes that match the project's visual identity, see issue #94.

## File Extensions

The lexer recognizes these file extensions:

- `*.hat` - Default H-hat source file extension
- `*.hhat` - Alternative extension

## MIME Types

- `text/x-heather`
- `text/x-hhat`

## Development

The lexer is implemented in `lexer.py` using Pygments' `RegexLexer` class. To modify or extend the syntax:

1. Update the token patterns in `lexer.py`
2. Test with `setup_pygments.py`
3. Update this README with new features
4. Update documentation examples

## References

- [Pygments Documentation](https://pygments.org/docs/)
- [Heather Syntax Documentation](../../../../docs/dialects/heather/syntax.md)
- [Heather Grammar](../../grammar/)
- [MkDocs Material - Code Blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)
