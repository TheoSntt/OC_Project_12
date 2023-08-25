from rich.console import Console
from rich.panel import Panel
from typing import Tuple, Optional
from rich import box
import pyinputplus as pyip


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
