


def main(*args):
    import sys
    from bot.note import main as note_mode
    from bot.sorter import main as sorter_mode
    from bot.help_bot import main as contacts_mode

    print(
        "Print [number] or [name] of mode to choose your one:\n [1]: [contacts] \n [2]: [notes] \n [3]: [sorter]\n [4]: [exit]"
    )

    while True:
        mode = input(">>> ")
        if mode == "1" or mode == "contacts":
            print("Contact mode enabled")
            contacts_mode()
            sys.exit()
        elif mode == "2" or mode == "notes":
            print("Notes mode enabled")
            note_mode()
            sys.exit()
        elif mode == "3" or mode == "sorter":
            print("Sorter mode enabled")
            sorter_mode()
            sys.exit()
        elif mode == "exit" or mode == "4":
            sys.exit()
        else:
            print("Invalid mode argument")


if __name__ == "__main__":
    main()
