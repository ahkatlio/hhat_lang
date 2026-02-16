# Cast

The `cast` module implements H-hat's type casting system, particularly the unique quantum-to-classical casting protocol that defines how quantum data is transformed into classical types.

## Overview

Casting in H-hat follows a specific workflow when converting quantum data to classical types:

1. **Lazy Evaluation**: Quantum data content is lazily evaluated and translated into low-level quantum language (LLQ)
2. **Backend Execution**: The translated code is executed by the target backend, producing data sampling from quantum computation
3. **Post-processing**: The sampling result is interpreted according to specified criteria
4. **Type Conversion**: The output is cast into the target classical type
5. **Return**: The final result is returned to the code evaluation context

## Structure

### Files

- **`base.py`**: Core casting infrastructure
  - `BaseCastFn`: Abstract base class for all cast functions
  - `CastFnType`: Type annotation for cast functions
  - Helper functions for handling different data formats (iterables, dicts, result objects)
  - Sampling utilities (`get_max_count`, `get_min_count`, `get_sample`)

- **`transform_fns.py`**: Concrete casting transformation functions
  - Implementations of specific cast operations for different type pairs
  - Transformation logic for quantum-to-classical conversions
  - Classical-to-classical type conversions

## Key Concepts

### Cast Functions

Cast functions take data (as `DataDef`, `Literal`, or raw values) and transform it to match a target type. The signature follows:

```python
CastFnType = Callable[[DataDef | Literal | Any], Literal]
```

### Quantum Cast Protocol

When casting quantum data (`@some-var*some-type`), the system:
- Coordinates hybrid quantum and classical instruction execution
- Falls back to dialect implementations for unsupported classical instructions
- Requires target backend support for quantum instructions

### Sampling Strategies

The module provides utilities to extract meaningful classical values from quantum measurement results:
- **Max count**: Most frequent measurement outcome
- **Min count**: Least frequent measurement outcome
- **Custom sampling**: User-defined interpretation strategies

## Connections

- **`core/data`**: Uses `DataDef` and `Literal` representations
- **`core/types`**: Enforces type definitions and constraints
- **`core/execution`**: Integrates with `QuantumProgram` for quantum data execution
- **`core/memory`**: Interacts with `MemoryManager` for data access
- **`core/code`**: Uses IR graph structures for code transformation
- **`core/lowlevel`**: Translates to low-level quantum languages

## Usage Context

Cast operations are invoked when:
- Explicit type casting is requested in user code
- Quantum measurements need classical interpretation
- Type coercion is required for operations
- Bridge between quantum and classical paradigms is needed
