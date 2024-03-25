from firstmate.menu import CommandLineMenu, MenuOption, MenuOptionAction
from firstmate.stack import MenuStack

stack = MenuStack()

subsubmenu = CommandLineMenu(
    title="Sub-sub-menu",
    description="This is the grandchild",
    options=[
        MenuOption(
            label="Print hello world from leaf",
            callback=lambda: print("Hello world from leaf!"),
        ),
        MenuOption(
            label="Print arg x",
            callback=lambda x: print("x =", x),
            data={"x": 3}
        )
    ]
)

submenu = CommandLineMenu(
    title="Sub-menu",
    description="This is the child",
    options=[
        MenuOption(
            label="Print hello world from trunk",
            callback=lambda: print("Hello world from trunk!"),
        ),
        MenuOption(
            label="Print arg x",
            callback=lambda x: print("x =", x),
            data={"x": 2}
        ),
        MenuOption(
            label=subsubmenu.title,
            action=MenuOptionAction.SHOW_MENU,
            data={"menu": subsubmenu}
        )
    ]
)

menu = CommandLineMenu(
    title="Main menu",
    description="This is the root",
    options=[
        MenuOption(
            label="Print hello world from root",
            callback=lambda: print("Hello world from root!"),
        ),
        MenuOption(
            label="Print arg x",
            callback=lambda x: print("x =", x),
            data={"x": 1}
        ),
        MenuOption(
            label=submenu.title,
            action=MenuOptionAction.SHOW_MENU,
            data={"menu": submenu}
        )
    ],
    enable_exit=True
)

if __name__ == "__main__":
    menu.show()
