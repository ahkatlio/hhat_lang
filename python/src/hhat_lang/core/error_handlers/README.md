# Error Handlers

The `error_handlers` module implements H-hat's comprehensive error handling system, providing structured error reporting that shields users from Python internals and presents clear, actionable H-hat-specific error messages.

## Overview

H-hat maintains its own error hierarchy to ensure users receive domain-specific error messages rather than Python stack traces. This module defines:
- Error code enumeration covering all possible errors
- Error handler base classes and specific error implementations
- Pretty-printed error output using Rich console
- Systematic error categorization

## Structure

### Files

- **`errors.py`**: Complete error system (954 lines)
  - `ErrorCodes`: Enum with all error codes and categories
  - `ErrorHandler`: Base class for all error handlers
  - Specific error classes for each error type
  - `sys_exit()`: Graceful exit with pretty error messages
  - Rich console integration for formatted output

## Key Concepts

### Error Code System

Error codes are organized into categories with reserved value ranges:

- **1**: `FEATURE_NOT_IMPLEMENTED_ERROR` - Reserved for unimplemented features
- **2-99**: Base errors (literals, symbols, paradigm checks)
- **101-199**: Index errors (qubit allocation and management)
- **200-299**: Type errors
- **300-399**: Data errors
- **400-499**: Cast errors
- **500-599**: Function errors
- **600-699**: Memory errors
- **700-799**: Instruction errors
- **800-899**: Evaluator errors
- **900-999**: Compiler errors

Example error codes:
```python
LITERAL_TYPE_MISMATCH_ERROR = 3
ARRAY_ELEMS_NOT_SAME_ERROR = 4
ARRAY_QUANTUM_CLASSICAL_MIXED_ERROR = 5
INDEX_ALLOCATION_ERROR = 101
TYPE_MEMBER_ALREADY_EXISTS_ERROR = 200
```

### ErrorHandler Base Class

All specific error classes inherit from `ErrorHandler` which provides:
- Error code association
- Formatted error message generation
- Rich console output formatting
- Consistent error reporting interface

### Graceful System Exit

The `sys_exit()` function ensures clean program termination:
```python
sys_exit(*args, error_fn=SomeError)
```

- Pretty-prints error message via Rich console
- Exits with appropriate error code
- Prevents Python stack traces from reaching users

### Error Categories

**Base Errors**: Fundamental data validation
- Literal type mismatches
- Symbol/identifier issues
- Paradigm violations (quantum/classical mixing)

**Index Errors**: Quantum qubit management
- Allocation failures
- Invalid qubit references
- Index out of bounds

**Type Errors**: Type system violations
- Member conflicts
- Invalid member access
- Type overflow
- Quantum-in-classical violations

**Memory Errors**: Memory management issues
- Stack frame errors
- Heap access violations
- Variable scope errors
- Invalid variable references

**Function Errors**: Function call issues
- Wrong argument types
- Argument count mismatches
- Undefined functions

**Cast Errors**: Type conversion failures
- Invalid cast operations
- Quantum-to-classical cast errors
- Unsupported conversions

**Compiler/Evaluator Errors**: Compilation and execution issues
- Parse errors
- Semantic errors
- Runtime evaluation failures

## Error Message Design

Error messages should be:
1. **User-facing**: No Python internals exposed
2. **Actionable**: Provide clear guidance on the issue
3. **Context-rich**: Include relevant code location and details
4. **Formatted**: Use Rich console for readability

## Connections

- **All core modules**: Every module uses error handlers for validation and error reporting
- **`core/data`**: Data validation errors (type mismatches, paradigm violations)
- **`core/types`**: Type system errors
- **`core/memory`**: Memory access and allocation errors
- **`core/execution`**: Runtime evaluation errors
- **`core/compiler`**: Compilation errors
- **`core/cast`**: Type casting errors
- **Dialects**: Dialect-specific error extensions

## Usage Patterns

### Raising Errors

```python
from hhat_lang.core.error_handlers.errors import LiteralTypeMismatchError

if value_type != expected_type:
    raise LiteralTypeMismatchError(value, expected_type)
```

### Graceful Exit

```python
from hhat_lang.core.error_handlers.errors import sys_exit, SomeError

if critical_error:
    sys_exit(error_details, error_fn=SomeError)
```

### Error Code Checks

```python
from hhat_lang.core.error_handlers.errors import ErrorCodes

if error.error_code == ErrorCodes.TYPE_MEMBER_ALREADY_EXISTS_ERROR:
    # Handle specific error type
```

## Extension Guidelines

When adding new error types:
1. Add error code to `ErrorCodes` enum in appropriate category range
2. Create specific error class inheriting from `ErrorHandler`
3. Implement formatted error message generation
4. Document error conditions and resolution steps
5. Update error code documentation with new ranges if needed
