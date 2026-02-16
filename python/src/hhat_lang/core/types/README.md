# Types

The `types` module implements H-hat's type system, providing infrastructure for defining, validating, and manipulating both built-in and user-defined types with full support for the classical-quantum paradigm distinction.

## Overview

This module is the foundation of H-hat's type system, handling:
- Type definitions and structures
- Built-in type implementations (integers, floats, strings, etc.)
- User-defined types (structs, enums, quantum types)
- Type validation and checking
- Member access and manipulation
- Classical vs. quantum type constraints
- Type resolution and inference

## Structure

### Files

- **`abstract_base.py`**: Abstract type system foundations
  - `BaseTypeDef`: Abstract base class for all type definitions
  - `BaseTypeDataBin`: Type data storage abstraction
  - Common type interfaces and protocols

- **`core.py`**: Core type implementations (283 lines)
  - `SingleType`: Single-value types
  - `TupleType`: Tuple/product types
  - `ArrayType`: Array/list types
  - Type validation functions (`is_valid_member`)
  - Type operations and manipulations

- **`builtin_base.py`**: Built-in type base classes
  - Foundation for standard types
  - Common built-in type functionality

- **`builtin_types.py`**: Standard built-in types
  - Integer types (`u16`, `u32`, `u64`, `int`)
  - Floating-point types (`float`)
  - String types (`str`, `char`)
  - Boolean types (`bool`)
  - Unit type

- **`builtin_conversion.py`**: Type conversion functions
  - Standard type conversions
  - Coercion rules
  - Type compatibility checking

- **`new_base_type.py`**: User-defined type base
  - Infrastructure for custom types
  - Type extension framework

- **`new_builtin_core.py`**: Core new built-in types
  - Extended built-in type system
  - Additional standard types

- **`new_builtin_std.py`**: Standard library types
  - Collection types
  - Utility types
  - Common data structures

- **`new_core.py`**: New type system core
  - Next-generation type system components
  - Type system extensions

- **`resolvers.py`**: Type resolution utilities
  - Type inference logic
  - Name-to-type resolution
  - Type compatibility checking

- **`utils.py`**: Type system utilities
  - `BaseTypeEnum`: Enumeration of type categories
  - Helper functions for type operations
  - Type checking utilities

## Key Concepts

### Type Hierarchy

```
BaseTypeDef (abstract)
    ├── SingleType (single values: int, float, quantum state)
    ├── TupleType (products: pairs, records, structs)
    └── ArrayType (sequences: lists, arrays)
```

### Type Definitions

All types inherit from `BaseTypeDef` which provides:

**Core Properties**:
- **Type name**: Identifier (`Symbol` or `CompositeSymbol`)
- **Type content**: Internal structure/members
- **Type members**: Accessible fields/methods
- **Quantum flag**: Classical vs. quantum designation

**Core Methods**:
- Member access and validation
- Type comparison and equality
- Size and layout information

### Classical vs. Quantum Types

H-hat's type system enforces paradigm rules:

**Classical Types**:
- Immediately evaluated
- Cannot contain quantum members
- Standard computational behavior

**Quantum Types**:
- Lazily evaluated
- Can contain classical members
- Follow quantum computational model

**Validation**:
```python
def is_valid_member(datatype: BaseTypeDef, member: Symbol) -> bool:
    """Quantum types support classical members, but classical types cannot contain quantum members."""
    if not datatype.is_quantum and isquantum(member):
        return False
    return True
```

### Built-in Types

Standard types available in all H-hat programs:

**Integer Types**:
- `u16`: Unsigned 16-bit integer
- `u32`: Unsigned 32-bit integer
- `u64`: Unsigned 64-bit integer
- `int`: Signed integer (implementation-dependent size)

**Floating-Point**:
- `float`: IEEE 754 floating-point

**Text**:
- `char`: Single character
- `str`: String (sequence of characters)

**Boolean**:
- `bool`: True/false values

**Quantum Types** (dialect-specific):
- Quantum states
- Quantum registers
- Measurement results

### Type Construction

#### SingleType

For simple, atomic types:
```python
int_type = SingleType(
    type_name=Symbol("u64"),
    type_content=...,
    is_quantum=False
)
```

#### TupleType

For product types (structs, records):
```python
pair_type = TupleType(
    type_name=Symbol("Pair"),
    type_content=(Symbol("u64"), Symbol("u64")),
    is_quantum=False
)
```

#### ArrayType

For sequence types:
```python
int_array_type = ArrayType(
    type_name=Symbol("Array"),
    element_type=Symbol("u64"),
    is_quantum=False
)
```

### Type Members

Types can have members (fields, methods):

```python
struct Point {
    x: float,
    y: float,
    distance: fn() -> float
}
```

**Member Operations**:
- `get_member(name)`: Access member by name
- `has_member(name)`: Check if member exists
- `add_member(name, type)`: Add new member
- `list_members()`: Get all members

### Type Resolution

The type system resolves type references:

**Name Resolution**:
```
Symbol("u64") → Built-in unsigned 64-bit integer type
Symbol("MyType") → User-defined type from symbol table
CompositeSymbol("Module.Type") → Type from module
```

**Type Inference**:
- Deduce types from literals
- Infer types from expressions
- Propagate types through operations

### Type Validation

Types are validated during:

1. **Variable Declaration**:
   - Value must match declared type
   - Quantum/classical paradigm must match

2. **Function Calls**:
   - Argument types must match parameters
   - Return type must match declaration

3. **Operations**:
   - Operand types must be compatible
   - Result type must be valid

4. **Member Access**:
   - Member must exist in type
   - Access must be valid for paradigm

### Type Errors

Type errors are reported via `core/error_handlers`:

- **`TypeMemberAlreadyExistsError`**: Duplicate member name
- **`TypeMemberOverflowError`**: Too many members
- **`TypeQuantumOnClassicalError`**: Quantum member in classical type
- **`TypeInvalidMemberError`**: Invalid member access
- **`TypeInvalidIndexOnContentError`**: Invalid type indexing

## Connections

- **`core/data`**: Types define the structure of data (`DataDef`, `Literal`)
- **`core/memory`**: Variables stored with type information
- **`core/compiler`**: Type checking during compilation
- **`core/execution`**: Runtime type validation
- **`core/cast`**: Type conversions follow type rules
- **`core/error_handlers`**: Type errors reported via error system
- **Dialects**: Each dialect can define additional types

## Usage Context

The type system is used throughout:

- **Variable Declaration**: Type annotations on variables
- **Function Signatures**: Parameter and return types
- **Type Checking**: Compile-time and runtime validation
- **Cast Operations**: Source and target type validation
- **Member Access**: Struct/object field access
- **Generic Programming**: Parameterized types (future)

## Type Categories (BaseTypeEnum)

Types are categorized for different purposes:

- **Primitive**: Basic types (int, float, bool)
- **Composite**: Structured types (tuples, structs)
- **Collection**: Container types (arrays, lists)
- **Quantum**: Quantum data types
- **Function**: Function types (higher-order functions)
- **Custom**: User-defined types

## User-Defined Types

Users can define custom types:

**Struct Types**:
```
type Point = { x: float, y: float }
```

**Enum Types**:
```
type Color = Red | Green | Blue
```

**Quantum Types**:
```
quantum type QuantumState = ...
```

Custom types integrate seamlessly with built-ins.

## Extension Guidelines

To add new types:

1. **Extend Base Classes**:
   ```python
   class MyType(BaseTypeDef):
       def __init__(self, ...):
           super().__init__(...)
   ```

2. **Implement Required Methods**:
   - Member access
   - Type validation
   - Equality and comparison

3. **Register Type**:
   - Add to built-in type registry (if built-in)
   - Make available in user programs

4. **Define Operations**:
   - Implement type-specific operations
   - Define conversion rules

5. **Document Behavior**:
   - Type semantics
   - Valid operations
   - Paradigm constraints

## Future Directions

Potential type system extensions:

- **Generic Types**: Parameterized types (`Array<T>`, `Option<T>`)
- **Type Classes**: Trait/interface system
- **Dependent Types**: Types depending on values
- **Linear Types**: Resource tracking (important for quantum)
- **Effect Types**: Tracking side effects and quantum operations
