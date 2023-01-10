# Read data from files or input from a command line
# Check input file for common separators (/n, :, _, =, and etc.)
# Put it into a standartize file and read from it if user wants to
# Table inside the phonebook file database 
# | ID  |  Surename  |  Name  | Patronym  |  Phone            |
# | 1   |  Ivanov    |  Ivan  | Ivanovich | +7(900)-000-00-00 |
# ..............................................................
# ..............................................................


class PhoneBook():
   
    _separators = ('\n', '_', '.', ',', '~', ':', ';',
                   '%', '@', '!', '#', '=','+','<','>')
    
    _output_file_name = "phonebook.csv"
    
    def __init__(self) -> None:
        
        string: str = ""
        clean: list[str] = []
    
        self.string = string
        self.clean = clean
    
    def open_and_read_from_file(self, name: str = "") -> None:
        if name == "":
            name = "file.txt"
        with open(name, 'r') as file:
            self.string = file.read()
        file.close()
    
    def clean_string_and_prepear_it(self, name: str = "") -> None:
        foo: str = ""
        n: int = 0
        
        if name == "":
            for x in range(len(self._separators)):
                foo = self._separators[x]
                n = 0
                for y in range(len(self.string)):
                    if foo == self.string[y]:
                        n += 1
                if n != 0:
                    name = self._separators[x]
                    break
                else:
                    self.string.rstrip()
        self.clean = self.string.split(name)
        
        
    
    def print_from_standart_file(self) -> None:
        with open(self._output_file_name, 'r') as file:
            print(file.read())
        file.close

    def put_into_standart_file(self) -> None:
        count: int = 0
        with open(self._output_file_name, 'a') as file:
            for i in range(len(self.clean)):
                if i == 0:
                    file.write("|")
                if count == 4:
                    file.write('\n|')
                file.write((5 * " ") + f"{self.clean[i]}" + (5 * " ") + "|")
                count += 1
        file.close()
    
    def mainloop(self) -> None: 
        control: int = 0
        foo: str = ""
        
        print("Prpgram is running.")
        while True:
            print("Enter:\n",
                  "1. To read from a file and output it into a standart file.\n",
                  "2. To show entire phonebook.\n",
                  "3. To terminate the program.")
            try:
                control = int(input())
            except ValueError:
                print("Error! Not a number was entered!")
                pass
            match control:
                case 1:
                    foo = input("Enter the name of the file to read from.\nOr enter nothing to read from standart file.\n")
                    try:
                        PhoneBook.open_and_read_from_file(self, foo)
                        
                    except FileNotFoundError:
                        print("Error! No such file!")
                        pass
                    foo = input(f"Enter the separator that is used in the file.\nOr enter nothing to use standart.\nStandart separators:\n{self._separators}\n")
                    PhoneBook.clean_string_and_prepear_it(self, foo)
                    PhoneBook.put_into_standart_file(self)
                case 2:
                    PhoneBook.print_from_standart_file(self)
                case 3:
                    print("Terminating the program.")
                    break
                case _:
                    pass
    

def main() -> int:
    
    book = PhoneBook()
    book.mainloop()
    
    return 0


if __name__ == "__main__":
    main()
