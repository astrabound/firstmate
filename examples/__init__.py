from examples import multiple_menus
from firstmate.menu import CommandLineMenu, MenuOption, MenuOptionAction

examples_menu = CommandLineMenu(
    title="Firstmate examples",
    description="This is a sample menu to showcase examples",
    options=[
        MenuOption(
            label="Multiple menus",
            action=MenuOptionAction.SHOW_MENU,
            data={"menu": multiple_menus.menu}
        )
    ],
    enable_exit=True
)
