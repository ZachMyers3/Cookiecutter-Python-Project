import typer

app = typer.Typer()


@app.command()
def command() -> None:
    pass


def main():
    app()


if __name__ == "__main__":
    main()
