# Heather Code Module

The `code` module for the Heather dialect provides Heather-specific code representations, intermediate representation (IR) builders, and built-in function implementations.

## Overview

While H-hat core defines abstract code structures, this module implements Heather's concrete code representations and IR construction logic. It provides:
- Simple IR builder for Heather syntax
- Heather-specific IR instruction types
- Built-in function implementations for Heather
- Code generation utilities

## Structure

### Subdirectories

#### `builtins/`
Contains implementations of Heather's built-in functions:
- Arithmetic operations
- Logical operations
- String operations
- Type conversions
- Quantum gate operations
- I/O functions

These extend the core built-in system with Heather-specific implementations.

#### `simple_ir_builder/`
Implements Heather's IR construction pipeline:

**IR Builder**:
- Converts parsed AST to Heather IR
- Implements Heather-specific IR nodes
- Handles Heather syntax peculiarities
- Generates executable IR representations

**IR Classes**:
- `IR`: Base IR representation for Heather
- `IRModule`: Module-level IR container
- `AssignInstr`: Assignment instruction IR
- `CallInstr`: Function call instruction IR
- `CastInstr`: Type cast instruction IR
- `DeclareInstr`: Variable declaration IR
- `DeclareAssignInstr`: Combined declaration and assignment IR

**Key Files**:
- `ir.py`: Heather-specific IR node definitions
- `ir_builder.py`: IR construction logic (`build_ir`)
- Utilities for IR manipulation and transformation

## Key Concepts

### Heather IR vs. Core IR

While core defines abstract IR interfaces, Heather implements concrete IR for its syntax:

**Core IR**: Generic, dialect-agnostic
**Heather IR**: Tailored to Heather's syntax and semantics

Heather IR extends and implements:
- `BaseIR` → `IR`
- Generic IR blocks → Heather-specific instruction nodes
- Abstract operations → Concrete Heather operations

### Instruction Types

Heather defines specific instruction types for its operations:

**`DeclareInstr`**:
```
var x: u64
```
Declares variable without initialization.

**`AssignInstr`**:
```
x = 42
```
Assigns value to existing variable.

**`DeclareAssignInstr`**:
```
var y: u64 = 42
```
Combined declaration and initialization (common pattern).

**`CallInstr`**:
```
::add(x y)
```
Function call with Heather's `::` syntax.

**`CastInstr`**:
```
@quantum_var*u64
```
Type casting (especially quantum-to-classical).

### Simple IR Builder

The IR builder (`simple_ir_builder/`) converts Heather's parse tree to executable IR:

**Workflow**:
1. **Parse**: Heather source → AST (via grammar/parsing modules)
2. **Visit**: AST traversal with semantic actions
3. **Build**: Construct Heather IR nodes (`build_ir`)
4. **Link**: Connect IR nodes into graph
5. **Validate**: Check IR correctness
6. **Execute**: Run via Heather executor

**Builder Functions**:
```python
def build_ir(ast_node, context) -> IR:
    """Convert AST node to Heather IR"""
    # Dispatch to specific IR constructors
    # Handle Heather syntax patterns
    # Return IR representation
```

### Built-in Functions

Heather provides its own built-in function implementations:

**Categories**:
- **Arithmetic**: `add`, `sub`, `mul`, `div`, `mod`
- **Comparison**: `eq`, `ne`, `lt`, `gt`, `le`, `ge`
- **Logical**: `and`, `or`, `not`, `xor`
- **Bitwise**: Bit manipulation operations
- **String**: String concatenation, length, indexing
- **Conversion**: Type conversions between built-ins
- **Quantum**: Gate operations (Hadamard, CNOT, rotations, etc.)
- **I/O**: Print, read, file operations

**Implementation Pattern**:
```python
@include_builtin_fn(
    fn_entry=FnHeaderDef(...),
    fn_path=Path("/heather/math")
)
def heather_builtin_add(a: Literal, b: Literal, mem: MemoryManager) -> Literal:
    # Heather-specific implementation
    return Literal(a.value + b.value, lit_type=a.lit_type)
```

## Connections

- **`core/code`**: Extends core IR abstractions
- **`dialects/heather/grammar`**: Works with Heather's grammar definitions
- **`dialects/heather/parsing`**: Receives AST from parser
- **`dialects/heather/compiler`**: Provides IR to compiler
- **`dialects/heather/execution`**: IR executed by Heather executor
- **`core/fns`**: Registers built-ins in core function system
- **`core/types`**: Uses Heather type definitions

## Usage Context

This module is used during:

- **Compilation**: Converting Heather source to IR
- **Function Calls**: Executing built-in operations
- **Code Generation**: Producing executable representations
- **Optimization**: IR transformation passes
- **Debugging**: IR inspection and validation

## Heather Syntax Patterns

The IR builder recognizes Heather-specific patterns:

**Function Calls**:
```heather
::function_name(arg1 arg2 arg3)
```

**Variable Declaration**:
```heather
var name: type
var name: type = value
```

**Type Casting**:
```heather
@variable*target_type
```

**Quantum Modifiers**:
```heather
@[modifier options] instruction
```

**Control Flow**:
```heather
if condition { body } else { alternative }
```

## Extension Guidelines

To add new Heather code features:

1. **Define IR Nodes**:
   - Add new instruction types in `simple_ir_builder/ir.py`
   - Extend IR base classes

2. **Implement Builder Logic**:
   - Update `ir_builder.py` with construction logic
   - Handle new syntax patterns

3. **Add Built-ins** (if needed):
   - Implement function in `builtins/`
   - Register with `@include_builtin_fn`

4. **Update Grammar**:
   - Ensure grammar supports new features (in `grammar/`)
   - Add parsing rules

5. **Test**:
   - Add IR construction tests
   - Verify built-in behavior
   - Check execution correctness

## Design Philosophy

### Simplicity

The "simple IR builder" aims for:
- Clear, understandable IR nodes
- Straightforward AST→IR mapping
- Minimal abstraction overhead

### Heather-Specific

This module is not generic:
- Tailored to Heather's syntax
- Implements Heather's semantics
- Optimized for Heather patterns

### Extensibility

Despite being specific, it remains extensible:
- New instructions can be added
- Built-ins are modular
- IR transformations are pluggable
