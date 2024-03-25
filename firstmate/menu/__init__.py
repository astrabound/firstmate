from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Self

from firstmate.common.constants import SEP_DASH, SEP_EQUALS, DEFAULT_MENU_TITLE
from firstmate.stack import MenuStack


class MenuOptionAction(Enum):
    EXIT = 0
    RETURN = 1
    RUN_CALLBACK = 2
    SHOW_MENU = 3


@dataclass
class MenuOption:
    """
    # MenuOption
    Dataclass for an option in a menu. Holds the following attributes

    - `label`: String label to show in a menu as an identifier.
    - `action`:
        Type of action to execute for this option.
        Can be of type enum `MenuOptionAction`
    - `callback`:
        Custom callback to run when action is `MenuOptionAction.RUN_CALLBACK`
    - `data`: Dictionary of arguments to pass to callback for execution.

    ## Note:
    - The `data` is spread so the keys will correspond to keyword arguments.

    """
    label: str = None
    action: MenuOptionAction = MenuOptionAction.RUN_CALLBACK
    callback: Callable = None
    data: Dict = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"<MenuOption: {self.label}>"


RETURN_MENU_OPTION = MenuOption(
    label="Return",
    action=MenuOptionAction.RETURN,
)

EXIT_MENU_OPTION = MenuOption(
    label="Exit",
    action=MenuOptionAction.EXIT,
)


class CommandLineMenu():
    """
    Class to represent a menu in command line.

    Arguments:
    - `title`: String title for the menu header.
    - `description`: Description to display below title for more information.
    - `context`: Data for the menu to use for execution and options generation.
    - `options`: List of options to display in the menu.
    - `enable_exit`: Boolean flag to enable exit from a menu. (Default: False)
    """
    stack = MenuStack()

    title: str = None
    description: str = None
    context: Dict = {}
    options: List[MenuOption] = []
    enable_exit: bool = False

    def __init__(
        self,
        title: str = None,
        description: str = None,
        context: Dict = {},
        options: List[MenuOption] = [],
        enable_exit: bool = False,
    ) -> None:

        self.title = title or DEFAULT_MENU_TITLE
        self.description = description
        self.context = context
        self.options = options
        self.enable_exit = enable_exit

    def show(self):
        additional_options = []

        if len(self.stack) > 0:
            additional_options.append(RETURN_MENU_OPTION)

        if self.enable_exit:
            additional_options.append(EXIT_MENU_OPTION)

        self.stack.push_menu(self)

        all_options = self.options + additional_options

        while True:
            print(SEP_EQUALS)
            print(self.title)
            print(SEP_DASH)

            if self.description:
                print(self.description)
                print(SEP_DASH)

            for index, option in enumerate(all_options):
                print(f"{index}: {option.label}")

            try:
                choice = int(input("Select an option: "))
                assert choice >= 0 and choice <= len(all_options), \
                    "Option out of range. Select from the given options."

                return_cue = self.run_option_action(all_options[choice])

                if return_cue:
                    break
            except (ValueError, AssertionError) as e:
                print(f"Invalid option selection: {e}")

    def run_option_action(self, option: MenuOption = None):
        return_cue = False

        try:
            if option.action == MenuOptionAction.EXIT:
                exit(0)
            elif option.action == MenuOptionAction.RETURN:
                self.stack.go_back()
                return_cue = True
            elif option.action == MenuOptionAction.RUN_CALLBACK:
                option.callback(**option.data)
            elif option.action == MenuOptionAction.SHOW_MENU:
                menu: Self = option.data.get("menu")
                menu.show()

        except Exception as e:
            print("Error: Exception while running option action")
            print(f"\tDetails: {e}")
            print("\tOption:", option)

        return return_cue
