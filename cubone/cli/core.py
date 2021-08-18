import click
from PyInquirer import prompt

from cubone.functions import start_project
from cubone.questions import CheckboxQuestion, ListQuestion


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
    questions = [
        CheckboxQuestion(name="toppings", choices=["Ham", "Ground Meat", "Bacon"]),
        ListQuestion(name="Game Type", choices=["Single-Player", "Multiplayer"])
    ]
    answers = prompt(questions)
    start_project(path, answers)


main.add_command(startproject)
