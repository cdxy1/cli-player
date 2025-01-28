#!/usr/bin/python

import time

import click

from core.files import init_main_dir, check_main_dir
from core.cli import select_menu, select_playlist, make_playlist


@click.group
def cli():
    pass


@cli.command()
def start():
    if not check_main_dir():
        init_main_dir()

    while True:
        choice = select_menu()

        match choice:
            case 1:
                if not select_playlist():
                    click.secho("There is nothing!", bold=True, fg="yellow")
                    time.sleep(0.5)
                    continue
            case 2:
                make_playlist()


if __name__ == "__main__":
    cli()
