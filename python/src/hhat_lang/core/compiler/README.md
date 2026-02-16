# Compiler

The `compiler` module defines the abstract structure and interface for H-hat compilers, establishing the contract that all dialect-specific compilers must implement.

## Overview

This module provides the foundational abstractions for building compilers in the H-hat ecosystem. Each H-hat dialect must implement a compiler that conforms to these interfaces, ensuring consistent behavior across different language variants.

## Structure

### Files

- **`core.py`**: Core compiler abstractions
  - `BaseCompiler`: Abstract base class for all H-hat compilers
  - Defines required compiler interfaces: `parse()` and `evaluate()`

- **`builtin_modules.py`**: Built-in module definitions
  - Standard library modules available to all dialects
  - Core module implementations
  - Module loading and resolution logic

## Key Concepts

### BaseCompiler

The `BaseCompiler` abstract class establishes the minimal interface every H-hat compiler must provide:

```python
class BaseCompiler(ABC):
    @abstractmethod
    def parse(self) -> Any:
        """Convert source code to intermediate representation"""
        
    @abstractmethod
    def evaluate(self) -> Any:
        """Execute or compile the parsed representation"""
```

### Compiler Responsibilities

A complete H-hat compiler implementation must handle:

1. **Multiple Compiler Coordination**: Manage classical compilers, dialect-specific compilers, and quantum compilers
2. **Executor Management**: Maintain executors for evaluating IR code (both classical and quantum)
3. **Quantum Specifications**: Track available quantum devices, backends, and quantum languages
4. **Module System**: Load and manage built-in and user-defined modules
5. **Error Handling**: Properly report and handle compilation errors

### Compilation Workflow

The typical compilation process follows these stages:

1. **Parsing** (`parse()`):
   - Lexical analysis (tokenization)
   - Syntax analysis (AST construction)
   - Semantic analysis (type checking, name resolution)
   - IR generation

2. **Evaluation** (`evaluate()`):
   - IR optimization
   - Code generation (for compiled dialects)
   - Interpretation (for interpreted dialects)
   - Quantum code translation to low-level quantum languages

## Connections

- **`core/code`**: Produces and manipulates IR structures
- **`core/execution`**: Uses executors defined in execution module
- **`core/types`**: Performs type checking using type definitions
- **`core/memory`**: Manages program state during compilation
- **`core/error_handlers`**: Reports compilation errors
- **`core/lowlevel`**: Interfaces with quantum language translators
- **`dialects/*/compiler`**: Dialect-specific compiler implementations extend these abstractions

## Built-in Modules

Built-in modules provide standard functionality available to all programs:
- Core data structures and operations
- Standard mathematical functions
- I/O operations
- Utility functions
- May include dialect-specific standard libraries

## Usage Context

The compiler module is invoked during:
- **Source Code Compilation**: Converting `.hat` files to executable form
- **REPL Evaluation**: Interactive code execution
- **JIT Compilation**: Runtime code generation
- **Module Loading**: Importing external code
- **Tool Integration**: IDE support, linters, formatters

## Extension Points

When implementing a dialect compiler:
1. Extend `BaseCompiler`
2. Implement dialect-specific parsing logic
3. Define evaluation strategy (interpretation vs. compilation)
4. Register dialect-specific built-in modules
5. Integrate with quantum backend infrastructure
