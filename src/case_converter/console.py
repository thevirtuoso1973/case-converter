import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
@click.argument("inp", type=click.Path(exists=True, allow_dash=True),
                default="-")
@click.option("-o", "--output", type=click.Path(exists=True, allow_dash=True),
              default="-")
@click.option("-f", "--from", "from_")
@click.option("-t", "--to")
@click.option("-e", "--encoding", default="UTF-8")
def main(inp, output, from_, to, encoding):
    """
    Convert the case of your code.
    Takes plaintext from stdin and prints to stdout by default.
    """
    try:
        with click.open_file(inp, 'r', encoding) as inStream, \
            click.open_file(inp, 'w', encoding) as outStream:
            outStream.write(inStream.read())
    except LookupError:
        click.echo("Invalid encoding.")
