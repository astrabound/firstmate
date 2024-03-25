from typing import List
from firstmate.common.singleton import SingletonMeta


class MenuStack(metaclass=SingletonMeta):
    """
    Singleton for stack of menu instances to track the order of menus traversed
    and manage backtracking.
    """

    stack: List = []

    def push_menu(self, menu=None) -> bool:
        status = False

        try:
            assert menu is not None, "Menu can not be None"
            self.stack.append(menu)
            status = True
        except AssertionError as e:
            print(f"Error: {e}")

        return status

    def go_to_root(self) -> bool:
        status = False

        try:
            assert len(self.stack) > 0, "No root found on stack."
            del self.stack[1:]
            status = True
        except AssertionError as e:
            print(f"Error: {e}")

        return status

    def go_back(self, levels=1) -> bool:
        status = False

        try:
            assert len(self.stack) > levels, \
                "Level count to go back must be less than length of stack."
            del self.stack[-levels:]
            status = True
        except AssertionError as e:
            print(f"Error: {e}")

        return status

    def __repr__(self) -> str:
        return f"<MenuStack {id(self)}>"

    def __len__(self) -> int:
        return len(self.stack)
