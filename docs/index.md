# Welcome to H-hat

[![Unitary Foundation](https://img.shields.io/badge/Supported%20By-Unitary%20Foundation-FFFF00.svg)](https://unitary.foundation)
[![Discord Chat](https://img.shields.io/badge/dynamic/json?color=blue&label=Discord&query=approximate_presence_count&suffix=%20online.&url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2FJqVGmpkP96%3Fwith_counts%3Dtrue)](http://discord.unitary.foundation)

!!! warning

    This is a work in progress and may be seen as such. Errors, inconsistencies, tons of experimentation and modifications are happening. Until version 0.3 is released, it is prone to breaking changes.

**H-hat is a rule system, compiler framework, and a statically typed, functional and distributed system inspired, quantum programming language.**

## Quick Links

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } __Getting Started__

    ---

    Install H-hat and write your first quantum program

    [:octicons-arrow-right-24: Start here](getting_started.md)

-   :material-lightbulb:{ .lg .middle } __Introduction__

    ---

    Learn what H-hat is and why you might want to use it

    [:octicons-arrow-right-24: Learn more](introduction/what_is_hhat.md)

-   :material-book-open:{ .lg .middle } __Language Concepts__

    ---

    Dive deep into H-hat's design and features

    [:octicons-arrow-right-24: Explore](rule_system.md)

-   :material-code-braces:{ .lg .middle } __Examples__

    ---

    See H-hat in action with practical code examples

    [:octicons-arrow-right-24: View examples](dialects/heather/examples/first_code.md)

-   :material-account-group:{ .lg .middle } __Community__

    ---

    Join our Discord and get involved

    [:octicons-arrow-right-24: Get involved](community/get_involved.md)

-   :material-hand-heart:{ .lg .middle } __Contributing__

    ---

    Help improve H-hat and contribute code

    [:octicons-arrow-right-24: Contribute](how_contribute.md)

</div>

## What is H-hat?

H-hat aims to bridge the gap between classical and quantum computing by providing a unified programming model that treats quantum and classical computations symmetrically. Key features include:

- **Unified Programming Model**: Code reasoning closer to classical programming languages
- **Quantum Data Types**: Variables, functions, and types just like classical counterparts
- **Platform Independent**: Target multiple quantum architectures from the same code
- **Backend-Aware Types**: Explicit CPU and QPU type distinctions
- **Modern Language Features**: Ownership, RAII, lazy evaluation, metaprogramming

### Language Features

- **Static typing** with backend-aware types (CPU/QPU)
- **Function overloading** with compile-time resolution
- **Algebraic data types** (enums and structs)
- **Ownership and borrowing** for safe resource management
- **Reflective cast** for quantum-to-classical conversion
- **Metaprogramming** capabilities
- **Structured typing** approach
- **Concurrency** and distributed computing support
- **Multi-architecture targeting** (x86_64, aarch64, various QPU types)

## How It Works

### Quantum Variables

Quantum variables in H-hat:

- Hold quantum and classical instructions
- Execute content and perform measurement when a `cast` function is called
- Re-execute the same data content every time cast is invoked

### Dialects

H-hat defines rules and concepts but doesn't enforce a single syntax. Instead, it supports multiple **dialects** that implement these rules.

**Heather** is the reference dialect that showcases H-hat's features with a simple, intuitive syntax.

## Development Status

!!! note

    Development is in **alpha phase**. APIs and features are subject to change.

H-hat is being developed in two programming languages:

- **Python** (`python/`): Initial prototype (currently on hold)
- **Rust** (`rust/`): Production implementation (active development)

See [Code Organization](introduction/organization.md) for details.

## Get Started

Ready to try H-hat?

1. **[Install H-hat](getting_started.md)** - Set up your environment
2. **[Learn the basics](introduction/what_is_hhat.md)** - Understand core concepts
3. **[Try examples](dialects/heather/examples/first_code.md)** - Write your first code
4. **[Join the community](community/get_involved.md)** - Connect with other users

## Community

Join the H-hat community:

- **Discord**: Chat with us on the [UnitaryFoundation Discord](http://discord.unitary.foundation) in the `#h-hat` channel
- **GitHub**: Contribute on [github.com/hhat-lang/hhat_lang](https://github.com/hhat-lang/hhat_lang)
- **Issues**: Report bugs and request features on our [issue tracker](https://github.com/hhat-lang/hhat_lang/issues)

## Contributing

We welcome contributions! Check out:

- [How to Contribute](how_contribute.md) - Guidelines and process
- [Development Setup](contributing/setup.md) - Environment configuration
- [Good First Issues](https://github.com/hhat-lang/hhat_lang/issues?q=is%3Aissue+state%3Aopen+label%3A%22good+first+issue%22) - Beginner-friendly tasks
- [Code of Conduct](community/code_of_conduct.md) - Community guidelines

## License

H-hat is released under the [MIT License](https://github.com/hhat-lang/hhat_lang/blob/main/LICENSE).

## Supported By

H-hat is proudly supported by the [Unitary Foundation](https://unitary.foundation), a nonprofit organization dedicated to advancing quantum computing education and open-source quantum software.
