# case-converter
Convert the case of names/identifiers in your source code.

# Install
`poetry build` from the root project directory and `pip install --user [the wheel file]`,
where [the wheel file] is the generated wheel file.

# Usage
`case-converter [OPTIONS] [FILENAME]`

Use `case-converter --help` for full help info.

# Supported Cases
- camelCase (aka. lowerCaseWithCapitalDelimiters)
- snake_case (aka. lower_case_with_underscores)
- kebab-case (aka. lower-case-with-hyphens)

# Potential Future Support
- PascalCase
- SCREAMING_SNAKE_CASE
- Camel_Snake_Case

# Development

Run tests with `poetry run pytest` in the root project directory.
