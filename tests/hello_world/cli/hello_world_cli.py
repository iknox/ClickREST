from time import sleep
import click

@click.command()
@click.option("--world", default="earth", help="world to greet")
def hello_world(world: str):
    """This is a basic 'Hello World' cli"""
    print(f"Hello { world }")
