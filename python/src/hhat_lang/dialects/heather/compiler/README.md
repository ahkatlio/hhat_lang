# Heather Compiler Module

The `compiler` module implements Heather's compilation pipeline, coordinating parsing, IR generation, and preparation for execution.

## Overview

This module provides the Heather-specific compiler implementation that extends H-hat's core compiler abstractions. It orchestrates the complete compilation process from Heather source code to executable IR.

## Structure

### Files

- **`core.py`**: Main Heather compiler implementation
  - `compile_project_ir()`: Primary compilation function
  - Project-level compilation coordination
  - Integration with grammar, parsing, and IR building
  - Built-in module generation

## Key Concepts

### Heather Compiler Pipeline

The compilation process follows these stages:

```
Heather Source Code (.hat files)
         ↓
   Grammar Parser
         ↓
  Abstract Syntax Tree (AST)
         ↓
    IR Visitor/Builder
         ↓
Intermediate Representation (IR)
         ↓
      IR Graph
         ↓
   Built-in Modules Integration
         ↓
     IR Graph Build/Link
         ↓
   Executable IR (ready for executor)
```

### compile_project_ir()

The main compilation function:

```python
def compile_project_ir(
    project_settings: HhatProjectSettings,
    raw_code: str,
    grammar_parser: Callable[[Callable], ParserPython] | None = None,
    program_rule: Callable | None = None,
) -> IRGraph
```

**Parameters**:
- **`project_settings`**: Project configuration (root path, config files, etc.)
- **`raw_code`**: Heather source code as string
- **`grammar_parser`**: Grammar parser (defaults to Heather's `parser_grammar_code`)
- **`program_rule`**: Top-level parsing rule (defaults to `fn_program`)

**Returns**:
- `IRGraph`: Complete executable IR graph for the project

**Process**:
1. Initialize IR graph
2. Generate built-in modules (`gen_builtin_modules`)
3. Parse source code using grammar
4. Visit AST and build IR
5. Link IR graph
6. Return complete executable graph

### Grammar Integration

The compiler integrates with Heather's grammar system:

**Default Grammar**:
- `parser_grammar_code`: Heather's PEG grammar parser
- `fn_program`: Top-level "program" rule

**Grammar Parser**:
- Uses Arpeggio (`ParserPython`) for PEG parsing
- Supports custom grammar extensions
- Allows dialect variations

### IR Building

Compilation delegates to the IR building pipeline:

```python
parse(
    grammar_parser=grammar_parser,
    program_rule=program_rule,
    raw_code=raw_code,
    project_root=project_settings.project_root,
    module_path=project_settings.project_root / MAIN_PATH,
    ir_graph=ir_graph,
)
```

This invokes:
- Grammar-based parsing (via `dialects/heather/parsing`)
- AST visitor pattern
- IR construction (via `dialects/heather/code/simple_ir_builder`)

### Built-in Module Generation

Before parsing user code, built-in modules are generated:

```python
gen_builtin_modules(ir_graph, ir_module, ir)
```

This populates the IR graph with:
- Core library functions
- Standard types
- Heather-specific built-ins
- Essential definitions

**Purpose**:
- Makes built-ins available to user code
- Establishes standard library
- Provides foundation for compilation

### IR Graph Building

After parsing and IR generation:

```python
ir_graph.build()
```

This:
- Links all IR nodes
- Resolves references
- Validates graph structure
- Prepares for execution

### Project Settings

The compiler uses `HhatProjectSettings` for configuration:

**Settings Include**:
- **`project_root`**: Base directory of project
- **`source_dir`**: Source code location
- **`config_files`**: Configuration file paths
- **`main_file`**: Entry point file
- **Quantum backend configuration**
- **Build options**

## Compilation Workflow

### Typical Usage

```python
from hhat_lang.core.config.base import HhatProjectSettings
from hhat_lang.dialects.heather.compiler.core import compile_project_ir

# Load project settings
settings = HhatProjectSettings(project_root=Path("/path/to/project"))

# Read source code
with open(settings.main_file) as f:
    source_code = f.read()

# Compile to IR
ir_graph = compile_project_ir(settings, source_code)

# IR graph is ready for execution
```

### Multi-File Projects

For projects with multiple files:
1. Main file is compiled first
2. Import statements trigger recursive compilation
3. Each imported file generates IR nodes
4. All IR nodes integrated into single graph

### Custom Compilation

You can customize compilation:

**Custom Grammar**:
```python
from my_heather_extension import my_grammar_parser

ir_graph = compile_project_ir(
    settings,
    code,
    grammar_parser=my_grammar_parser
)
```

**Custom Program Rule**:
```python
from my_heather_extension import my_program_rule

ir_graph = compile_project_ir(
    settings,
    code,
    program_rule=my_program_rule
)
```

## Connections

- **`core/compiler`**: Implements `BaseCompiler` interface
- **`core/config`**: Uses `HhatProjectSettings`
- **`dialects/heather/grammar`**: Uses Heather grammar definitions
- **`dialects/heather/parsing`**: Invokes parser and IR visitor
- **`dialects/heather/code`**: Uses Heather IR classes
- **`dialects/heather/execution`**: Compiled IR executed by Heather executor
- **`toolchain/project`**: Uses project structure constants
- **`core/code`**: Produces `IRGraph` output

## Usage Context

The compiler is invoked by:

- **CLI Tools**: `hhat compile main.hat`
- **REPL**: Interactive compilation and execution
- **Testing**: Automated test compilation
- **IDE Integration**: Language server, syntax checking
- **Build Systems**: Project build pipelines

## Error Handling

Compilation errors are reported via `core/error_handlers`:

**Error Types**:
- **Syntax Errors**: Invalid Heather syntax
- **Parse Errors**: Grammar violations
- **Semantic Errors**: Type errors, undefined names
- **IR Errors**: Invalid IR construction

Errors include:
- Line and column numbers
- Source code context
- Helpful error messages
- Suggested fixes (when possible)

## Extension Guidelines

To extend the Heather compiler:

1. **Add Compilation Phases**:
   - Insert new passes in `compile_project_ir`
   - Add pre/post-processing steps

2. **Implement Optimizations**:
   - Add IR transformation passes
   - Implement constant folding
   - Dead code elimination

3. **Support New Features**:
   - Extend grammar (in `grammar/`)
   - Update IR builder (in `code/`)
   - Modify compiler integration

4. **Custom Backends**:
   - Generate code for new targets
   - Implement backend-specific IR

5. **Enhanced Analysis**:
   - Add type inference
   - Implement data flow analysis
   - Add lint checks

## Future Enhancements

Potential compiler improvements:

- **Incremental Compilation**: Only recompile changed files
- **Caching**: Store compiled IR for faster builds
- **Parallel Compilation**: Compile independent modules concurrently
- **Optimization Levels**: `-O0`, `-O1`, `-O2` optimization flags
- **Ahead-of-Time Compilation**: Generate native code
- **Link-Time Optimization**: Cross-module optimizations
- **Debug Information**: Source map generation for debugging
