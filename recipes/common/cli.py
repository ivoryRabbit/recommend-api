import typer
import time

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal is True:
        typer.echo(f"Goodbye {name}. Have a good day")
    else:
        typer.echo(f"Bye {name}!")


@app.command()
def wait(seconds: int = typer.Argument(5, envvar="WAIT_TIME", show_envvar=False)):
    def echo(message: str):
        typer.echo(f" Wait {message} seconds")

    with typer.progressbar(range(seconds), label="Waiting") as progress:
        for val in progress:
            # echo(val)
            time.sleep(0.1)
            # progress.update(10)
        first = typer.style("Process", fg=typer.colors.GREEN, bold=True)
        second = typer.style("Completed", fg=typer.colors.RED, bold=False)
        typer.echo(f" {first} {second}.")
        typer.secho(f"Wait: {seconds} seconds", fg=typer.colors.MAGENTA)
        typer.secho(f"Invalid argument type: insert numeric type", fg=typer.colors.MAGENTA, err=True)


if __name__ == "__main__":
    ask = typer.confirm("Are you sure you want to process it?", abort=True)
    app()
