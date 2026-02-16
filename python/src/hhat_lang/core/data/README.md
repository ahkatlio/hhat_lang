# Data

The `data` module defines how H-hat represents and manipulates program data, including symbols, literals, variables, functions, and the crucial distinction between classical and quantum data paradigms.

## Overview

This module is central to H-hat's hybrid quantum-classical computation model. It provides:
- Data type representations (literals, symbols, identifiers)
- Variable declaration, assignment, and retrieval mechanisms
- Function definition and invocation structures
- Classical vs. quantum paradigm enforcement
- Array and composite data structures

## Structure

### Files

- **`core.py`**: Core data representations (522 lines)
  - `Symbol`: Simple identifier representation
  - `CompositeSymbol`: Nested/structured identifiers
  - `Literal`: Typed value representation
  - `LiteralArray`: Array of literals
  - `ObjArray`, `ObjTuple`: Composite data structures
  - `AllNoneQuantum`: Enum for quantum/classical/mixed categorization
  - `ACCEPTABLE_TYPE_VALUES`: Type validation mappings

- **`fn_def.py`**: Function definition data structures
  - `BuiltinFnDef`: Built-in function representations
  - Function metadata and signatures
  - Function call data structures

- **`var_def.py`**: Variable definition data structures
  - `DataDef`: Variable data definition
  - Variable metadata (type, value, scope)
  - Variable state tracking

- **`var_assignment.py`**: Variable assignment logic
  - Assignment operation implementations
  - Value update mechanisms
  - Scope-aware assignment

- **`var_utils.py`**: Variable utilities
  - Helper functions for variable operations
  - Variable validation
  - Type checking utilities

- **`utils.py`**: General data utilities
  - `isquantum()`: Check if data is quantum
  - `has_same_paradigm()`: Verify paradigm consistency
  - Data transformation helpers

## Key Concepts

### Classical vs. Quantum Paradigm

H-hat enforces strict paradigm rules:

- **Quantum data can contain classical instructions and data internally**
- **Classical data CANNOT contain quantum elements**
- Quantum data is lazily evaluated (not immediately computed)
- Quantum-to-classical conversion follows the cast protocol

### Symbols and Identifiers

- **`Symbol`**: Simple names (`x`, `myVar`, `quantum_state`)
- **`CompositeSymbol`**: Structured names (`module.function`, `Type.member`)
- Used for variables, functions, types, and module paths

### Literals

Literals represent typed values:

```python
Literal(value=42, lit_type="u64")
Literal(value=3.14, lit_type="float")
Literal(value="hello", lit_type="str")
```

Type validation ensures values match their declared types according to `ACCEPTABLE_TYPE_VALUES`.

### Arrays and Collections

- **`LiteralArray`**: Homogeneous arrays of literals
- **`ObjArray`**: Arrays of any objects
- **`ObjTuple`**: Immutable tuples
- Arrays must be either fully quantum, fully classical, or explicitly mixed

### Variable Definitions

`DataDef` encapsulates complete variable information:
- Name (Symbol/CompositeSymbol)
- Type (BaseTypeDef reference)
- Value (Literal or nested DataDef)
- Scope information
- Quantum/classical paradigm

### Function Definitions

Function data includes:
- Function name and signature
- Argument names and types
- Return type
- Function body (IR blocks)
- Built-in vs. user-defined distinction

## Paradigm Enforcement

The module provides utilities to enforce H-hat's paradigm rules:

```python
isquantum(data)  # Returns True if data is quantum
has_same_paradigm(data1, data2)  # Checks paradigm compatibility
```

Errors are raised when:
- Classical data attempts to contain quantum elements
- Arrays mix quantum and classical data improperly
- Type mismatches occur

## Connections

- **`core/types`**: Defines the type system that data conforms to
- **`core/memory`**: Stores and retrieves data structures
- **`core/code`**: Uses symbols and literals in IR representation
- **`core/execution`**: Executes operations on data
- **`core/cast`**: Transforms data between types
- **`core/error_handlers`**: Reports data-related errors (type mismatches, paradigm violations)

## Usage Context

The data module is used throughout the system:
- **Variable Operations**: Declaration, assignment, retrieval
- **Function Calls**: Argument passing, return values
- **Type Checking**: Validating data conforms to types
- **Expression Evaluation**: Computing with literals and variables
- **Quantum Operations**: Managing quantum state data
- **Cast Operations**: Type conversions and quantum measurements
