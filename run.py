from time import sleep
from src.manipulator import MainframeManipulator
from src.commands_parser import CommandsParser


def main() -> None:
    manipulator = MainframeManipulator()
    parser = CommandsParser()

    manipulator.set_fullscreen_mode()
    first_address = parser.get_first_address()

    manipulator.press_sequence(first_address)
    manipulator.press_key('F4')

    for command_value in parser.get_all_commands_values():
        manipulator.press_sequence(command_value)
        manipulator.press_key('F5')

    manipulator.press_sequence(first_address)
    manipulator.press_key('F4')
    sleep(0.2)
    manipulator.press_key('F6')

    manipulator.set_normal_mode()

    print(f'Адрес первой команды: {parser.get_first_address()}\n')
    print(f'Команды:')
    for command_value in parser.get_all_commands_values():
        print(command_value)


if __name__ == '__main__':
    main()
