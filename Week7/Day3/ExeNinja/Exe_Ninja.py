def get_full_name(**kwargs):
    name = ""
    for x in kwargs:
        name = name + kwargs[x] + " "
    return name


def print_frame(sentance):
    max_len = 0
    for x in sentance:
        if len(x) > max_len:
            max_len = len(x)
    print_frame_x(max_len)
    for x in sentance:
        filler = " " * (max_len - len(x))
        print("*" + x + filler + "*")
    print_frame_x(max_len)


def print_frame_x(number_of_x):
    print("*" * (number_of_x + 2))


def to_morse_code(msg, dictionary):
    code = ""
    for x in msg:
        if x == " ":
            code += "/"
        else:
            code += dictionary[x.upper()]
            code += " "
    return code


def from_morse_code(msg_morse, morse_dict):
    msg = ""
    letters = msg_morse.split(' ')
    for x in letters:
        if "/" in x:
            msg += " "
            x = x.replace("/", "")

        for y in morse_dict:
            if morse_dict[y] == x:
                msg += y.lower()
                break
    return msg


def main():
    # exe1
    print(get_full_name(first_name="Arthur", middle_name="Alessandro", last_name="Ruthenberg"))
    print(get_full_name(first_name="Madonna"))
    print(get_full_name(title="His Royal Highness,", second_title="Prince", of_what="of Edinbrguh"))

    # exe2

    # exe3
    sentance = "quick fox jumps over the lazy dog"
    print_frame(sentance.split(" "))
    # exe4

    # exe5
    morse_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..'}
    msg = "quick fox jumps over the lazy dog 13 times"

    msg_morse = to_morse_code(msg, morse_dict)
    print(msg_morse)
    print(from_morse_code(msg_morse, morse_dict))


if __name__ == "__main__":
    main()
