"""
Setup script to register the Heather lexer with Pygments.

This script can be run to install the Heather lexer as a Pygments plugin,
making it available for syntax highlighting in MkDocs and other tools.

Usage:
    python -m hhat_lang.dialects.heather.toolchain.pygments.setup_pygments
"""

from __future__ import annotations


def register_lexer() -> None:
    """
    Register the Heather lexer with Pygments.
    
    This makes the lexer available under the aliases:
    - heather
    - hhat
    - hhat-heather
    """
    try:
        from pygments.lexers import _mapping, get_lexer_by_name
        
        # Check if lexer is already registered
        try:
            lexer = get_lexer_by_name("heather")
            print("✓ Heather lexer is already registered")
            print(f"  Name: {lexer.name}")
            print(f"  Aliases: {', '.join(lexer.aliases)}")
        except Exception:
            # Register the lexer
            lexer_info = (
                "hhat_lang.dialects.heather.toolchain.pygments.lexer",
                "Heather",
                ("heather", "hhat", "hhat-heather"),
                ("*.hat", "*.hhat"),
                ("text/x-heather", "text/x-hhat"),
            )
            
            _mapping.LEXERS["HeatherLexer"] = lexer_info
            
            print("✓ Heather lexer registered successfully")
            print("  Aliases: heather, hhat, hhat-heather")
            print("  File extensions: *.hat, *.hhat")
        
    except ImportError:
        print("✗ Pygments is not installed. Install it with:")
        print("  pip install pygments")


def verify_lexer() -> bool:
    """
    Verify that the Heather lexer works correctly.
    
    Returns:
        True if the lexer is working, False otherwise.
    """
    try:
        from pygments import highlight
        from pygments.formatters import TerminalFormatter
        from pygments.lexers import get_lexer_by_name
        
        # Get the lexer
        lexer = get_lexer_by_name("heather")
        
        # Test code
        test_code = '''
// Simple Heather program
main { print("Hello quantum world!") }

fn add(a:i32 b:i32) i32 {
    ::sum(a b)
}

type point { x:i32 y:i32 }

const pi:f64 = 3.141592653589793
'''
        
        # Try to highlight
        result = highlight(test_code, lexer, TerminalFormatter())
        
        print("\n✓ Lexer verification successful!")
        print("\nSample highlighted code:")
        print(result)
        
        return True
        
    except Exception as e:
        print(f"\n✗ Lexer verification failed: {e}")
        return False


def main() -> None:
    """Main entry point for the setup script."""
    print("H-hat Heather Lexer Setup")
    print("=" * 50)
    
    register_lexer()
    print()
    verify_lexer()
    
    print("\nTo use in MkDocs, add to mkdocs.yml:")
    print("```yaml")
    print("markdown_extensions:")
    print("  - pymdownx.superfences:")
    print("      custom_fences:")
    print("        - name: heather")
    print("          class: heather")
    print("          format: !!python/name:pymdownx.superfences.fence_code_format")
    print("```")
    print("\nThen use in markdown:")
    print("```heather")
    print("main { print(\"Hello quantum!\") }")
    print("```")


if __name__ == "__main__":
    main()
