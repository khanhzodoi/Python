import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    string = next_lang.decode(encoding, errors=errors)
    raw_bytes = (string).encode(encoding, errors=errors)
    print(string, "<===>", raw_bytes)


languages = open("test.txt", 'rb')
main(languages, input_encoding, error)
languages.close()
