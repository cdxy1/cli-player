import click

from core.files import init_main_dir, check_main_dir
from core.cli import select_menu, select_playlist, make_playlist


@click.group
def cli():
    pass


@cli.command()
def start():
    if not check_main_dir:
        path = click.prompt(
            click.style("Enter default dir path or leave blank", bold=True),
            type=str,
            default="",
        )
        init_main_dir(path)

    while True:
        choice = select_menu()

        if choice == 1:
            select_playlist()
        elif choice == 2:
            make_playlist()


if __name__ == "__main__":
    cli()
