import string
import sys


class Vigenere:
    def __init__(self, alph=tuple(string.ascii_uppercase)):
        self._alph = alph

    def check_key(self, value: str):
        if not isinstance(value, str):
            print("[ERROR]: key must be string type and not empty")
            exit()
        for char in value.upper():
            if char not in self._alph:
                print("[ERROR]: Only letters are allowed in the keyword without blank spaces")
                exit()
        return value.upper()

    def check_message(self, value: str):
        if not isinstance(value, str):
            print("[ERROR]: message should be string type")
            exit()
        mes = "".join(value.split())
        for char in mes.upper():
            if char not in self._alph:
                print("[ERROR]: Only letters allowed in the message")
                exit()
        return mes.upper()

    @staticmethod
    def get_cheap_viagra(message: str, key: str) -> list[str]:
        text = list(message.upper())
        key = key.upper()
        help_key = []
        counter = 0
        for _ in range(len(text)):
            try:
                key[counter]
            except IndexError:
                counter = 0
            help_key.append(key[counter])
            counter += 1
        return help_key

    @staticmethod
    def get_letters_nums(alph: tuple[str]) -> dict[str, int]:
        letters_nums: dict[str, int] = {}
        counter = 0
        for char in alph:
            letters_nums[f"{char}"] = counter
            counter += 1
        return letters_nums

    @staticmethod
    def get_nums_letters(alph: tuple[str]) -> dict[int, str]:
        nums_letters: dict[int, str] = {}
        counter = 0
        for char in alph:
            nums_letters[counter] = char
            counter += 1
        return nums_letters

    def decode_encode_message(self, keyword: str, message: str, mode: str = "encode") -> str:
        num_let: dict[int, str] = self.get_nums_letters(self._alph)
        let_num: dict[str, int] = self.get_letters_nums(self._alph)
        clean_message = self.check_message(message)
        clean_keyword = self.check_key(keyword).upper()
        help_key = self.get_cheap_viagra(clean_message, clean_keyword)
        mes_key = list(zip(clean_message, help_key))
        lst = []
        for mlet, klet in mes_key:
            if mode == "encode":
                res = let_num[klet] + let_num[mlet]
                if res >= 26:
                    lst.append(num_let[res - 26])
                else:
                    lst.append(num_let[res])
            else:
                res = let_num[mlet] - let_num[klet]
                if res < 0:
                    lst.append(num_let[26 + res])
                else:
                    lst.append(num_let[res])
        return "".join(lst)


def input_mode():
    start = True
    while start:
        try:
            get_mode = input("Enter desired mode. 'D' for decode or 'E' for encode: ")
            if get_mode.lower() == "exit":
                exit()
            get_text = input("Enter your message: ")
            get_key = input("Enter a key: ")
            vigenere = Vigenere()
            match get_mode.upper():
                case "D":
                    print(vigenere.decode_encode_message(get_key, get_text, mode="decode"))
                case "E":
                    print(vigenere.decode_encode_message(get_key, get_text))
                case _:
                    print("[ERROR]: Enter right mode!!!")
                    continue
        except Exception as error:
            print(f"[ERROR]: {error}!!!")


def console_mode():
    get_text = "".join(x for x in sys.argv[1:-1])
    get_key = sys.argv[-1]
    vigenere = Vigenere()
    print(vigenere.decode_encode_message(get_key, get_text))
    return vigenere.decode_encode_message(get_key, get_text)


def main():
    if len(sys.argv) == 1:
        input_mode()
    else:
        console_mode()


if __name__ == "__main__":
    main()
