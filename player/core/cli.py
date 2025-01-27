import click
from inputimeout import inputimeout, TimeoutOccurred

from core.files import (
    make_playlist_dir,
    playlists_list,
    select_pl_dir,
)


def select_menu():
    while True:
        click.clear()
        click.echo(
            f"{click.style('Select or create playlist:', bold=True)}\n 1. Select playlist\n 2. Create playlist\n"
        )
        choice = click.prompt(click.style("Enter a number", bold=True), type=int)
        if choice not in (1, 2):
            click.clear()
            click.secho("Enter 1 or 2, please!", bold=True, fg="yellow")
            continue
        else:
            return choice


def make_playlist():
    pl_lst = playlists_list()
    while True:
        name = click.prompt(
            click.style("Enter a name of playlist", bold=True), type=str
        )
        if not isinstance(name, str):
            click.clear()
            click.secho("Name must be string!", bold=True, fg="yellow")
            continue
        elif name in pl_lst.keys():
            click.clear()
            click.secho("The playlist name is already exists.", bold=True, fg="yellow")
            continue
        else:
            make_playlist_dir(name)
            return


def show_playlists():
    pl_lst = playlists_list()
    click.clear()
    click.echo(f"{click.style('Playlists', bold=True)}:\n==========")
    for num, key in enumerate(pl_lst.keys()):
        click.echo(f"{click.style(num, bold=True)}. {key.title()}")
    else:
        click.echo("==========\n")

    return pl_lst


def playlist_ended(lst, num):
    flag = True
    current_num = num
    menu = f"{click.style('What next?', bold=True)}:\n1. Next playlist\n2. Retry current playlist\n3. Choose another playlist\n"

    click.clear()

    while True:
        for sec in range(10, 0, -1):
            if flag:
                click.clear()
                click.secho(menu)
                click.echo(
                    f"{click.style('Press', bold=True)} {click.style('enter', fg='yellow')} {click.style('to select option.', bold=True)} S({sec})",
                )

                try:
                    if _ := inputimeout(timeout=1):
                        import sys, termios

                        flag = False
                        termios.tcflush(sys.stdin, termios.TCIFLUSH)
                except TimeoutOccurred:
                    continue
            else:
                click.clear()
                click.echo(menu)
                step = click.prompt(click.style("Enter a action", bold=True), type=int)
                break
        else:
            step = 1

        match step:
            case 1:
                try:
                    select_pl_dir(lst, current_num + 1)
                    current_num += 1
                    flag = True
                except IndexError:
                    click.secho("It was the last playlist!!!", bold=True, fg="yellow")
                    break
            case 2:
                select_pl_dir(lst, current_num)
                flag = True
            case 3:
                break
            case _:
                click.clear()
                click.echo(menu)
                click.secho("Enter a valid action.", bold=True, fg="yellow")


def select_playlist():
    while True:
        pl_lst = show_playlists()

        num = click.prompt(click.style("Choose playlist", bold=True), type=int)
        if num > len(pl_lst.keys()) or num < 0:
            click.secho("Number out of range.", bold=True, fg="yellow")
            continue
        elif not isinstance(num, int):
            click.secho("Arg must be integer.", bold=True, fg="yellow")
            continue
        else:
            select_pl_dir(pl_lst, num)
            playlist_ended(pl_lst, num)
