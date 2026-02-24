# Key Features

H-hat provides a comprehensive set of features designed to make quantum programming more accessible, maintainable, and powerful.

## Type System

### Static Typing

All variables and functions have explicit types known at compile time:

```heather
x:i32 = 42
p:point = .{x=34 y=43}
result:status_t = status_t.ON
```

This enables:

- Early error detection
- Better IDE support and tooling
- Optimization opportunities
- Clear documentation through types

### Backend-Aware Types

Types can be tagged with their execution backend (feature in development):

```heather
classical_data:i32@cpu = 100
```

The compiler aims to:

- Route operations to appropriate backends
- Manage data transfer between backends
- Optimize for target architecture

### Algebraic Data Types

Define rich data structures with enums and structs:

```heather
type status_t { ON OFF }

type result_t { 
  data{
    value:i32
    elapsed:f64
  }
  NONE
}

type point { x:i32 y:i32 }
```

## Function System

### Function Definition

Define functions with explicit types:

```heather
fn sum(a:i64 b:i64) i64 { ::add(a b) }

fn print-gt(a:u64 b:u64) {
  if(
    gt(a b): print(a)
    true: print(b)
  )
}
```

Return uses the `::` syntax sugar for returning expressions.

### Meta-Functions

Meta-functions provide special control flow constructs. See the [Heather dialect documentation](../dialects/heather/syntax.md) for details.

## Cast System

H-hat provides a cast system for type conversions. The exact semantics and quantum-specific casts are still being defined. See the [rule system documentation](../rule_system.md) for more information.

## Ownership and Resource Management

H-hat is designed with resource management in mind, particularly important for quantum computing where qubits are limited resources. The exact semantics of ownership, borrowing, and resource management are still being defined.

See the [rule system documentation](../rule_system.md) for current status.

## Quantum Computing Support

H-hat is designed for quantum-classical hybrid computing. The quantum primitives and backend integration are actively being developed. The compiler framework aims to support multiple quantum architectures through intermediate representations.

## Compiler Framework

H-hat uses a multi-stage compilation pipeline:

- Parsing and AST construction
- Semantic analysis and type checking
- Multiple intermediate representations (HIR, layout IR, etc.)
- Backend-specific code generation
- Optimization passes

See the [compiler framework documentation](../core/compiler_framework.md) for details.

## Development Experience

H-hat aims to provide a good development experience through:

- Clear and helpful error messages
- Comprehensive documentation
- Tooling support (language server, syntax highlighting)
- Active community on Discord

See the [toolchain documentation](../toolchain.md) for more details on available tools.

## Next Steps

- Learn about [code organization](organization.md)
- [Get started](../getting_started.md) with your first program
- Explore [language concepts](../rule_system.md) in depth
- Try [examples](../dialects/heather/examples/first_code.md)
