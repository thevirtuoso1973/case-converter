import click

from . import __version__, converters
from .regex import Case

@click.command()
@click.version_option(version=__version__)
@click.argument("filename", type=click.Path(exists=True, allow_dash=True),
                default="-")
@click.option("-o", "--output", type=click.Path(allow_dash=True),
              default="-", show_default=True, help="file to output to")
@click.option("-f", "--from", "from_",
              type=click.Choice([Case.CAMEL.value,
                                 Case.SNAKE.value,
                                 Case.KEBAB.value],
                                case_sensitive=False),
              prompt=True, help="case of the input file")
@click.option("-t", "--to",
              type=click.Choice([Case.CAMEL.value,
                                 Case.SNAKE.value,
                                 Case.KEBAB.value],
                                case_sensitive=False),
              prompt=True, help="desired case")
@click.option("-e", "--encoding", default="UTF-8", show_default=True,
              help="the encoding of the input, also used for output")
def main(filename, output, from_, to, encoding):
    """
    Convert the case of matched text in FILENAME.

    Takes plaintext from stdin and prints to stdout by default.
    """
    try:
        if filename != "-" and filename == output:
            with click.open_file(filename, "r+", encoding) as inStream:
                if to == Case.CAMEL.value:
                    converters.convertToCamel(inStream, inStream, from_)
                elif to == Case.SNAKE.value:
                    converters.convertToSnake(inStream, inStream, from_)
                elif to == Case.KEBAB.value:
                    converters.convertToKebab(inStream, inStream, from_)
                else:
                    click.echo("Something went wrong.")
        else:
            with click.open_file(filename, "r", encoding) as inStream, \
                click.open_file(output, "w", encoding) as outStream:
                if to == Case.CAMEL.value:
                    converters.convertToCamel(inStream, outStream, from_)
                elif to == Case.SNAKE.value:
                    converters.convertToSnake(inStream, outStream, from_)
                elif to == Case.KEBAB.value:
                    converters.convertToKebab(inStream, outStream, from_)
                else:
                    click.echo("Something went wrong.")
    except LookupError:
        click.echo("Invalid encoding.")
