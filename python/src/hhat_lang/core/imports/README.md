# Imports

The `imports` module handles H-hat's module and file import system, enabling code reuse and modular program organization through local and remote resource loading.

## Overview

This module provides the infrastructure for:
- Importing external H-hat source files
- Loading modules and libraries
- Resolving import paths (absolute and relative)
- Parsing and integrating imported code into the current program
- Managing project-level imports

## Structure

### Files

- **`importer.py`**: Core import functionality (289 lines)
  - `BaseImporter`: Abstract base class for import systems
  - Path resolution (project root, source folders)
  - Parser integration for imported files
  - IR graph construction from imported modules
  - Built-in function path management

- **`utils.py`**: Import utilities
  - Helper functions for import operations
  - Path manipulation utilities
  - Import validation

## Key Concepts

### BaseImporter

The `BaseImporter` class coordinates the import process:

**Key Attributes**:
- `_base`: Base path for relative imports
- `_project_root`: Root directory of the H-hat project
- `_parser_fn`: Function to parse imported source files
- `_grammar_parser`: Grammar definition for the dialect
- `_program_rule`: Top-level parsing rule

**Responsibilities**:
1. Resolve import paths (relative vs. absolute)
2. Locate source files in project structure
3. Parse imported files using dialect's grammar
4. Generate IR from parsed imports
5. Integrate imported definitions into current scope

### Import Path Resolution

Imports can be specified as:

**Absolute imports**:
```
import /project/module/submodule
```

**Relative imports**:
```
import ./sibling_module
import ../parent_module/sibling
```

The importer resolves these to file system paths using:
- `_project_root`: Base for absolute paths
- `_base`: Current file directory for relative paths
- `SOURCE_FOLDER_NAME`: Standard source folder name
- `SOURCE_TYPES_PATH`: Standard types folder path

### Import Workflow

1. **Parse Import Statement**: Extract import path from source code
2. **Resolve Path**: Convert to absolute file system path
3. **Locate File**: Find `.hat` file in project structure
4. **Parse File**: Use dialect's grammar to parse imported file
5. **Generate IR**: Convert parsed AST to IR representation
6. **Integrate**: Add imported definitions to current IR graph
7. **Register**: Update symbol tables with imported names

### Parser Integration

The importer integrates with the parsing infrastructure:

```python
_parser_fn: Callable[
    [
        Callable[[Callable], ParserPEG | ParserPython],  # Grammar parser
        Callable,                                         # Program rule
        str,                                              # Source code
        Path,                                             # File path
        Path,                                             # Project root
        IRGraph,                                          # Target IR graph
    ],
    BaseIR,
]
```

This allows imported files to be parsed using the same machinery as the main program.

### Project Structure Integration

The importer understands H-hat project structure:
```
project_root/
├── src/           # SOURCE_FOLDER_NAME
│   ├── main.hat
│   ├── types/     # SOURCE_TYPES_PATH
│   └── modules/
└── config/
```

Import resolution considers:
- Standard source directory locations
- Type definition locations
- Module organization conventions

### Built-in Module Imports

The `builtin_fns_path` from `core.fns` is accessible to importers, enabling:
- Import of core library functions
- Standard library modules
- Dialect-specific built-ins

## Connections

- **`core/compiler`**: Compiler invokes importer when encountering import statements
- **`core/code`**: Imported code generates IR nodes and graphs
- **`toolchain/project`**: Uses project structure constants (`SOURCE_FOLDER_NAME`, `SOURCE_TYPES_PATH`)
- **`core/fns`**: Accesses `builtin_fns_path` for built-in module imports
- **`core/memory`**: Imported definitions added to symbol tables
- **Parsing**: Uses Arpeggio (`ParserPEG`, `ParserPython`) for grammar-based parsing
- **Dialects**: Each dialect implements its own importer extending `BaseImporter`

## Usage Context

Imports are processed during:

- **Compilation**: Before evaluating main program
- **Module Loading**: When import statements are encountered
- **Dependency Resolution**: Building import dependency graph
- **REPL**: Dynamic imports in interactive sessions

## Import Types

### Local Imports
Import files from the same project:
```
import ./utils
import ../shared/common
```

### Module Imports
Import from standard or third-party modules:
```
import /core/math
import /quantum/gates
```

### Built-in Imports
Import standard library functionality:
```
import /std/io
import /std/collections
```

## Extension Guidelines

To implement a dialect-specific importer:

1. **Extend BaseImporter**:
   ```python
   class HeatherImporter(BaseImporter):
       def __init__(self, project_root, grammar_parser, program_rule, parser_fn):
           super().__init__(project_root, grammar_parser, program_rule, parser_fn)
   ```

2. **Implement Path Resolution**:
   - Handle dialect-specific path conventions
   - Support custom module locations

3. **Integrate with Parser**:
   - Use dialect's grammar for parsing imports
   - Generate dialect-compatible IR

4. **Handle Special Imports**:
   - Dialect-specific built-ins
   - External library interfaces

5. **Error Handling**:
   - File not found errors
   - Parse errors in imported files
   - Circular dependency detection

## Future Extensions

Potential import system enhancements:
- Remote imports (HTTP/HTTPS URLs)
- Package management integration
- Cached/compiled imports
- Conditional imports
- Wildcard imports
- Selective imports (import specific symbols)
