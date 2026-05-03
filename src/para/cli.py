from pathlib import Path
from datetime import date
from typer import Typer

app = Typer()


@app.command()
def archive(path: Path):
    today = date.today()
    archived_path = Path(f"~/archive/{today.year}/{today.isoformat()}-{path.name}")
    print(archived_path.expanduser())

    path.rename(archived_path.expanduser())

@app.command()
def init(name: str):
    today = date.today()
    project_path = Path(f"~/projects/{slugify(name)}").expanduser()
    project_path.mkdir()
    status_file = project_path / "STATUS.md"
    status_file.write_text(
        "\n".join([
            "<!-- markdownlint-disable MD13 -->",
            "<!-- LTeX: enable=true language=de-DE -->",
            f"# Status: {name}",
            "",
            f"- {today}: Initialized"
            ])
        )


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-")
