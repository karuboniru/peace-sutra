import sys
import re

def main():
    file = open(sys.argv[1], 'r')
    buf_str = file.read()
    file.close()
    str_split = re.split(';|,|\ |\n',buf_str)
    out_buffer=''
    for s in str_split:
        if s == '':
            break
        out_buffer = out_buffer+s+'平安 '
    if (len(sys.argv) == 3):
        file = open(sys.argv[2], 'w+')
        file.write(out_buffer)
        file.close()
    else:
        print(out_buffer)

if __name__ == "__main__":
    main()