import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from core.engine import Engine
from core.action_system import ActionSystem
import json

console = Console()

class AutobotTUI:
    def __init__(self):
        self.engine = Engine()
        self.actions = ActionSystem()
        self.running = True

    def display_banner(self):
        try:
            with open("assets/banner.txt", "r") as f:
                banner = f.read()
            console.print(Panel(banner, style="bold cyan", expand=False))
        except FileNotFoundError:
            console.print(Panel("[bold cyan]AUTOBOT v2.0[/bold cyan]", expand=False))

    def main_menu(self):
        while self.running:
            console.clear()
            self.display_banner()

            table = Table(show_header=False, box=None, padding=(0, 2))
            options = [
                "1. [bold yellow]Anonymity & Privacy[/bold yellow]",
                "2. [bold yellow]Wireless Security[/bold yellow]",
                "3. [bold yellow]Web Security[/bold yellow]",
                "4. [bold yellow]Network & MITM[/bold yellow]",
                "5. [bold yellow]Exploitation Framework[/bold yellow]",
                "6. [bold yellow]Tool Database[/bold yellow]",
                "7. [bold yellow]My Custom Actions[/bold yellow]",
                "0. [bold red]Exit[/bold red]"
            ]
            for opt in options:
                table.add_row(opt)

            console.print(Panel(table, title="[bold white]AUTOBOT v2.0 Main Menu[/bold white]", border_style="cyan", expand=False))

            choice = Prompt.ask("\n[bold cyan]Select an option[/bold cyan]", choices=["1", "2", "3", "4", "5", "6", "7", "0"])

            if choice == "1": self.anonymity_menu()
            elif choice == "2": self.wireless_menu()
            elif choice == "3": self.web_menu()
            elif choice == "4": self.network_menu()
            elif choice == "5": self.exploitation_menu()
            elif choice == "6": self.tools_menu()
            elif choice == "7": self.actions_menu()
            elif choice == "0":
                console.print("[bold green]Shutting down AUTOBOT... Goodbye![/bold green]")
                self.running = False

    def tools_menu(self):
        try:
            with open("config/tools.json", "r") as f:
                tools = json.load(f)
        except Exception as e:
            console.print(f"[red]Error loading tools: {e}[/red]")
            return

        while True:
            console.clear()
            table = Table(title="Tool Database", show_header=True, header_style="bold magenta")
            table.add_column("ID", style="dim")
            table.add_column("Name")
            table.add_column("Description")

            for tool in tools:
                table.add_row(tool['id'], tool['name'], tool['description'])

            console.print(Panel(table, border_style="magenta"))

            tool_id = Prompt.ask("\nEnter Tool ID to launch, or a new tool to install (or 'b' to go back)")
            if tool_id == 'b': break

            tool = next((t for t in tools if t['id'] == tool_id), None)
            if tool:
                self.engine.execute(tool['command'])
                Prompt.ask("\nPress Enter to return to menu")
            else:
                if self.engine.smart_install(tool_id):
                    self.engine.execute(tool_id)
                Prompt.ask("\nPress Enter to return to menu")

    def actions_menu(self):
        while True:
            console.clear()
            actions_list = self.actions.list_actions()

            table = Table(title="My Custom Actions", show_header=False, box=None)
            for i, action in enumerate(actions_list, 1):
                table.add_row(f"{i}. {action}")
            table.add_row(f"{len(actions_list)+1}. [bold green]Add New Action[/bold green]")
            table.add_row(f"{len(actions_list)+2}. [bold red]Back[/bold red]")

            console.print(Panel(table, border_style="green"))

            choice = Prompt.ask("\nSelect action index")

            if choice.isdigit():
                idx = int(choice)
                if idx == len(actions_list) + 1:
                    self.add_action()
                elif idx == len(actions_list) + 2:
                    break
                elif 1 <= idx <= len(actions_list):
                    action_name = actions_list[idx-1]
                    action_data = self.actions.get_action(action_name)

                    # Handle parameterization during execution
                    steps = action_data.get("steps", [])
                    params = action_data.get("parameters", [])

                    # Create a map for the current execution
                    replacements = {}
                    for i, p in enumerate(params, 1):
                        val = Prompt.ask(f"p{i} ({p})")
                        replacements[p] = val if val.strip() != "" else p

                    # Execute steps with replacements
                    for step in steps:
                        cmd = step['command']
                        for original, replacement in replacements.items():
                            cmd = cmd.replace(original, replacement)
                        self.engine.execute(cmd)

                    Prompt.ask("\nAction complete. Press Enter to return")
            elif choice == 'b':
                break

    def add_action(self):
        name = Prompt.ask("Enter action name")
        console.print("[bold red]RECORDING MODE ACTIVE[/bold red]")
        console.print("Enter commands. Type 'q' to finish recording commands.")

        steps = []
        while True:
            cmd = Prompt.ask("[bold blue]Command[/bold blue]")
            if cmd.lower() == 'q': break
            if cmd:
                steps.append({"command": cmd, "type": "shell"})

        # Parameterization Phase
        parameters = []
        console.print("\n[bold yellow]Parameterization Phase[/bold yellow]")
        console.print("Enter strings you want to parameterize (e.g., the IP address).")
        console.print("Type 'save' to finish and save the action.")

        while True:
            param = Prompt.ask("[bold blue]Parameter[/bold blue]")
            if param.lower() == 'save': break
            if param:
                parameters.append(param)

        self.actions.save_action(name, steps, parameters)
        console.print(f"[green]Action '{name}' saved successfully![/green]")

    def web_menu(self):
        console.print("[yellow]Loading Web Security Module...[/yellow]")
        self.engine.run_bash_module("modules/web/web_core.sh")
        Prompt.ask("\nPress Enter to return to main menu")

    def anonymity_menu(self):
        console.print("[yellow]Loading Anonymity & Privacy Module...[/yellow]")
        self.engine.run_bash_module("modules/anonymity/privacy.sh")
        Prompt.ask("\nPress Enter to return to main menu")

    def wireless_menu(self):
        console.print("[yellow]Loading Wireless Security Module...[/yellow]")
        self.engine.run_bash_module("modules/wireless/wireless_core.sh")
        Prompt.ask("\nPress Enter to return to main menu")

    def network_menu(self):
        console.print("[yellow]Loading Network & MITM Module...[/yellow]")
        self.engine.run_bash_module("modules/network/network_core.sh")
        Prompt.ask("\nPress Enter to return to main menu")

    def exploitation_menu(self):
        console.print("[yellow]Loading Exploitation Framework Module...[/yellow]")
        self.engine.run_bash_module("modules/exploitation/exploit_core.sh")
        Prompt.ask("\nPress Enter to return to main menu")

if __name__ == "__main__":
    app = AutobotTUI()
    app.main_menu()
