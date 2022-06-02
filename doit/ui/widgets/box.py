from rich.box import HEAVY
from rich.console import RenderableType
from rich.panel import Panel
from rich.style import StyleType
from rich.table import Table
from rich.text import Text
from textual.widget import Widget


class Box(Widget):
    """
    A simple widget to render text with a panel
    """

    def __init__(
        self,
        names: list[str] = [],
        color: StyleType = "blue",
    ) -> None:
        super().__init__()
        self.names = names
        self.color = color
        self.highlighted = False

    def render(self) -> RenderableType:
        table = Table.grid(padding=(0, 1), expand=True)
        style = "bold blue" if self.highlighted else "dim white"
        for i in self.names:
            table.add_column(Text(i, style=style), justify="center", ratio=1)

        table.add_row(*self.names)

        return Panel(table, border_style=style, height=3, box=HEAVY)

    def highlight(self) -> None:
        self.highlighted = True
        self.refresh()

    def lowlight(self) -> None:
        self.highlighted = False
        self.refresh()
