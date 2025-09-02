import click
from parse_csv import parse_csv
from restriction_digest import digest
from adaptor_ligation import ligate

@click.command()
@click.argument("input_file", type=click.Path(exists=True))

