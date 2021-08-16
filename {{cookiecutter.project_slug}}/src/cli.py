import typer

from {{ cookiecutter.project_underscore }} import main as {{ cookiecutter.project_underscore }}

app = typer.Typer()


@app.command()
def command() -> None:
    {{ cookiecutter.project_underscore }}()


def main():
    app()


if __name__ == "__main__":
    main()
