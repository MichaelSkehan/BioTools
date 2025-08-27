import click
from primer.primer import Primer

@click.command()
@click.argument("sequences", nargs=-1)
def main(sequences):
    """CLI tool to analyze a DNA primer sequence."""
    if not sequences:
        click.echo("No sequences provided.", err=True)
        return
    for seq in sequences:
        primer = Primer(seq)
        click.echo(primer.report())
        click.echo("-"*40)

if __name__ == "__main__":
    main()