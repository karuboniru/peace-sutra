import json

def main():
    file = open('./ci.json', 'r')
    file_out = open('ciout.txt', 'w+')
    data = json.load(file)
    for i in data:
        file_out.write(i['ci']+',')
    file.close()
    file_out.close()


if __name__ == "__main__":
    main()
