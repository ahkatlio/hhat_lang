# Toolchain

The `toolchain` module provides development tools, utilities, and infrastructure for working with H-hat projects, including command-line interfaces, project management, configuration handling, and notebook integration.

## Overview

This module contains the practical tools developers use to:
- Create and manage H-hat projects
- Run and compile H-hat programs
- Configure project settings
- Work with Jupyter notebooks
- Use command-line interfaces

## Structure

### Subdirectories

#### `cli/`
Command-line interface for H-hat

**Files**:
- **`cli.py`**: Main CLI implementation
  - Command parsing and dispatch
  - User interaction
  - Help system
  - Error reporting

**Commands** (typical):
```bash
hhat new my_project       # Create new project
hhat run main.hat         # Run H-hat program
hhat compile program.hat  # Compile to IR
hhat test                 # Run tests
hhat repl                 # Start interactive REPL
```

**Features**:
- Argument parsing
- Command validation
- Output formatting
- Progress indicators
- Colored output

#### `config/`
Configuration management

**Purpose**:
- Load and parse configuration files
- Validate configuration settings
- Provide default configurations
- Environment-specific settings

**Configuration Types**:
- **Project Config**: Project-level settings
- **User Config**: User preferences
- **System Config**: System-wide defaults
- **Backend Config**: Quantum backend settings

**Example Configuration**:
```json
{
  "project_name": "my_quantum_app",
  "dialect": "heather",
  "version": "0.1.0",
  "quantum": {
    "backend": "qiskit",
    "device": "ibmq_manila",
    "shots": 1024
  },
  "paths": {
    "source": "src",
    "types": "hat_types",
    "docs": "docs"
  }
}
```

#### `project/`
Project creation and management

**Files**:
- **`new.py`**: Create new H-hat projects
- **`run.py`**: Run H-hat programs
- **`update.py`**: Update project structure/dependencies
- **`utils.py`**: Project utilities

**Project Structure Constants**:
```python
SOURCE_FOLDER_NAME = "src"
TYPES_FOLDER_NAME = "hat_types"
IMPORTS_FOLDER_NAME = ".hat_imports"
DOCS_FOLDER_NAME = "docs"
TESTS_FOLDER_NAME = "tests"
PROOFS_FOLDER_NAME = "proofs"
MAIN_FILE_NAME = "main.hat"
```

**Standard Project Layout**:
```
my_project/
├── src/
│   ├── main.hat
│   ├── hat_types/
│   └── .hat_imports/
├── docs/
│   ├── main.hat.md
│   └── hat_types/
├── tests/
├── proofs/
└── config.json
```

#### `notebooks/`
Jupyter notebook integration

**Purpose**:
- Run H-hat in Jupyter notebooks
- Interactive quantum programming
- Educational materials
- Exploratory development

**Features**:
- Cell-by-cell execution
- Result visualization
- State inspection
- Interactive debugging

**Usage**:
```python
# In Jupyter notebook
from hhat_lang.toolchain.notebooks import HhatKernel

# Write H-hat code in cells
%%heather
var x: u64 = 42
::print(x)
```

## Key Concepts

### Project Lifecycle

**Creation**:
```bash
hhat new quantum_algorithm
cd quantum_algorithm
```

Creates standard project structure with:
- Source directory
- Type definitions folder
- Documentation folder
- Configuration file
- Example main file

**Development**:
```bash
hhat run src/main.hat        # Run program
hhat compile src/module.hat  # Compile module
hhat test                    # Run test suite
```

**Building**:
```bash
hhat build --release         # Production build
hhat build --optimize        # Optimized build
```

### Configuration Management

**Configuration Hierarchy**:
1. **System Defaults**: Built-in defaults
2. **User Config**: `~/.hhat/config.json`
3. **Project Config**: `./config.json`
4. **Environment Variables**: `HHAT_*`
5. **Command-line Args**: Override all

**Precedence**: Command-line > Environment > Project > User > System

**Loading Configuration**:
```python
from hhat_lang.core.config.base import HhatProjectSettings
from pathlib import Path

settings = HhatProjectSettings(project_root=Path("/path/to/project"))

# Access settings
print(settings.project_name)
print(settings.dialect)
print(settings.quantum_backend)
```

### Path Management

The toolchain defines standard paths:

**Source Paths**:
- `SOURCE_FOLDER_NAME`: "src" - Source code location
- `TYPES_FOLDER_NAME`: "hat_types" - Type definitions
- `IMPORTS_FOLDER_NAME`: ".hat_imports" - Cached imports

**Documentation Paths**:
- `DOCS_FOLDER_NAME`: "docs" - Documentation
- `MAIN_DOC_FILE_NAME`: "main.hat.md" - Main docs

**Computed Paths**:
- `MAIN_PATH`: Path to main file
- `SOURCE_TYPES_PATH`: Path to type definitions
- `DOCS_TYPES_PATH`: Path to type documentation

**Usage**:
```python
from hhat_lang.toolchain.project import SOURCE_FOLDER_NAME, MAIN_PATH

project_root = Path("/path/to/project")
source_dir = project_root / SOURCE_FOLDER_NAME
main_file = project_root / MAIN_PATH
```

### CLI Commands

Typical CLI structure:

**Global Options**:
```bash
hhat --version          # Show version
hhat --help             # Show help
hhat --verbose          # Verbose output
hhat --quiet            # Minimal output
```

**Project Commands**:
```bash
hhat new <name>         # Create project
hhat init               # Initialize in existing directory
hhat update             # Update project structure
```

**Compilation Commands**:
```bash
hhat compile <file>     # Compile to IR
hhat build              # Build project
hhat check              # Type check without building
```

**Execution Commands**:
```bash
hhat run <file>         # Run program
hhat test               # Run tests
hhat bench              # Run benchmarks
```

**Interactive Commands**:
```bash
hhat repl               # Start REPL
hhat notebook           # Start Jupyter notebook
```

**Documentation Commands**:
```bash
hhat doc                # Generate documentation
hhat doc --serve        # Serve documentation locally
```

### Project Templates

Project creation supports templates:

**Basic Template**:
```
project/
├── src/
│   └── main.hat
├── config.json
└── README.md
```

**Library Template**:
```
library/
├── src/
│   ├── lib.hat
│   └── hat_types/
├── tests/
├── docs/
└── config.json
```

**Application Template**:
```
app/
├── src/
│   ├── main.hat
│   ├── modules/
│   └── hat_types/
├── resources/
├── config.json
└── README.md
```

**Template Selection**:
```bash
hhat new --template=library my_lib
hhat new --template=app my_app
```

### Notebook Integration

**Jupyter Magic Commands**:
```python
%%heather               # Heather code cell
%%hhat --backend=qiskit # Specify backend
%%hhat --shots=2048     # Set execution parameters
```

**IPython Integration**:
```python
from hhat_lang.toolchain.notebooks import load_ipython_extension

# Automatically loaded in Jupyter
%load_ext hhat_lang.toolchain.notebooks
```

**Features**:
- Syntax highlighting
- Auto-completion
- Inline documentation
- Result visualization
- State inspection

## Connections

- **`core/compiler`**: CLI invokes compiler for compilation
- **`core/execution`**: CLI invokes executor for running programs
- **`core/config`**: Uses configuration system
- **`dialects/*`**: Works with all dialect implementations
- **`low_level/*`**: Configures backends through toolchain

## Usage Context

The toolchain is used for:

- **Project Setup**: Creating new projects
- **Daily Development**: Running and testing code
- **Build Automation**: CI/CD integration
- **Interactive Exploration**: REPL and notebooks
- **Documentation**: Generating and viewing docs

## CLI Implementation

**Entry Point**:
```python
# In cli.py
import typer

app = typer.Typer()

@app.command()
def run(file: str, backend: str = "qiskit", shots: int = 1024):
    """Run an H-hat program"""
    # Load configuration
    # Compile program
    # Execute
    # Display results

@app.command()
def new(name: str, template: str = "basic"):
    """Create new H-hat project"""
    # Create directory structure
    # Generate config file
    # Create initial files
    
if __name__ == "__main__":
    app()
```

**Usage**:
```bash
python -m hhat_lang.toolchain.cli run main.hat
# or after installation:
hhat run main.hat
```

## Configuration Schema

Typical configuration structure:

```json
{
  "project": {
    "name": "string",
    "version": "semver",
    "description": "string",
    "authors": ["string"],
    "license": "string"
  },
  "dialect": "heather",
  "compiler": {
    "optimization_level": "0-3",
    "warnings": "boolean",
    "strict": "boolean"
  },
  "execution": {
    "default_backend": "string",
    "shots": "integer",
    "timeout": "integer"
  },
  "quantum": {
    "backends": {
      "qiskit": {...},
      "squidasm": {...}
    }
  },
  "paths": {
    "source": "string",
    "types": "string",
    "docs": "string",
    "tests": "string"
  }
}
```

## Extension Guidelines

To extend the toolchain:

1. **Add CLI Commands**:
   ```python
   @app.command()
   def my_command(arg: str):
       """My custom command"""
       # Implementation
   ```

2. **Add Project Templates**:
   - Create template directory structure
   - Define template metadata
   - Register template

3. **Extend Configuration**:
   - Add new config sections
   - Update schema validation
   - Document new options

4. **Add Utilities**:
   - Implement in `project/utils.py`
   - Export from module
   - Document usage

## Future Enhancements

Potential toolchain improvements:

- **Package Manager**: Dependency management and package registry
- **IDE Integration**: Language server protocol (LSP) support
- **Debugger**: Interactive debugging tools
- **Profiler**: Performance analysis
- **Linter**: Code quality checks
- **Formatter**: Code formatting
- **Plugin System**: Extensible toolchain
- **Cloud Integration**: Deploy to quantum cloud platforms
- **Collaboration**: Team development features
- **Version Control**: Git integration
- **CI/CD Templates**: Automated build and test pipelines
