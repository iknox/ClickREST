from ..cli.hello_world_cli import hello_world
from typing import Union
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from contextlib import redirect_stdout
import io

app = FastAPI()

# The most minimal implementation
@app.get("/")
def root_get():    
    output = io.StringIO()

    with redirect_stdout(output):
        hello_world.main(
            ["--world", "pluto"],
            standalone_mode=False
            )

    return output.getvalue()
 