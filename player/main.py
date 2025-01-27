import click
from inputimeout import inputimeout, TimeoutOccurred

from core.files import (
    init_main_dir,
    make_playlist_dir,
    playlists_list,
    select_pl_dir,
    check_main_dir,
)


@click.group
def cli():
    pass


def select_menu():
    while True:
        click.clear()
        click.echo(
            "Select or create playlist:\n 1. Select playlist\n 2. Create playlist"
        )
        choice = click.prompt("Enter a number", type=int)
        if choice not in (1, 2):
            click.clear()
            click.echo("Enter 1 or 2, please!")
            continue
        else:
            return choice


def make_playlist():
    pl_lst = playlists_list()
    while True:
        name = click.prompt("Enter a name of playlist", type=str)
        if not isinstance(name, str):
            click.clear()
            click.echo("Name must be string.")
            continue
        elif name in pl_lst.keys():
            click.clear()
            click.echo("The playlist name is already exists.")
            continue
        else:
            make_playlist_dir(name)
            return


def show_playlists():
    pl_lst = playlists_list()
    click.clear()
    click.echo("Playlists:\n==========")
    for num, key in enumerate(pl_lst.keys()):
        click.echo(f"{num}. {key.title()}")
    else:
        click.echo("==========\n")

    return pl_lst


def playlist_ended(lst, num):
    flag = True
    current_num = num

    click.clear()

    while True:
        for sec in range(10, 0, -1):
            if flag:
                click.clear()
                click.echo(
                    "\nWhat next?:\n1. Next playlist\n2. Retry current playlist\n3. Choose another playlist"
                )
                click.echo(f"Press something to select option. S({sec})")
                try:
                    if _ := inputimeout(timeout=1):
                        import sys, termios

                        flag = False
                        termios.tcflush(sys.stdin, termios.TCIFLUSH)
                except TimeoutOccurred:
                    continue
            else:
                click.clear()
                click.echo(
                    "\nWhat next?:\n1. Next playlist\n2. Retry current playlist\n3. Choose another playlist"
                )
                step = click.prompt("Enter a action", type=int)
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
                    click.echo("It was the last playlist!!!")
                    break
            case 2:
                select_pl_dir(lst, current_num)
                flag = True
            case 3:
                break
            case _:
                click.clear()
                click.echo(
                    "\nWhat next?:\n1. Next playlist\n2. Retry current playlist\n3. Choose another playlist"
                )
                click.echo("Enter a valid action.")


def select_playlist():
    while True:
        pl_lst = show_playlists()

        num = click.prompt("Choose playlist", type=int)
        print(num)
        if num > len(pl_lst.keys()) or num < 0:
            click.echo("Number out of range.")
            continue
        elif not isinstance(num, int):
            click.echo("Arg must be integer.")
            continue
        else:
            select_pl_dir(pl_lst, num)
            playlist_ended(pl_lst, num)


@cli.command()
def start():
    click.echo("Start player")

    if not check_main_dir:
        path = click.prompt(
            "Enter default dir path or leave blank", type=str, default=""
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
