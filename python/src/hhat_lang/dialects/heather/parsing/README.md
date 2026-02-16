# Heather Parsing Module

The `parsing` module bridges Heather's grammar and IR construction by implementing the parser and AST visitor that convert source code into executable intermediate representation.

## Overview

This module is the heart of Heather's front-end compilation pipeline, implementing:
- Parser initialization and configuration
- AST (Abstract Syntax Tree) visitor pattern
- Semantic analysis during parsing
- IR node construction from parsed syntax
- Integration between grammar rules and code generation

## Structure

### Files

- **`ir_visitor.py`**: Main parsing and IR construction (861 lines)
  - `parse()`: Primary parsing function
  - `parser_grammar_code`: Grammar parser factory
  - `PTNodeVisitor` subclasses for AST traversal
  - Semantic actions for each grammar rule
  - IR node generation logic
  - Symbol table building

- **`utils.py`**: Parsing utilities
  - Helper functions for AST manipulation
  - Common parsing patterns
  - Error recovery utilities
  - Token processing helpers

## Key Concepts

### Parsing Pipeline

```
Heather Source Code
        ↓
Grammar Rules (PEG)
        ↓
    Parser (Arpeggio)
        ↓
Parse Tree (Concrete Syntax Tree)
        ↓
  Visitor Pattern
        ↓
Semantic Actions
        ↓
Abstract Syntax Tree (AST)
        ↓
  IR Construction
        ↓
Intermediate Representation
```

### parse() Function

The main parsing entry point:

```python
def parse(
    grammar_parser: Callable[[Callable], ParserPEG | ParserPython],
    program_rule: Callable,
    raw_code: str,
    project_root: Path,
    module_path: Path,
    ir_graph: IRGraph,
) -> BaseIR
```

**Parameters**:
- **`grammar_parser`**: Factory function creating parser with grammar
- **`program_rule`**: Top-level grammar rule (e.g., `fn_program`)
- **`raw_code`**: Heather source code string
- **`project_root`**: Project root directory (for imports)
- **`module_path`**: Current module path
- **`ir_graph`**: IR graph to populate

**Process**:
1. **Initialize Parser**: Create parser with grammar and program rule
2. **Parse Source**: Generate parse tree from source code
3. **Create Visitor**: Instantiate AST visitor
4. **Visit Tree**: Traverse parse tree with semantic actions
5. **Build IR**: Construct IR nodes and add to graph
6. **Return**: Return complete IR representation

**Returns**:
- `BaseIR`: Root IR node for the parsed module

### parser_grammar_code

Factory function for creating the Heather parser:

```python
def parser_grammar_code(program_rule: Callable) -> ParserPython:
    """Create Arpeggio parser with Heather grammar"""
    return ParserPython(
        program_rule,
        ws=WHITESPACE,  # Whitespace handling
        skipws=True,    # Automatically skip whitespace
        debug=False     # Debug mode for development
    )
```

### Visitor Pattern

The visitor pattern separates grammar structure from semantic actions:

**Parse Tree Visitor**:
```python
class HeatherIRVisitor(PTNodeVisitor):
    def visit_function_def(self, node, children):
        """Called when visiting function definition"""
        # Extract function name, parameters, body
        # Construct FnDef IR node
        # Register in symbol table
        return fn_def_ir
    
    def visit_variable_decl(self, node, children):
        """Called when visiting variable declaration"""
        # Extract var name and type
        # Construct DeclareInstr IR node
        # Add to current scope
        return declare_ir
    
    # ... methods for each grammar rule
```

**Pattern Benefits**:
- Separates syntax from semantics
- Reusable visitor implementations
- Easy to extend with new actions
- Clean separation of concerns

### Semantic Actions

Each grammar rule has corresponding semantic action:

**Function Definition**:
```python
def visit_fn_def(self, node, children):
    # children = [name, params, return_type, body]
    fn_name = children[0]  # Symbol
    params = children[1]   # ArgsValuesBlock
    ret_type = children[2] # Type symbol
    body = children[3]     # BodyBlock
    
    # Construct function header
    header = FnHeader(fn_name, ret_type, param_types, param_names)
    
    # Build function definition IR
    fn_def = FnDef(header=header, body=body)
    
    # Register in IR graph
    ir_graph.add_function(fn_def)
    
    return fn_def
```

**Variable Declaration**:
```python
def visit_var_decl(self, node, children):
    # children = ['var', name, type]
    var_name = children[1]  # Symbol
    var_type = children[2]  # Type symbol
    
    # Create declaration IR
    declare_ir = DeclareInstr(name=var_name, type=var_type)
    
    return declare_ir
```

**Expression Evaluation**:
```python
def visit_bin_op(self, node, children):
    # children = [left, op, right]
    left_expr = children[0]
    operator = children[1]
    right_expr = children[2]
    
    # Create function call IR for operator
    call_ir = CallInstr(
        fn_name=operator_to_fn(operator),
        args=[left_expr, right_expr]
    )
    
    return call_ir
```

### AST Construction

The visitor constructs AST nodes that map to IR:

**AST Node Types**:
- **Terminals**: Leaf nodes (identifiers, literals, operators)
- **Non-Terminals**: Composite nodes (expressions, statements, blocks)

**AST to IR Mapping**:
```
Grammar Rule          AST Node              IR Node
───────────────────────────────────────────────────────
var_decl          → VariableDecl        → DeclareInstr
assignment        → Assignment          → AssignInstr
function_call     → FunctionCall        → CallInstr
cast_expr         → CastExpression      → CastInstr
literal           → LiteralNode         → Literal
```

### Symbol Table Building

During parsing, symbol tables are constructed:

**Process**:
1. **Encounter Declaration**: Variable, function, or type declaration
2. **Validate**: Check for redeclarations, type errors
3. **Register**: Add to appropriate symbol table
4. **Resolve References**: Link usages to declarations

**Scope Management**:
- Global scope: Module-level definitions
- Function scope: Function parameters and locals
- Block scope: Control flow block locals

### Type Resolution

Types are resolved during parsing:

**Type References**:
```heather
var x: u64        # Resolve 'u64' to built-in type
var p: Point      # Resolve 'Point' to user-defined type
```

**Resolution Process**:
1. Check built-in types (`builtins_types`)
2. Check user-defined types in symbol table
3. Check imported types
4. Error if unresolved

### Import Handling

The parser handles import statements:

```python
from hhat_lang.core.imports import TypeImporter, FnImporter
```

**Import Types**:
- **Type Imports**: Import type definitions from other modules
- **Function Imports**: Import function definitions

**Process**:
1. Parse import statement
2. Resolve module path
3. Parse imported module (recursive)
4. Extract requested definitions
5. Add to current symbol table

### IR Node Construction

The visitor creates IR nodes using Heather's IR classes:

**From `dialects/heather/code/simple_ir_builder/ir`**:
```python
from hhat_lang.dialects.heather.code.simple_ir_builder.ir import (
    IR,
    AssignInstr,
    CallInstr,
    CastInstr,
    DeclareAssignInstr,
    DeclareInstr,
)
```

**Construction Examples**:

**Variable Declaration**:
```python
ir_node = DeclareInstr(
    name=Symbol("x"),
    type=Symbol("u64")
)
```

**Assignment**:
```python
ir_node = AssignInstr(
    target=Symbol("x"),
    value=Literal(42, lit_type="u64")
)
```

**Function Call**:
```python
ir_node = CallInstr(
    fn_name=Symbol("add"),
    args=[
        Symbol("x"),
        Symbol("y")
    ]
)
```

### Error Handling

The parser handles syntax and semantic errors:

**Syntax Errors**:
- Invalid grammar (caught by Arpeggio)
- Unexpected tokens
- Missing required elements

**Semantic Errors**:
- Undefined variable reference
- Type mismatch
- Redeclaration
- Invalid operations

**Error Reporting**:
```python
from hhat_lang.core.error_handlers.errors import ErrorHandler

if undefined_variable:
    raise UndefinedVariableError(var_name, line, column)
```

Errors include:
- Line and column numbers
- Error message
- Source code context
- Suggestions for fixes

### Parse Tree vs. AST

**Parse Tree** (Concrete Syntax Tree):
- Represents exact source code structure
- Includes all tokens and whitespace
- One-to-one with grammar rules

**AST** (Abstract Syntax Tree):
- Simplified representation
- Omits syntactic noise
- Focuses on semantic structure

The visitor converts Parse Tree → AST → IR.

## Connections

- **`dialects/heather/grammar`**: Uses grammar rules for parsing
- **`dialects/heather/code`**: Constructs Heather IR nodes
- **`dialects/heather/compiler`**: Invoked by compiler for parsing
- **`core/code`**: Uses core IR abstractions (`IRGraph`, `IRNode`)
- **`core/data`**: Creates data representations (`Symbol`, `Literal`)
- **`core/types`**: Resolves type references (`builtins_types`)
- **`core/imports`**: Handles module imports
- **`core/error_handlers`**: Reports parsing errors

## Usage Context

The parsing module is used during:

- **Compilation**: Converting source to IR
- **REPL**: Parsing interactive commands
- **IDE Integration**: Syntax checking, auto-completion
- **Linting**: Static analysis
- **Documentation**: Code analysis tools

## Performance Considerations

**Parser Performance**:
- PEG parsing can be slow for complex grammars
- Consider memoization for repeated sub-parses
- Profile grammar rules for bottlenecks

**Memory Usage**:
- Parse trees can be large
- Visitor pattern allows streaming (no full tree in memory)
- IR construction can be incremental

**Optimization Strategies**:
- Cache parsed modules
- Incremental parsing for edits
- Parallel parsing of independent modules

## Extension Guidelines

To extend parsing functionality:

1. **Add Grammar Rules**:
   - Define new rules in `grammar/`
   - Update program rule composition

2. **Implement Visitor Methods**:
   - Add `visit_*` method for new rule
   - Extract relevant information from children
   - Construct appropriate IR nodes

3. **Handle New IR Nodes**:
   - Define IR node in `code/`
   - Create construction logic in visitor

4. **Update Type System**:
   - Add new type patterns to type resolution
   - Handle new type syntax

5. **Test**:
   - Write parser tests for new syntax
   - Verify IR construction correctness
   - Check error handling

## Debugging

Debugging parsing issues:

**Enable Debug Mode**:
```python
parser = ParserPython(program_rule, debug=True)
```

**Inspect Parse Tree**:
```python
parse_tree = parser.parse(source_code)
print(parse_tree.tree_str())  # Pretty-print tree
```

**Trace Visitor**:
```python
class DebuggingVisitor(PTNodeVisitor):
    def visit_*( self, node, children):
        print(f"Visiting: {node.rule_name}")
        # ... visit logic
```

**Common Issues**:
- Grammar rule conflicts
- Incorrect visitor return values
- Missing semantic actions
- Type resolution failures

## Future Enhancements

Potential improvements:

- **Error Recovery**: Continue parsing after errors
- **Incremental Parsing**: Re-parse only changed sections
- **Parallel Parsing**: Parse independent modules concurrently
- **Better Error Messages**: More context, suggestions
- **Parse Caching**: Cache parsed modules for faster recompilation
- **Lazy Parsing**: Parse on-demand for large codebases
- **Syntax Macros**: User-defined syntax extensions
