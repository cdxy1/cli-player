import click

from core.music import test_play


@click.group
def cli():
    pass


@cli.command()
def start():
    click.echo("click is working")


@cli.command()
def test():
    value = click.prompt("Please eneter something", type=str)
    for _ in range(1):
        click.echo(value)
        test_play()


if __name__ == "__main__":
    cli()
