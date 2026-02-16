# Key Features

H-hat provides a comprehensive set of features designed to make quantum programming more accessible, maintainable, and powerful.

## Type System

### Static Typing

All variables and functions have explicit types known at compile time:

```heather
let x: Int = 42;
let q: Qubit = |0>;
let state: QubitArray[4] = prepare_ghz_state();
```

This enables:

- Early error detection
- Better IDE support and tooling
- Optimization opportunities
- Clear documentation through types

### Backend-Aware Types

Types are tagged with their execution backend:

```heather
let classical_data: Int@cpu = 100;
let quantum_data: Qubit@qpu = |+>;
```

The compiler automatically:

- Routes operations to appropriate backends
- Manages data transfer between backends
- Optimizes for target architecture

### Algebraic Data Types

Define rich data structures with enums and structs:

```heather
enum QuantumState {
    Pure(Qubit),
    Mixed(DensityMatrix),
    Entangled(QubitArray)
}

struct CircuitResult {
    state: QuantumState,
    shots: Int,
    elapsed: Duration
}
```

## Function System

### Explicit Function Overloading

Define multiple implementations of the same function:

```heather
fn measure(q: Qubit) -> Bool { ... }
fn measure(qs: QubitArray) -> BitArray { ... }
fn measure(q: Qubit, basis: PauliBasis) -> Bool { ... }
```

Resolution happens at compile time based on argument types.

### Meta-Functions

Special function-like constructs for control flow and composition:

```heather
// Option meta-function (like pattern matching)
match result {
    Some(value) => process(value),
    None => default_action()
}

// Block meta-function
repeat(10) {
    apply_gate(q);
}
```

### Modifiers

Modifiers change how data is treated:

```heather
let borrowed: &Qubit = &q;          // Borrow (reference)
let pointer: *Qubit = *q;           // Pointer (dereference)
let lazy_val: lazy Int = expensive(); // Lazy evaluation
let strict_val: strict Int = f();   // Strict evaluation
```

## Cast System

### Type Conversion

Explicit casting between compatible types:

```heather
let q: Qubit = |0>;
let classical: Bool = cast q to Bool;  // Measurement
```

### Reflective Cast

Special quantum-to-classical conversion that preserves quantum state:

```heather
let q: Qubit = hadamard(|0>);
let prob: Float = cast q to Float;  // Get probability without full collapse
```

This enables:

- Adaptive algorithms
- Quantum state tomography
- Error mitigation strategies

### Custom Cast Functions

Define your own conversion logic:

```heather
cast fn QubitArray to BitString {
    // Custom measurement and encoding
}
```

## Ownership and Memory Management

### RAII-Like Resource Management

Resources are automatically managed with clear ownership:

```heather
{
    let q = allocate_qubit();
    apply_gates(q);
    // q is automatically deallocated here
}
```

### Borrowing and References

Safely share data without copying:

```heather
fn apply_twice(q: &Qubit) {
    hadamard(q);
    hadamard(q);
}

let q = |0>;
apply_twice(&q);  // q is borrowed, not moved
```

### Move Semantics

Explicit transfer of ownership:

```heather
let q1 = |0>;
let q2 = move q1;  // q1 no longer valid
```

## Evaluation Strategies

### Strict vs Lazy Evaluation

Control when expressions are evaluated:

```heather
// Strict: evaluated immediately
let result: strict Int = compute_heavy();

// Lazy: evaluated when needed
let result: lazy Int = compute_heavy();
```

This is particularly important for:

- Quantum circuit construction
- Conditional quantum operations
- Performance optimization

## Quantum Primitives

### Platform-Independent Instructions

Define general quantum operations:

```heather
// Generic gate application
let q = hadamard(|0>);
let q = cnot(control, target);

// Parameterized gates
let q = rx(theta, |0>);
```

### Backend-Specific Optimization

The compiler translates these to architecture-specific implementations:

- Gate decomposition for native gate sets
- Pulse-level compilation where available
- Topology-aware routing

## Multi-Architecture Support

### Target Selection

Specify target architectures explicitly:

```heather
#[target(x86_64)]
fn classical_processing(data: &[Float]) { ... }

#[target(superconducting)]
fn quantum_processing(q: Qubit) { ... }
```

### Cross-Compilation

Build for multiple targets from a single codebase:

```bash
hhat build --target x86_64
hhat build --target aarch64
hhat build --target ion_trap
```

## Concurrency and Parallelism

### Concurrent Quantum Operations

Express parallel quantum computations:

```heather
parallel {
    let result1 = quantum_subroutine1(q1);
    let result2 = quantum_subroutine2(q2);
}
```

### Distributed Computing

Built-in support for distributed execution:

```heather
@distributed
fn large_scale_simulation(params: Parameters) {
    // Automatically distributed across available resources
}
```

## Metaprogramming

### Compile-Time Evaluation

Execute code during compilation:

```heather
const N: Int = 1024;
const QUBIT_COUNT: Int = log2(N);  // Computed at compile time
```

### Code Generation

Generate code based on types and constants:

```heather
#[generate_for(backends = [ion_trap, superconducting])]
fn optimized_circuit(q: Qubit) { ... }
```

## Structured Typing

### Duck Typing with Verification

Types can be compatible based on structure:

```heather
trait Measurable {
    fn measure(self) -> Bool;
}

// Any type implementing measure() is Measurable
```

The compiler verifies structural compatibility at compile time.

## Module System

### Explicit Imports

Clear dependency management:

```heather
import quantum.gates.{hadamard, cnot};
import classical.math.{sqrt, cos};
```

### Namespaces

Organize code into logical modules:

```heather
module quantum::algorithms {
    pub fn grover_search(...) { ... }
    pub fn shor_factorization(...) { ... }
}
```

## Safety and Verification

### Type Safety

Strong type system prevents common errors:

- No implicit conversions between quantum and classical
- Ownership prevents use-after-free
- Borrow checking prevents data races

### Formal Verification Support

Foundation for proving correctness:

- Type-level guarantees
- Effect systems for tracking quantum operations
- Integration points for external provers

## Development Experience

### Clear Error Messages

Helpful compiler diagnostics:

```
error: cannot cast Qubit to Int without measurement
  --> program.hhat:10:5
   |
10 |     let x: Int = q;
   |     ^^^^^^^^^^^^^^^ implicit quantum measurement
   |
   = help: use `cast q to Int` to explicitly measure
```

### Tooling Support

Rich development ecosystem:

- Language server protocol (LSP) implementation
- Syntax highlighting
- Debugger integration
- Package manager

## Next Steps

- Learn about [code organization](organization.md)
- [Get started](../getting_started.md) with your first program
- Explore [language concepts](../rule_system.md) in depth
- Try [examples](../dialects/heather/examples/first_code.md)
