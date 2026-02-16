# Execution

The `execution` module defines the infrastructure for executing H-hat programs, with special emphasis on hybrid quantum-classical execution and the coordination between quantum backends and classical dialect implementations.

## Overview

This module provides the execution engine abstractions that enable H-hat programs to run, particularly handling the complex interplay between:
- Classical instruction execution
- Quantum circuit execution on backends
- Fallback to dialect implementations when backends lack features
- Hybrid quantum-classical workflows

## Structure

### Files

- **`abstract_base.py`**: Base executor abstractions
  - `BaseExecutor`: Abstract base class for all executors
  - Common executor interfaces
  - Execution context management

- **`abstract_program.py`**: Quantum program execution (109 lines)
  - `BaseQuantumProgram`: Abstract base for quantum program handlers
  - `QuantumProgram`: Concrete quantum program executor
  - Coordinates quantum and classical instruction execution
  - Manages fallback logic for unsupported instructions

## Key Concepts

### BaseExecutor

The `BaseExecutor` abstract class defines the interface all executors must implement:
- Evaluate IR code
- Manage execution state
- Handle instruction dispatch
- Coordinate with memory manager

### QuantumProgram

`QuantumProgram` is the core class for executing quantum computations. It's used during quantum-to-classical cast operations (`@some-var*some-type`).

**Key Responsibilities**:

1. **Hybrid Execution Coordination**:
   - Execute quantum instructions on target backend
   - Execute classical instructions via dialect implementation
   - Bridge between quantum and classical contexts

2. **Fallback Logic**:
   - If classical instructions aren't on target backend → fallback to dialect
   - If classical instructions aren't in dialect → raise error
   - Quantum instructions MUST be on target backend or error

3. **Quantum Circuit Management**:
   - Construct quantum circuits from IR
   - Submit to quantum backend
   - Retrieve measurement results

**Constructor Parameters**:
```python
QuantumProgram(
    qdata: DataDef | Literal,      # Quantum data to execute
    mem: MemoryManager,             # Memory context
    node: IRNode,                   # Current IR node
    ir_graph: IRGraph,              # Complete IR graph
    executor: BaseExecutor,         # Executor instance
    qlang: BaseLLQManager          # Low-level quantum language manager
)
```

### Execution Workflow

1. **Classical Execution**:
   - Executor interprets IR nodes
   - Updates memory state
   - Returns computed values

2. **Quantum Execution** (during cast operation):
   - Lazy evaluation of quantum data
   - Translation to low-level quantum language
   - Backend execution producing measurement samples
   - Post-processing and interpretation
   - Cast to classical type

3. **Hybrid Execution**:
   - Quantum and classical instructions interleaved
   - Backend handles quantum instructions
   - Dialect handles classical instructions
   - Results passed between contexts

## Fallback Strategy

The execution model implements a sophisticated fallback mechanism:

```
User Code
    ↓
IR Representation
    ↓
Quantum Backend Execution
    ↓
┌─────────────────────────────────┐
│ Instruction Type?               │
├─────────────────────────────────┤
│ Quantum → MUST be in backend    │
│            or ERROR              │
│                                  │
│ Classical → Try backend first   │
│            → Fallback to dialect │
│            → ERROR if neither    │
└─────────────────────────────────┘
```

This ensures:
- Quantum operations use specialized hardware
- Classical operations have maximum flexibility
- Clear error messages when operations are unsupported

## Connections

- **`core/code`**: Executes IR graphs and nodes
- **`core/data`**: Operates on `DataDef` and `Literal` values
- **`core/memory`**: Reads/writes program state via `MemoryManager`
- **`core/cast`**: `QuantumProgram` is invoked during quantum-to-classical casting
- **`core/lowlevel`**: Uses `BaseLLQManager` to translate to quantum languages
- **`core/error_handlers`**: Reports execution errors
- **`low_level/quantum_lang`**: Quantum language translation
- **`low_level/target_backend`**: Backend communication

## Usage Context

The execution module is invoked during:

- **Program Evaluation**: Running compiled/interpreted H-hat code
- **REPL Sessions**: Interactive code execution
- **Quantum Casting**: Converting quantum data to classical types
- **Function Calls**: Executing function bodies
- **Expression Evaluation**: Computing operation results

## Executor Types

Different executors may exist for:
- **Interpreted execution**: Direct IR interpretation
- **JIT compilation**: Just-in-time code generation
- **AOT compilation**: Ahead-of-time compiled code execution
- **Quantum simulation**: Simulated quantum execution
- **Quantum hardware**: Real quantum device execution

## Extension Points

When implementing custom executors:
1. Extend `BaseExecutor`
2. Implement IR node evaluation logic
3. Define instruction dispatch mechanism
4. Handle memory state updates
5. Integrate with quantum backends (if applicable)
6. Implement error handling and reporting
