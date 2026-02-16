# Functions (fns)

The `fns` module implements H-hat's function system, providing infrastructure for defining, registering, and invoking both built-in and user-defined functions.

## Overview

This module handles function management across the H-hat ecosystem, including:
- Built-in function registration and lookup
- Function signature definitions
- Function call mechanics
- Path-based function organization
- Integration with memory management for function storage

## Structure

### Files

- **`abstract_base.py`**: Abstract function interfaces
  - Base classes for function representations
  - Common function protocols

- **`core.py`**: Core function infrastructure (64 lines)
  - `builtin_fns_path`: Global dictionary mapping paths to built-in functions
  - `include_builtin_fn`: Decorator for registering built-in functions
  - Function invocation wrappers
  - Built-in function signature management

## Key Concepts

### Built-in Functions

Built-in functions are implemented in Python and made available to H-hat programs. They provide core functionality like:
- Arithmetic operations (`add`, `sub`, `mul`, `div`)
- Logical operations (`and`, `or`, `not`)
- Type conversions
- I/O operations
- Quantum gate operations

### Function Registration

The `include_builtin_fn` decorator registers built-in functions:

```python
@include_builtin_fn(
    fn_entry=FnHeaderDef(
        name=Symbol("add"),
        type=Symbol("int"),
        args_names=(Symbol("a"), Symbol("b")),
        args_types=(Symbol("int"), Symbol("int"))
    ),
    fn_path=Path("/core/math")
)
def builtin_fn_int_add(a: Literal, b: Literal, mem: MemoryManager) -> Literal:
    return Literal(a.value + b.value, lit_type="int")
```

This:
1. Creates function signature (`FnHeaderDef`)
2. Associates implementation with signature
3. Registers in `builtin_fns_path` dictionary
4. Makes function available at specified path

### Function Paths

Functions are organized hierarchically by path:
```
/core/math/add
/core/math/sub
/core/logic/and
/quantum/gates/hadamard
```

This enables:
- Namespace organization
- Module-like structure
- Name conflict resolution
- Selective imports

### Function Signatures

Function signatures (`FnHeaderDef`) capture:
- **Function name**: `Symbol` identifier
- **Return type**: `Symbol` or `CompositeSymbol`
- **Argument names**: Tuple of `Symbol`s
- **Argument types**: Tuple of type symbols

Example:
```python
FnHeaderDef(
    name=Symbol("process_quantum_state"),
    type=Symbol("measurement_result"),
    args_names=(Symbol("state"), Symbol("basis")),
    args_types=(Symbol("QuantumState"), Symbol("MeasurementBasis"))
)
```

### Function Call Interface

Built-in functions follow a standard signature:
```python
def builtin_fn(
    *args: Literal | DataDef,
    mem: MemoryManager
) -> Literal | DataDef:
    # Function implementation
    pass
```

**Parameters**:
- `*args`: Function arguments (typed data)
- `mem`: Memory manager for state access

**Returns**:
- Result as `Literal` or `DataDef`

### Function Storage

Functions are stored in two locations:

1. **`builtin_fns_path` dictionary** (in this module):
   - Maps `Path` → `dict[FnHeader, BuiltinFnDef]`
   - Global registry of all built-in functions
   - Enables function lookup by path and signature

2. **Memory's Symbol Table** (in `core/memory`):
   - Stores `FnHeader` as key
   - Maps to function implementation
   - Provides runtime function lookup

## Built-in Function Structure

`BuiltinFnDef` wraps Python implementations:
- **`fn_name`**: Function identifier
- **`fn_args`**: `ArgsValuesBlock` with argument metadata
- **`fn_type`**: Return type
- **`fn_impl`**: Python callable implementation
- **`fn_path`**: Hierarchical path

## Function Lookup Process

1. Parse function call in source code
2. Extract function name and argument types
3. Construct `FnHeader` from call site
4. Look up in memory's symbol table
5. Retrieve `BuiltinFnDef` or user function
6. Validate argument types
7. Invoke implementation
8. Return result

## Connections

- **`core/code`**: `FnHeaderDef` and `FnHeader` defined in code module, used here
- **`core/data`**: Uses `Symbol`, `Literal`, `DataDef` for function data
- **`core/memory`**: Functions stored in `MemoryManager`'s symbol table
- **`core/types`**: Function arguments and returns have type constraints
- **`core/execution`**: Executors invoke functions during evaluation
- **`core/compiler`**: Compiler resolves function calls to definitions
- **Dialects**: Each dialect can register its own built-in functions

## Usage Context

The functions module is used for:
- **Function Definition**: Registering new built-in functions
- **Function Calls**: Resolving and invoking functions at runtime
- **Module Loading**: Importing functions from paths
- **Standard Library**: Providing core functionality
- **Extension**: Adding dialect-specific functions

## User-Defined Functions

While this module focuses on built-in functions, user-defined functions:
- Are parsed from source code
- Stored in memory with `FnHeader` keys
- Have IR block bodies (not Python implementations)
- Follow same lookup and invocation patterns

## Extension Guidelines

To add a new built-in function:

1. **Implement the function**:
   ```python
   def my_builtin_fn(arg1: Literal, arg2: Literal, mem: MemoryManager) -> Literal:
       # Implementation
       return result
   ```

2. **Create signature**:
   ```python
   fn_entry = FnHeaderDef(
       name=Symbol("my_function"),
       type=Symbol("return_type"),
       args_names=(Symbol("arg1"), Symbol("arg2")),
       args_types=(Symbol("type1"), Symbol("type2"))
   )
   ```

3. **Register with decorator**:
   ```python
   @include_builtin_fn(fn_entry=fn_entry, fn_path=Path("/my/module"))
   def my_builtin_fn(...):
       ...
   ```

4. Function becomes available at `/my/module/my_function`
