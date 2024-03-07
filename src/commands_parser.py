import typing as t

from .config import DATA_DIR
from .types import Command


class CommandsParser:
    def __init__(self, filename: str = 'commands.txt'):
        self.__filename = filename
        self.__commands = self.__read_commands()

    @staticmethod
    def __convert_to_bin(hex_value: str, target_length: int) -> str:
        int_value = int(hex_value, base=16)
        bin_value = bin(int_value)[2:]
        zeros_to_add = target_length - len(bin_value)
        return '0' * zeros_to_add + bin_value

    def __read_commands(self) -> t.List[Command]:
        with open(DATA_DIR / self.__filename, 'r') as file:
            commands = []
            for line in file.readlines():
                line = line.strip()
                if line:
                    instructions = line.split()

                    if len(instructions) == 2:
                        address, value = line.split()
                        flag = None
                    else:
                        address, value, flag = line.split()

                    if flag == '+':
                        is_new_module = True
                    else:
                        is_new_module = False

                    commands.append(Command(
                        self.__convert_to_bin(address, target_length=16),
                        self.__convert_to_bin(value, target_length=16),
                        is_new_module
                    ))

            return commands

    def get_first_address(self) -> str:
        return self.__commands[0].address

    def get_all_commands(self) -> t.Iterator[Command]:
        for command in self.__commands:
            yield command
