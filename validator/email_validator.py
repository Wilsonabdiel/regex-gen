import re
import click

@click.group()
def cli():
    pass



@cli.command()
@click.argument('email')
def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False



@cli.command()
@click.argument('email')
def validate(email):
    if validate_email(email):
        click.echo(f'{email} is a valid email address.')
    else:
        click.echo(f'{email} is not a valid email address.')
