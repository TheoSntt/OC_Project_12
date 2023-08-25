from rich.console import Console
from rich.panel import Panel
from typing import Tuple, Optional
from rich import box
import pyinputplus as pyip
from rich.table import Table


class Display:
    def __init__(self) -> None:
        self._console = Console()

    def log(self, msg_obj=None) -> None:
        self._console.print(msg_obj, style="bold green")

    def log_styled(self, msg_obj=None, style: Optional[str] = None) -> None:
        self._console.print(msg_obj, style=style)

    def warning(self, msg_obj=None) -> None:
        self._console.print(msg_obj, style="bold yellow")

    def error(self, msg_obj=None) -> None:
        self._console.print(msg_obj, style="bold red")

    def prompt_api_details(self) -> Tuple[str, str, str]:
        api_prompt = Panel(
            """
                You can find your API keys :key: on your Twitter App Dashboard
                [blue underline bold][link=https://google.com]here[/link][/blue underline bold]
            """,
            box=box.ROUNDED,
        )
        self.log_styled(api_prompt, style="yellow")
        self.log(
            "Paste the Client ID, Secret and App Name from your profile and hit enter: "
        )
        client_id = pyip.inputStr("Client ID 🆔 ")
        client_secret = pyip.inputStr("Client Secret 🕵️ ", allowRegexes=[r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"],
                                      blockRegexes=[r"."])
        app_name = pyip.inputStr("App Name ✏️  ")
        return (client_id, client_secret, app_name)

    def clientsAsTable(self, clients) -> None:
        table = Table(
            show_header=True,
            box=box.ROUNDED,
            show_lines=True,
            padding=(0, 1, 1, 0),
            border_style="yellow"
        )
        table.add_column("ID", justify="center")
        table.add_column("Name", justify="center")
        table.add_column("Surname", justify="center")
        table.add_column("Email", justify="center")
        table.add_column("Telephone", justify="center")
        table.add_column("Company", justify="center")
        table.add_column("First exchange", justify="center")
        table.add_column("Last exchange", justify="center")
        table.add_column("Commercial contact", justify="center")

        for client in clients:
            table.add_row(
                str(client.id),
                client.name,
                client.surname,
                client.email,
                client.telephone,
                client.enterprise_name,
                str(client.create_date),
                str(client.last_update_date),
                str(client.contact)
            )
        self._console.print(table)

    def collabsAsTable(self, clients) -> None:
        table = Table(
            show_header=True,
            box=box.ROUNDED,
            show_lines=True,
            padding=(0, 1, 1, 0),
            border_style="yellow"
        )
        table.add_column("ID", justify="center")
        table.add_column("Name", justify="center")
        table.add_column("Surname", justify="center")
        table.add_column("Email", justify="center")
        table.add_column("Telephone", justify="center")
        table.add_column("Role", justify="center")
        for client in clients:
            table.add_row(
                str(client.id),
                client.name,
                client.surname,
                client.email,
                client.telephone,
                str(client.role)
            )
        self._console.print(table)