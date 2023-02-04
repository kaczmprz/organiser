class Organiser:
    def __init__(self):
        self._things_to_do: list = []
        self._things_done: list = []

    def add(self, item: str) -> None:
        self._things_to_do.append(item)

    def done(self, item: str) -> None:
        try:
            self._things_to_do.remove(item)
            self._things_done.append(item)
        except Exception as e:
            print(f"Cannot remove {item} because doesn't exist in list to do")

    def show(self) -> None:
        print(f'Things to do: {self._things_to_do}')
        print(f'Things done: {self._things_done}')

    def delete(self, item: str) -> None:
        try:
            self._things_to_do.remove(item)
        except Exception as e:
            print(f"Cannot remove {item} because doesn't exist in list to do")

    def change_order(self, item: str) -> None:
        if item in self._things_to_do:
            self._things_to_do.remove(item)
            self._things_to_do.insert(0, item)
        else:
            self._things_to_do.insert(0, item)

    @staticmethod
    def get() -> str:
        return str(input("Write thing: "))

    @staticmethod
    def menu():
        print("1 - add new thing to list to do")
        print("2 - mark thing as done")
        print("3 - show things to do and done")
        print("4 - delete thing from list to do")
        print("5 - insert thing to the beginning of the list")
        print("0 - to close the program")

    @staticmethod
    def exit():
        print("Thank you!")


if __name__ == '__main__':
    print('Hello in our application')
    organiser = Organiser()
    while True:
        organiser.menu()
        option = int(input('Choose option: '))
        if option == 0:
            organiser.exit()
            break
        elif option == 1:
            organiser.add(organiser.get())
        elif option == 2:
            organiser.done(organiser.get())
        elif option == 3:
            organiser.show()
        elif option == 4:
            organiser.delete(organiser.get())
        elif option == 5:
            organiser.change_order(organiser.get())
