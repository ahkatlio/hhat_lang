# Development Setup

This guide will help you set up your development environment for contributing to H-hat.

!!! warning

    The Python project is currently on halt. The Rust implementation is the primary focus for development.

## Prerequisites

### For Rust Development (Recommended)

You'll need:

- **Rust**: 1.70 or later (install via [rustup](https://rustup.rs/))
- **Git**: For version control
- **A code editor**: VS Code, IntelliJ IDEA, or your preferred editor

### For Python Development (Reference Only)

The Python implementation is on hold, but if you want to explore it:

- **Python**: 3.12 or later
- **Git**: For version control

## Clone the Repository

```bash
git clone https://github.com/hhat-lang/hhat_lang.git
cd hhat_lang
```

## Rust Setup

### 1. Install Rust

If you haven't already:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Verify installation:

```bash
rustc --version
cargo --version
```

### 2. Navigate to Rust Project

```bash
cd rust/hhat_lang
```

### 3. Build the Project

```bash
cargo build
```

This will:

- Download dependencies
- Compile the project
- Create a debug binary in `target/debug/`

### 4. Run Tests

```bash
cargo test
```

### 5. Run the Compiler

```bash
cargo run -- --help
```

### Development Tools

For VS Code, install the **rust-analyzer** extension for better Rust development experience.

Run clippy to catch common mistakes:

```bash
cargo clippy
```

Format code according to Rust conventions:

```bash
cargo fmt
```

## Python Setup (Reference)

!!! note

    Python development is currently on hold. This section is for reference.

### 1. Navigate to Python Project

```bash
cd python
```

### 2. Create Virtual Environment

Using venv:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Using conda:

```bash
conda create -n hhat python=3.12
conda activate hhat
```

### 3. Install Dependencies

For full access to H-hat's Python development tools:

```bash
# For bash/sh
pip install -e .[all,dev]

# For zsh (need quotes)
pip install -e ".[all,dev]"
```

### 4. Install Pre-commit Hooks

```bash
pre-commit install
```

This ensures code formatting and checks run automatically before commits.

### 5. Run Tests

```bash
pytest
```

### Python Tools

#### Formatting and Linting

The project uses pre-commit hooks defined in `.pre-commit-config.yaml`:

- **black**: Code formatter
- **isort**: Import sorter
- **flake8**: Style checker
- **mypy**: Type checker

Run manually:

```bash
pre-commit run --all-files
```

## IDE Setup

### Visual Studio Code

Recommended extensions:

- **rust-analyzer**: Rust language support
- **Python** (if working with Python code)
- **Even Better TOML**: TOML file support
- **Markdown All in One**: Markdown editing
- **GitLens**: Enhanced Git integration

Workspace settings (`.vscode/settings.json`):

```json
{
  "rust-analyzer.cargo.features": "all",
  "editor.formatOnSave": true,
  "rust-analyzer.checkOnSave.command": "clippy"
}
```

### IntelliJ IDEA / CLion

Install plugins:

- **Rust**: Rust language support
- **TOML**: TOML file support

Configure Rust toolchain in Settings → Languages & Frameworks → Rust.

## Testing Documentation Locally

If you're working on documentation and want to preview changes locally:

### Install MkDocs

```bash
pip install mkdocs-material
pip install mkdocs-blog-plugin
```

### Serve Documentation

```bash
mkdocs serve
```

Visit [http://localhost:8000](http://localhost:8000) to preview.

### Build Documentation

```bash
mkdocs build
```

Output is in `site/` directory.

## Git Workflow

### Branch Naming Convention

Branch naming conventions are project-specific. Common patterns include:

- `impl/<description>-<issue-number>` for general implementations
- `dev/python_impl/<description>` for Python-specific work
- `dev/rust_impl/<description>` for Rust-specific work

Consult with maintainers on Discord about branch naming for your specific contribution.

Examples from recent work:

- `impl/add-python-readmes-93`
- `impl/reorganize-docs-95`

### Create a Feature Branch

```bash
git checkout main
git pull origin main
git checkout -b impl/your-feature-123
```

### Make Changes

```bash
# Edit files
git add .
git commit -m "Brief description of changes"
```

### Push Changes

```bash
git push origin impl/your-feature-123
```

### Create Pull Request

1. Go to [GitHub repository](https://github.com/hhat-lang/hhat_lang)
2. Click "Pull Requests" → "New Pull Request"
3. Select your branch
4. Fill in PR description
5. Link related issues

## Code Quality Checks

### Before Committing

For Rust:

```bash
cargo fmt
cargo clippy
cargo test
```

For Python:

```bash
pre-commit run --all-files
pytest
```

### CI/CD

Pull requests automatically run:

- Formatting checks
- Linter checks
- Test suite
- Build verification

Fix any CI failures before merging.

## Troubleshooting

### Rust Build Fails

**Problem**: Compilation errors

**Solution**:

- Update Rust: `rustup update`
- Clean build: `cargo clean && cargo build`
- Check Rust version: `rustc --version`

### Python Import Errors

**Problem**: Cannot import hhat_lang modules

**Solution**:

- Ensure virtual environment is activated
- Install in editable mode: `pip install -e .`
- Check Python path: `python -c "import sys; print(sys.path)"`

### Documentation Not Building

**Problem**: MkDocs errors

**Solution**:

- Install dependencies: `pip install -r requirements.txt`
- Check mkdocs.yml syntax
- Verify all referenced files exist

## Getting Help

If you encounter issues:

1. Check existing [GitHub issues](https://github.com/hhat-lang/hhat_lang/issues)
2. Ask on [Discord #h-hat channel](http://discord.unitary.foundation)
3. Create a new issue with details about your problem

## Next Steps

- Read [How to Contribute](../how_contribute.md)
- Browse [open issues](https://github.com/hhat-lang/hhat_lang/issues)
- Join the [community](../community/get_involved.md)
- Start with a [good first issue](https://github.com/hhat-lang/hhat_lang/issues?q=is%3Aissue+state%3Aopen+label%3A%22good+first+issue%22)
