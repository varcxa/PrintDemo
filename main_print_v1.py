# pip install rich 가 필요합니다.

from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

name = "junhyeok"
age = 20
score = 99.9
data = {"name": name, "age": age, "score": score}
rprint(f"[bold green]Hello, {name}![/] Your score is [cyan]{score:.2f}[/].")
panel_text = """
[bold]Student Info[/]
- Name : [yellow]{name}[/]
- Age  : [magenta]{age}[/]
- Score: [cyan]{score:.2f}[/]
""".format(name=name, age=age, score=score)

rprint(Panel(panel_text, title="Profile", border_style="blue"))
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")

for k, v in data.items():
    table.add_row(k, str(v))

rprint(table)

rprint("2025", "09", "23", sep="-", end=" ✅\n")
