import click

from core.files import init_main_dir, make_playlist_dir, playlists_list, select_playlist


@click.group
def cli():
    pass


@cli.command()
def start():
    click.echo("click is working")


@cli.command()
def test():
    click.echo("Start player")
    path = click.prompt("Enter default dir path or leave blank", type=str, default="")
    init_main_dir(path)
    click.echo("Select or create playlist:\n 1. Select playlist\n 2. Create playlist")
    choice = click.prompt("Enter a number", type=int)

    if choice == 2:
        name = click.prompt("Enter a name of playlist:", type=str)
        make_playlist_dir(name)
    else:
        pl_lst = playlists_list()
        click.echo("Playlists:\n==========")
        for num, key in enumerate(pl_lst.keys()):
            click.echo(f"{num}, {key.title()}")
        else:
            click.echo("==========\n")

        num = click.prompt("Choose playlist", type=int)
        select_playlist(pl_lst, num)


if __name__ == "__main__":
    cli()
