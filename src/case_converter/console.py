import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
@click.argument("filename")
def main():
    """Convert the case of your code."""
    click.echo("Hello, world!")
