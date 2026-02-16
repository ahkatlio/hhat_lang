# Code Organization

Understanding how H-hat's codebase is structured will help you navigate the project and contribute effectively.

!!! note

    Development is still in alpha phase. The structure may evolve as the project matures.

## Repository Structure

The H-hat project is organized into several main directories:

```
hhat_lang/
├── docs/              # Documentation website content
├── python/            # Python implementation (on hold)
├── rust/              # Rust implementation (active development)
├── sandbox/           # Testing and experimentation
└── definitions/       # Design diagrams and specifications
```

## Development Languages

H-hat has been developed in two programming languages (DPLs):

### Python Implementation

**Status**: Currently on hold

The Python implementation served as the initial prototype for exploring H-hat concepts. It includes:

- Core rule system implementation
- Heather dialect parser and compiler
- Type system prototypes
- Execution engine experiments

You can find detailed information in [`python/README.md`](https://github.com/hhat-lang/hhat_lang/blob/main/python/README.md).

**Location**: `python/`

**Key Directories**:

- `python/src/hhat_lang/core/` - Core language features
- `python/src/hhat_lang/dialects/heather/` - Heather dialect implementation
- `python/src/hhat_lang/low_level/` - Low-level quantum backends
- `python/src/hhat_lang/toolchain/` - CLI and development tools
- `python/tests/` - Test suite

### Rust Implementation

**Status**: Active development (primary focus)

The Rust implementation is the production-quality compiler and runtime being built for H-hat. It focuses on:

- Performance and efficiency
- Memory safety and correctness
- Production-ready tooling
- Multi-platform support

You can find detailed information in [`rust/README.md`](https://github.com/hhat-lang/hhat_lang/blob/main/rust/README.md).

**Location**: `rust/hhat_lang/`

**Key Directories**:

- `rust/hhat_lang/src/ir/` - Intermediate representations (HIR, layout IR, etc.)
- `rust/hhat_lang/src/parse/` - Parser and syntax tree construction
- `rust/hhat_lang/src/semantics/` - Semantic analysis and type checking
- `rust/hhat_lang/src/backends/` - Code generation for various targets
- `rust/hhat_lang/src/runtime/` - Runtime system
- `rust/hhat_lang/src/jit/` - Just-in-time compilation
- `rust/hhat_lang/src/passes/` - Compiler optimization passes
- `rust/hhat_lang/src/toolchain/` - CLI tools

## H-hat Components

### Core Rule System

The rule system defines the foundational concepts and constraints that all H-hat dialects must follow. This includes:

- Type system rules
- Ownership and borrowing rules
- Cast semantics
- Backend interaction protocols

**Python**: `python/src/hhat_lang/core/`  
**Rust**: `rust/hhat_lang/src/semantics/`

### Compiler Framework

The compiler framework provides infrastructure for:

- Parsing dialect syntax
- Building intermediate representations
- Type checking and semantic analysis
- Optimization passes
- Code generation

**Python**: `python/src/hhat_lang/core/compiler/`  
**Rust**: `rust/hhat_lang/src/` (distributed across modules)

### Heather Dialect

Heather is the reference dialect demonstrating H-hat's capabilities. It provides:

- Concrete syntax definition
- Parser implementation
- Standard library
- Example programs

**Python**: `python/src/hhat_lang/dialects/heather/`  
**Rust**: `rust/hhat_lang/src/` (integrated into main compiler)

**Documentation**: `docs/dialects/heather/`

## Documentation Structure

The documentation is organized to guide users through different aspects of H-hat:

### Getting Started

Quick start guides for new users:

- Installation instructions
- First program
- Development environment setup

### Introduction

High-level overview of H-hat:

- What is H-hat?
- Why use H-hat?
- Key features
- Code organization

### Language Concepts

Deep dives into H-hat's design:

- Rule system
- Type system
- Compiler framework
- Language design philosophy

### Examples

Practical code examples with the Heather dialect:

- Basic syntax
- Function definitions
- Type casting
- Quantum operations

### Guides

Language-specific development guides:

- Python guide
- Rust guide
- Running H-hat programs

### Tools

Documentation for development tools:

- Toolchain overview
- CLI reference
- IDE integration

### Community

How to get involved:

- Discord server
- Discussion forums
- Social media

### Contributing

Guidelines for contributors:

- How to contribute
- Development setup
- Code of conduct
- Pull request process

## Module Organization

### Python Modules

Each Python module contains a `README.md` explaining:

- Module purpose
- Key components
- How to use it
- Extension points

Notable modules:

- **core/types/** - Type system implementation
- **core/compiler/** - Compilation pipeline
- **core/execution/** - Runtime execution
- **dialects/heather/** - Heather dialect implementation

### Rust Modules

Rust modules follow standard Rust conventions:

- `mod.rs` or `module_name.rs` for module definition
- Hierarchical organization
- Public API documentation in doc comments

Notable modules:

- **ir/** - Intermediate representations and data structures
- **parse/** - Parser and AST construction
- **semantics/** - Type checking and semantic analysis
- **backends/** - Code generation for various targets

## Configuration Files

### Python Configuration

- `python/pyproject.toml` - Python project configuration
- `python/.pre-commit-config.yaml` - Code quality checks

### Rust Configuration

- `rust/hhat_lang/Cargo.toml` - Rust package configuration

### Documentation Configuration

- `mkdocs.yml` - Documentation site configuration
- `docs/stylesheets/extra.css` - Custom styling

## Testing

### Python Tests

Located in `python/tests/`:

- Unit tests for each module
- Integration tests for dialects
- Test utilities and fixtures

Run with: `pytest`

### Rust Tests

Distributed throughout Rust source:

- Unit tests in same file as implementation
- Integration tests in `tests/` directory
- Doc tests in documentation comments

Run with: `cargo test`

## Build Artifacts

### Python

- `python/dist/` - Distribution packages
- `python/.venv/` - Virtual environment (local)
- `python/src/**/__pycache__/` - Bytecode cache

### Rust

- `rust/target/` - Build output
  - `debug/` - Debug builds
  - `release/` - Optimized builds

## Contributing to Code Organization

When adding new features:

1. **Choose the right location**: Follow existing patterns
2. **Add README files**: Document your module's purpose (Python)
3. **Write doc comments**: Explain public APIs (Rust)
4. **Update documentation**: Keep docs/ in sync with code
5. **Add tests**: Include tests for new functionality

See [How to Contribute](../how_contribute.md) for detailed guidelines.

## Next Steps

- Start with [Getting Started](../getting_started.md)
- Explore the [language concepts](../rule_system.md)
- Try [examples](../dialects/heather/examples/first_code.md)
- Join the [community](../community/get_involved.md)
