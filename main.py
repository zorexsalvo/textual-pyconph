
from rich.table import Table

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static, Markdown


COLUMNS = ("Time", "Program", "Speaker", "Track")


SCHEDULE_1 = [
    ("8:00am - 9:00am", "Registration", "", "Online"),
    ("9:00am - 9:30am", "Opening Remarks", "", "[Track 1] Online"),
    ("9:30am - 10:30am", "Keynote 1: What's New in Python", "Mike Driscoll", "[Track 1] Online"),
    ("10:30am - 10:45am", "Break", "", "Online"),
    ("10:45am - 11:30am", "Keynote 2: Robust Python and Why It Matters", "Pat Viafore", "[Track 1] Online"),
    ("11:45am - 1:00pm", "Lunch / PyLadies Lunch", "", "Online"),
    ("1:00pm - 2:00pm", "The Art of Public Speaking, Presentation and Evaluation for Personal and Career Management", "Niharika Vadluri", "[Track 1] Online"),
    ("1:00pm - 2:00pm", "Musician to Machine Learning", "Arron Ritchie", "[Track 2] Online"),
    ("2:00pm - 3:00pm", "Continous Delivery for Python with Feature Flags", "Justine Paul Ballares", "[Track 1] Online"),
    ("2:00pm - 3:00pm", "A Fundamental Checklist for Publishing and Maintaining Opensource Python Packages in PyPI", "Kevin Lloyd Bernal", "[Track 2] Online"),
    ("3:00pm - 4:00pm", "Relation Extraction from Online Philippine News Source", "Michel Onasis Ogbinar", "[Track 1] Online"),
    ("3:00pm - 4:00pm", "Exploring The Forward-Forward Algorithm", "Elston Tan", "[Track 2] Online"),
    ("4:00pm - 5:00pm", "Python on the Client-Side Web", "Jabez Emmanuel Borja", "[Track 1] Online"),
    ("4:00pm - 5:00pm", "Managing Dependencies in Python with Poetry", "Neriah 'BJ' Ato", "[Track 2] Online"),
    ("5:00pm - 6:00pm", "pip install malware", "Max Kahan", "[Track 1] Online"),
    ("5:00pm - 6:00pm", "Working with Multiple Hands: Parallel and Distributed Programming", "Vikram Waradpande", "[Track 2] Online"),
    ("6:00pm - 6:30pm", "Announcements", "", "[Track 1] Online"), 
]

SCHEDULE_2 = [
    ("8:00am - 9:00am", "Registration", "", "Muralla Ballroom, The Bayleaf Hotel"),
    ("9:00am - 9:30am", "Opening Remarks", "", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("9:30am - 10:45am", "Keynote 3: The Zen of Programming - A personal journey towards writing beautiful code", "Sander Hoogendoorn", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("10:45am - 11:00am", "Break", "", "Muralla Ballroom, The Bayleaf Hotel"),
    ("11:00am - 12:00pm", "How Python Drives Modern Data Engineering", "Kiana Alessandra Villaera", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("11:00am - 12:00pm", "Workshop 1: Let's Make a Realtime Game with Django Channels", "Sony Valdez", "[Track 2] Basil Room, The Bayleaf Hotel"),
    ("12:00pm - 1:00pm", "Lunch (Group Lunches)", "", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("1:00pm - 1:30pm", "Group Photo", "", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("1:30pm - 2:30pm", "Lightning Talks", "", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("2:30pm - 3:30pm", "Javascript Fatigue: Back to Hypermedia with Django + HTMX", "John Rei Enriquez", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("1:30pm - 4:30pm", "Workshop 3: Data Engineering - A Roadmap to Building a Robust Data Infrastructure for Your Projects", "Ramon Perez", "[Track 2] Basil Room, The Bayleaf Hotel"),
    ("3:30pm - 4:30pm", "Surviving the Innovators Dilemma: A personal journey through scale ups, tech boards and microteams.", "Sander Hoogendoorn", "[Track 1] Muralla Ballroom, The Bayleaf Hotel"),
    ("4:30pm - 4:45pm", "Break", "", "The Bayleaf Hotel"),
    ("4:45pm - 5:30pm", "PyTunes", "", "The Bayleaf Hotel"),
    ("5:30pm - 6:00pm", "Games and Closing Remarks", "", "The Bayleaf Hotel"),
]


def get_schedule(title, schedule):
    table = Table(title=title, show_lines=True)

    table.add_column(COLUMNS[0], justify="right", style="cyan", no_wrap=True)
    table.add_column(COLUMNS[1], style="cyan", no_wrap=True)
    table.add_column(COLUMNS[2], style="cyan", no_wrap=True)
    table.add_column(COLUMNS[3], justify="right", style="green")

    for sched in schedule:
        table.add_row(*sched)

    return table


class DayButtonGroup(Static):

    def compose(self) -> ComposeResult:
        yield Button("Day 1 (Online)", id="day1-button", classes="day-button", variant="warning")
        yield Button("Day 2 (In-Person)", id="day2-button", classes="day-button", variant="warning")


class DayTable(Container):
    def compose(self):
        yield Static(get_schedule("Day 1 (February 25)", SCHEDULE_1), id="day1-table")
        yield Static(get_schedule("Day 2 (February 26)", SCHEDULE_2), id="day2-table") 

    def on_mount(self):
        table1 = self.get_widget_by_id("day1-table")
        table1.add_class("day-active")


class Sponsors(Container):
    def compose(self):
        yield Markdown("# Test")



SPONSORS = """\
# Keystone Sponsor
- **Python Software Foundation**


# Gold Sponsors
- **codev**
- **CodeHappy**
- **Total Rewards Software**


# Silver Sponsors
- **Torchbox** - Creator of Wagtail
- **Teach Me Python**


# Contributing Partner
- **Manning**
- **Python Web Conf**
- **No Starch Press**
- **Jet Brains**
- **Developer Week**


# Community Partner
- **PyTsada**
- **PizzaPy**
- **Women Who Code Manila**
- **Grupo Kalinangan**

"""



class Sidebar(Container):
    def compose(self) -> ComposeResult:
        yield Markdown(SPONSORS)

class PyConPhilipines(App):
    """A Textual app to show PyCon Philippines 2023 Schedule."""

    TITLE = "PyCon Philippines"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("b", "toggle_sidebar", "Toggle side bar")
    ]
    CSS_PATH = "pycon.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""

        yield Header()
        yield Sidebar(classes="-hidden")
        yield Markdown("# PyCon Philippines 2023")
        yield DayButtonGroup() 
        yield DayTable()
        yield Sponsors()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_toggle_sidebar(self) -> None:
        sidebar = self.query_one(Sidebar)
        self.set_focus(None)
        if sidebar.has_class("-hidden"):
            sidebar.remove_class("-hidden")
        else:
            if sidebar.query("*:focus"):
                self.screen.set_focus(None)
            sidebar.add_class("-hidden")

    def on_mount(self) -> None:
        day1_button =  self.get_widget_by_id("day1-button")
        day1_button.add_class("active") 

    def on_button_pressed(self, event: Button.Pressed) -> None:
        day1_button =  self.get_widget_by_id("day1-button")
        day2_button =  self.get_widget_by_id("day2-button")
        table1 = self.get_widget_by_id("day1-table")
        table2 = self.get_widget_by_id("day2-table")

        for btn in [day1_button, day2_button]:
            btn.remove_class("active")

        for tbl in [table1, table2]:
            tbl.remove_class("day-active")

        if event.button.id == "day1-button":
            day1_button.add_class("active")
            table1.add_class("day-active")

        elif event.button.id == "day2-button":
            day2_button.add_class("active")
            table2.add_class("day-active")


if __name__ == "__main__":
    app = PyConPhilipines()
    app.run()
