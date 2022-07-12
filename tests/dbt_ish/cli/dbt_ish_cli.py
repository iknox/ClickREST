from time import sleep
import click
import json

@click.command()
def dbt_ish():
    """This is a simple cli that writes json to stdout one line at a time a-la dbt"""
    event = {
        "thing": "stuff",
        "count": 0 
    }

    for x in range(0, 10):
        print(json.dumps(event))
        event["count"] += 1
        sleep(1)
