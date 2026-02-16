# What is H-hat?

[![Unitary Foundation](https://img.shields.io/badge/Supported%20By-Unitary%20Foundation-FFFF00.svg)](https://unitary.foundation)
[![Discord Chat](https://img.shields.io/badge/dynamic/json?color=blue&label=Discord&query=approximate_presence_count&suffix=%20online.&url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2FJqVGmpkP96%3Fwith_counts%3Dtrue)](http://discord.unitary.foundation)

!!! warning

    This is a work in progress and may be seen as such. Errors, inconsistencies, tons of experimentation and modifications are happening. Until version 0.3 is released, it is prone to breaking changes.

**H-hat is a rule system, compiler framework, and a statically typed, functional and distributed system inspired, quantum programming language.**

## Overview

H-hat is designed to bridge the gap between classical and quantum computing paradigms by providing a unified programming model that treats quantum and classical computations symmetrically. Unlike traditional quantum programming frameworks that focus primarily on quantum circuits, H-hat adopts a higher-level approach centered on data manipulation and transformation.

## Core Philosophy

The language is built on the principle that **quantum computation should be reasoned about using familiar programming constructs**, rather than requiring programmers to think exclusively in terms of quantum gates and circuits. This philosophy manifests in several key ways:

- **Data-Centric Approach**: Focus on manipulating quantum data rather than quantum states directly
- **Unified Syntax**: Classical and quantum code share similar syntaxes and components
- **Explicit Control**: Clear ownership, lifetime, and evaluation strategies
- **Platform Independence**: Abstract away specific quantum hardware details while maintaining efficiency

## What Makes H-hat Different?

### 1. Quantum Variables as First-Class Citizens

In H-hat, quantum variables work similarly to classical variables but with special semantics:

- Hold both quantum and classical instructions
- Execute content and perform measurement when a `cast` function is called
- Can be re-executed multiple times with the same data content

### 2. Multi-Paradigm Support

H-hat combines features from multiple programming paradigms:

- **Functional**: Pure functions, immutability options
- **Imperative**: Mutable state when needed
- **Distributed Systems**: Concurrency and resilience patterns
- **Systems Programming**: Low-level control and performance

### 3. Backend-Aware Type System

Types in H-hat are aware of their execution backend:

- CPU types for classical computation
- QPU types for quantum computation
- Automatic routing and optimization based on backend

### 4. Dialect System

Rather than enforcing a single syntax, H-hat defines a rule system that allows multiple syntaxes (dialects) to coexist and interoperate. The reference dialect, **Heather**, demonstrates these capabilities.

## Target Platforms

H-hat is designed to work across:

- Single computers
- High-Performance Computing (HPC) clusters
- Embedded systems
- Distributed quantum-classical hybrid systems

### Quantum Hardware Support

The language aims to support multiple quantum computing architectures:

- **Gate-based systems**: Superconducting qubits, trapped ions
- **Analog systems**: Neutral atoms, continuous variable systems
- **Photonic systems**: Optical quantum computers

## Inspirations

H-hat draws inspiration from several influential programming languages:

- **Fortran**: Performance-oriented scientific computing
- **Erlang**: Distributed systems and fault tolerance
- **Rust**: Ownership, memory safety, and zero-cost abstractions
- **C**: Low-level control and systems programming
- **Lean**: Formal verification and proof systems

## Development Status

!!! note

    H-hat is currently in **alpha phase**. The language specification and implementations are actively evolving.

The project is being developed in two programming languages:

- **Python**: Initial prototyping and exploration (currently on hold)
- **Rust**: Primary development focus for production implementation

## Next Steps

- Learn about [why you might want to use H-hat](why_hhat.md)
- Explore the [key features](features.md) in detail
- Understand the [code organization](organization.md)
- Jump into [Getting Started](../getting_started.md) to write your first H-hat program
