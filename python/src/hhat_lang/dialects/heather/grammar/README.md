# Heather Grammar Module

The `grammar` module defines Heather's syntax through formal grammar rules, using PEG (Parsing Expression Grammar) to specify how Heather code should be parsed.

## Overview

This module contains the complete grammar specification for the Heather dialect, broken down into logical categories. The grammar defines:
- Heather's syntax rules
- Token patterns
- Expression precedence
- Statement structures
- Language constructs

## Structure

### Files

- **`generic_grammar.py`**: Base grammar components
  - Common patterns used across grammar
  - Basic tokens and identifiers
  - Whitespace handling
  - Comment syntax
  - Literal patterns (numbers, strings)

- **`const_grammar.py`**: Constant and literal definitions
  - Integer literals (decimal, hex, binary, octal)
  - Floating-point literals
  - String literals (single/double quoted)
  - Character literals
  - Boolean literals (`true`, `false`)
  - Array literals
  - Special constants

- **`type_grammar.py`**: Type syntax
  - Type annotations (`: type`)
  - Type declarations (`type Name = ...`)
  - Struct type definitions
  - Enum type definitions
  - Array types (`Array<T>`)
  - Function types
  - Quantum type modifiers

- **`fn_grammar.py`**: Function definitions
  - Function declaration syntax
  - Function signatures
  - Parameter lists
  - Return type annotations
  - Function body syntax
  - Top-level program rule (`fn_program`)

- **`metamod_grammar.py`**: Metaprogramming and modifiers
  - Quantum modifiers (`@[...]`)
  - Compile-time directives
  - Annotations
  - Attributes

## Key Concepts

### PEG Grammar

Heather uses Parsing Expression Grammars via Arpeggio:

**Advantages**:
- Unambiguous parsing
- No left-recursion issues
- Ordered choice (first match wins)
- Easy to write and understand

**Grammar Rule Pattern**:
```python
def rule_name():
    return [pattern1, pattern2], optional_patterns, ...
```

### Whitespace Handling

Defined in `generic_grammar.py`:

```python
WHITESPACE = (r'\s', r'#.*')  # Spaces and comments
```

This establishes that:
- Whitespace is significant for token separation
- `#` starts single-line comments
- Comments are treated as whitespace

### Grammar Hierarchy

```
fn_program (top-level)
    ├── function_definitions
    ├── type_definitions
    ├── constant_definitions
    └── statements
        ├── declarations
        ├── assignments
        ├── expressions
        │   ├── function_calls
        │   ├── operators
        │   ├── literals
        │   └── identifiers
        ├── control_flow
        └── modifiers
```

### Lexical Elements (generic_grammar)

**Identifiers**:
```python
identifier = r'[a-zA-Z_][a-zA-Z0-9_]*'
```
- Start with letter or underscore
- Followed by letters, digits, underscores

**Reserved Keywords**:
```python
keywords = ['var', 'fn', 'type', 'if', 'else', 'while', 'for', 'return', 'quantum', ...]
```

**Operators**:
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Comparison: `<`, `>`, `==`, `!=`, `<=`, `>=`
- Logical: `and`, `or`, `not`
- Assignment: `=`
- Special: `::` (function call), `@` (cast/modifier)

### Constants and Literals (const_grammar)

**Integer Literals**:
```heather
42        # Decimal
0x2A      # Hexadecimal
0b101010  # Binary
0o52      # Octal
```

**Float Literals**:
```heather
3.14
1.0e-10
2.5E+3
```

**String Literals**:
```heather
"hello world"
'single quotes'
"escaped \"quotes\""
```

**Boolean Literals**:
```heather
true
false
```

**Array Literals**:
```heather
[1, 2, 3, 4, 5]
["a", "b", "c"]
```

### Type Syntax (type_grammar)

**Type Annotations**:
```heather
var x: u64
var name: str
var state: QuantumState
```

**Type Definitions**:
```heather
type Point = {
    x: float,
    y: float
}

type Color = Red | Green | Blue

type IntArray = Array<u64>
```

**Quantum Type Modifiers**:
```heather
quantum type QState = ...
```

### Function Syntax (fn_grammar)

**Function Declaration**:
```heather
fn add(a: u64, b: u64) u64 {
    ::return(::add(a, b))
}
```

**Components**:
- `fn`: keyword
- `add`: function name
- `(a: u64, b: u64)`: parameter list with types
- `u64`: return type
- `{ ... }`: function body

**Function Calls**:
```heather
::function_name(arg1, arg2)
```
Note the `::` prefix for calls.

### Metaprogramming and Modifiers (metamod_grammar)

**Quantum Modifiers**:
```heather
@[controlled target=q1]
apply_gate(q0)

@[adjoint]
rotation_gate(angle)
```

**Pattern**:
- `@[...]`: Modifier block
- Contains key-value pairs or flags
- Modifies behavior of following instruction

## Grammar Integration

### Parser Construction

Grammar files define rules used by Arpeggio:

```python
from arpeggio import ParserPython
from hhat_lang.dialects.heather.grammar.fn_grammar import fn_program

parser = ParserPython(fn_program, ws=WHITESPACE, skipws=True)
```

### Parsing Process

```
Source Code
    ↓
Lexical Analysis (tokenization)
    ↓
Syntax Analysis (grammar rules)
    ↓
Abstract Syntax Tree (AST)
    ↓
Semantic Analysis (IR visitor)
    ↓
Intermediate Representation
```

### Grammar Composition

Grammar rules are composed hierarchically:

**Example**:
```python
def fn_program():
    return ZeroOrMore([type_def, fn_def, statement])

def fn_def():
    return 'fn', identifier, '(', param_list, ')', type_annotation, fn_body

def param_list():
    return Optional(param, ZeroOrMore(',', param))

def param():
    return identifier, ':', type_annotation
```

This composes smaller rules into larger structures.

## Connections

- **`dialects/heather/parsing`**: Grammar rules used by parser
- **`dialects/heather/compiler`**: Compiler invokes parser with grammar
- **`dialects/heather/code`**: AST structure matches IR requirements
- **Core modules**: Grammar reflects H-hat core concepts (types, functions, data)

## Usage Context

Grammar is used during:

- **Compilation**: Parsing source code
- **Syntax Highlighting**: IDE/editor integration
- **Linting**: Syntax validation
- **Auto-completion**: IDE suggestions
- **Documentation**: Syntax reference generation

## Heather Syntax Characteristics

### Function Call Prefix

Heather uses `::` for function calls:
```heather
::add(1, 2)  # Not: add(1, 2)
```

**Rationale**:
- Distinguishes function calls from other syntax
- Explicit call sites
- Easier parsing

### Type-First Declarations

Variables declared with explicit types:
```heather
var x: u64 = 42  # Not: var x = 42
```

**Rationale**:
- Clear type information
- No type inference ambiguity
- Explicit is better than implicit

### Quantum Modifiers

Special syntax for quantum-specific annotations:
```heather
@[controlled target=q1, conditions=...]
gate_operation(q0)
```

**Rationale**:
- Quantum operations need metadata
- Flexible key-value syntax
- Clear quantum/classical distinction

### Cast Syntax

Special syntax for type casting:
```heather
@variable*target_type
```

**Rationale**:
- Visually distinctive
- Highlights quantum-to-classical casts
- Aligns with quantum modifier syntax (`@`)

## Extension Guidelines

To extend Heather's grammar:

1. **Add New Syntax**:
   - Add grammar rule in appropriate file
   - Update grammar hierarchy
   - Document new syntax

2. **Modify Existing Rules**:
   - Update rule definition
   - Check for conflicts with existing rules
   - Update parser integration

3. **Add Keywords**:
   - Add to reserved keyword list
   - Update identifier rule to exclude keyword
   - Document keyword usage

4. **Test Grammar**:
   - Write test cases for new syntax
   - Verify parsing correctness
   - Check error messages for invalid syntax

5. **Update Documentation**:
   - Add syntax examples
   - Update language reference
   - Provide migration guide if breaking changes

## Grammar Testing

Grammar rules should be tested:

**Valid Syntax**:
```python
parser.parse("fn add(a: u64, b: u64) u64 { ::return(::add(a, b)) }")
# Should succeed
```

**Invalid Syntax**:
```python
parser.parse("fn add a b { return a + b }")
# Should raise ParseError
```

## Design Philosophy

### Explicit Over Implicit

Heather grammar favors explicit syntax:
- Type annotations required
- Function calls prefixed
- Casts clearly marked

### Consistency

Similar constructs have similar syntax:
- All declarations use `keyword name: type`
- All function calls use `::name(...)`
- All modifiers use `@[...]`

### Readability

Grammar designed for human readability:
- Keywords are English words
- Punctuation is conventional
- Nesting is clear via braces

### Extensibility

Grammar structure allows extensions:
- Modular grammar files
- Composable rules
- Backward compatibility considerations
