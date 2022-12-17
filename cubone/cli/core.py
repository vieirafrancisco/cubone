import click


@click.group()
def main():
    pass


@click.command()
@click.option(
    "--path",
    "-p",
    help="Absolute path where will be created the projects files.",
    default=".",
    type=str,
)
def startproject(path):
    """Start a new game project."""
    print("Project started!")


main.add_command(startproject)
