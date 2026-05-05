from pathlib import Path
from datetime import date
import re
from typer import Typer
from rich.console import Console

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

@app.command()
def status():
    projects_path = Path("~/projects").expanduser()
    console = Console()

    projects = []
    for project in projects_path.glob("*"):
        status_file = project / "STATUS.md"
        if project.name.startswith("."):
            continue
        if not status_file.exists():
            projects.append(
                {
                    "status": "skip",
                    "title": project.name,
                }
            )
            continue

        status_content = status_file.read_text()
        title_match = re.search(r'# Status: (.*)', status_content)
        title = title_match.group(1) if title_match else project.name
        all_status = re.findall(r"- (\d{4}-\d{2}-\d{2}):? (.*)", status_content)
        date, status_string = sorted(all_status, key=lambda item: item[0])[-1]
        projects.append(
            {
                "title": title,
                "status": "has-status",
                "last_update": date,
                "last_status": status_string,
            }
        )

    def projects_key(a):
        return (a["status"], a["title"], a.get("all_status"))

    for i, project in enumerate(sorted(projects, key=projects_key)):
        title = project["title"]
        if project["status"] == "skip":
            console.print(f"{i+1:2}. [ SKIP ] {title}", style="dim")
        elif project["status"] == "has-status":
            console.print(f"{i+1:2}. {title}", style="bold green")
            console.print(f"  {project['last_update']} - {project['last_status']}\n")

def slugify(name: str) -> str:
    return name.lower().replace(" ", "-")
