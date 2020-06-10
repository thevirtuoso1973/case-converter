import click

from . import __version__, converters

@click.command()
@click.version_option(version=__version__)
@click.argument("inp", type=click.Path(exists=True, allow_dash=True),
                default="-")
@click.option("-o", "--output", type=click.Path(exists=True, allow_dash=True),
              default="-", show_default=True)
@click.option("-f", "--from", "from_",
              type=click.Choice([converters.Case.CAMEL.value,
                                 converters.Case.SNAKE.value,
                                 converters.Case.KEBAB.value],
                                case_sensitive=False),
              prompt=True)
@click.option("-t", "--to",
              type=click.Choice([converters.Case.CAMEL.value,
                                 converters.Case.SNAKE.value,
                                 converters.Case.KEBAB.value],
                                case_sensitive=False),
              prompt=True)
@click.option("-e", "--encoding", default="UTF-8", show_default=True)
def main(inp, output, from_, to, encoding):
    """
    Convert the case of your code.
    Takes plaintext from stdin and prints to stdout by default.
    """
    try:
        with click.open_file(inp, "r", encoding) as inStream, \
            click.open_file(inp, "w", encoding) as outStream:
            if to == converters.Case.CAMEL.value:
                converters.convertToCamel(inStream, outStream, from_)
            elif to == converters.Case.SNAKE.value:
                converters.convertToSnake(inStream, outStream, from_)
            elif to == converters.Case.KEBAB.value:
                converters.convertToKebab(inStream, outStream, from_)
            else:
                click.echo("Something went wrong.")
    except LookupError:
        click.echo("Invalid encoding.")
