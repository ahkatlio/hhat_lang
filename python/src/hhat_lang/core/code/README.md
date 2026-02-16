# Code

The `code` module defines H-hat's internal intermediate representation (IR) for program code, providing the structures and abstractions needed to represent, manipulate, and analyze H-hat programs at various stages of compilation and execution.

## Overview

This module contains the core data structures for representing code internally, including:
- Abstract syntax representations
- Intermediate representation (IR) blocks and graphs
- Symbol tables for tracking identifiers
- Function headers and signatures
- Instruction definitions

## Structure

### Files

- **`abstract.py`**: Abstract base classes for IR components
  - `BaseIR`: Root abstract class for all IR nodes
  - Common interfaces for IR manipulation

- **`base.py`**: Core code representation classes (292 lines)
  - `FnHeaderDef`: Function signature definition for symbol tables
  - `FnHeader`: Function header with complete metadata
  - `BaseIRBlock`: Base class for IR code blocks
  - Fundamental building blocks for code representation

- **`instructions.py`**: Instruction definitions
  - Specific instruction types and their behaviors
  - Instruction encoding and manipulation
  - Classical and quantum instruction representations

- **`ir_block.py`**: IR block implementations
  - Code block structures
  - Block composition and nesting
  - Control flow representation

- **`ir_custom.py`**: Custom IR components
  - `ArgsValuesBlock`: Function argument representation
  - Specialized IR nodes for specific use cases
  - Custom code patterns

- **`ir_graph.py`**: IR graph data structure
  - `IRGraph`: Graph-based IR representation
  - `IRNode`: Individual nodes in the IR graph
  - Graph traversal and manipulation utilities
  - Enables analysis and optimization passes

- **`symbol_table.py`**: Symbol table implementation
  - Tracks identifiers (variables, functions, types)
  - Scope management
  - Name resolution

- **`tools.py`**: Utility functions for code manipulation
  - Helper functions for IR operations
  - Code transformation utilities

- **`utils.py`**: General utilities
  - Common helper functions
  - Shared constants and enumerations

## Key Concepts

### Function Headers

Function headers provide type signatures for functions stored in memory's symbol table. For example:

```python
fn sum(a:u64 b:u64) u64 { ::add(a b) }
```

Is represented as:

```python
FnHeaderDef(
    name=Symbol("sum"),
    type=Symbol("u64"),
    args_names=(Symbol("a"), Symbol("b")),
    args_types=(Symbol("u64"), Symbol("u64"))
)
```

### IR Graph Structure

The IR graph represents program code as a directed graph where:
- **Nodes** (`IRNode`) represent individual operations or code blocks
- **Edges** represent control flow and data dependencies
- **Graph** (`IRGraph`) provides global view and traversal capabilities

This enables:
- Optimization passes
- Data flow analysis
- Code transformation
- Execution planning

### Symbol Tables

Symbol tables maintain mappings between identifiers and their definitions:
- Variable names to types and values
- Function names to signatures and implementations
- Type names to type definitions
- Scope-aware lookups

## Connections

- **`core/data`**: Uses `Symbol`, `CompositeSymbol`, `Literal` for representing code elements
- **`core/types`**: Function headers reference type definitions
- **`core/memory`**: IR blocks are stored and retrieved from memory structures
- **`core/execution`**: IR graphs are executed by executors
- **`core/compiler`**: IR is generated during compilation phases
- **`core/fns`**: Function definitions use IR blocks for function bodies

## Usage Context

The code module is central to:
- **Parsing**: Converting source code to IR
- **Compilation**: Transforming and optimizing IR
- **Execution**: Interpreting or JIT-compiling IR
- **Analysis**: Understanding program behavior
- **Type checking**: Validating program correctness
