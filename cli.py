import click
from primer import Primer

@click.command()
@click.argument("sequence")
def main(sequence):
    """CLI tool to analyze a DNA primer sequence."""
    primer = Primer(sequence)
    click.echo(primer.report())

if __name__ == "__main__":
    main()