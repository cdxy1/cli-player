import click

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
        click.echo(
            "Select or create playlist:\n 1. Select playlist\n 2. Create playlist"
        )
        choice = click.prompt("Enter a number", type=int)
        if choice not in (1, 2):
            click.echo("Enter 1 or 2, please!")
            continue
        else:
            return choice


def make_playlist():
    pl_lst = playlists_list()
    while True:
        name = click.prompt("Enter a name of playlist", type=str)
        if not isinstance(name, str):
            click.echo("Name must be string.")
            continue
        elif name in pl_lst.keys():
            click.echo("The playlist name is already exists.")
            continue
        else:
            make_playlist_dir(name)
            return


def show_playlists():
    pl_lst = playlists_list()
    click.echo("Playlists:\n==========")
    for num, key in enumerate(pl_lst.keys()):
        click.echo(f"{num}. {key.title()}")
    else:
        click.echo("==========\n")

    return pl_lst


def playlist_ended(lst, num):
    current_num = num

    while True:
        click.echo(
            "\nWhat next?:\n1. Next playlist\n2. Retry current playlist\n3. Choose another playlist"
        )
        step = click.prompt("Enter the action", type=int)

        match step:
            case 1:
                try:
                    select_pl_dir(lst, current_num + 1)
                    current_num += 1
                except IndexError:
                    click.echo("It was the last playlist!!!")
                    break
            case 2:
                select_pl_dir(lst, num)
            case 3:
                break
            case _:
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
