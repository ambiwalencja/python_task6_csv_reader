import os
import sys
# from os import path


class CsvReader:
    def __init__(self):
        self.input_file = sys.argv[1]  # nazwa pliku wchodzącego - drugi wyraz linii komend
        self.output_file = sys.argv[2]  # plik wychodzący, który dopiero stworzymy
        self.list_of_lines = self.read_file()  # lista, w której przechowujemy wiersze pliku, a w nich elementy
        self.list_of_changes = []  # lista modyfikacji podana w linii komend
        for change in sys.argv[3:]:  # wypełniamy listę modyfikacji w pętli
            self.list_of_changes.append(change.split(","))  # używamy splita, żeby rozdzielić części modyfikacji

    def __str__(self):
        return f'Input file: {self.input_file}; output file: {self.output_file}; changes: {self.list_of_changes}'

    def read_file(self):  # czyta i wstawia zawartość pliku do listy list (atrybutu klasy) lista[wiersz][element]
        list_of_lines = []
        with open(self.input_file, "r") as file:
            for line in file.readlines():
                separated_line = line.split("\n")[0].split(",")  # jedna linia (bez entera) w formie listy
                list_of_lines.append(separated_line)
        return list_of_lines  # ustawiam atrybut w inicie

    def modify_file(self):
        for change in self.list_of_changes:  # pętla po wszystkich zmianach (każda zmiana to lista)
            if int(change[0]) > len(self.list_of_lines) - 1:  # jeśli podamy zbyt duzy Y
                return False
            if int(change[1]) > len(self.list_of_lines[0]) - 1:  # jeśli podamy zbyt duży X
                return False
            self.list_of_lines[int(change[0])][int(change[1])] = change[2]  # podmieniamy element listy
        return True

    def save_file(self):
        with open(self.output_file, "w") as file:
            for line in self.list_of_lines:
                for element in line[:-1]:  # jedziemy po wszystkich elementach wiersza oprócz ostatniego
                    file.write(str(element) + ",")  # po każdym przecinek
                file.write(str(line[-1] + "\n"))  # a po ostatnim enter


def check_input_file():
    if not os.path.exists(sys.argv[1]):
        return False
    return True


def show_directory():
    files = []
    for element in os.listdir('.'):
        if os.path.isfile(element):
            files.append(element)
    return files


# ------------------------------------------------------------------------
if not check_input_file():
    print(f'No such file. Available files: {show_directory()}')
else:
    my_reader = CsvReader()
    if not my_reader.modify_file():
        print(f'Change impossible - maximum index of row is {len(my_reader.list_of_lines) - 1} '
              f'and maximum index of column is {len(my_reader.list_of_lines[0]) - 1}')
    my_reader.save_file()
