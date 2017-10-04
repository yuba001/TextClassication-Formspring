import re

def read_csv(path):
    # First open the file
    with open(path, 'rt') as f:
        #skip first line
        next(f)
        # read files line by line
        lines = f.read().split("\n")
    print(lines[0])

    return lines

def get_label(path):
    lines = read_csv(path)
    counter = 0
    for line in lines:
      if counter < 50:
        respons_re = re.compile(r'(?:No|Yes)\s(?:\d|None)')
        #mo = respons_re.search(lines[1])
        mo = respons_re.findall(line)
        #print(mo.group())
        #print(mo)
        counter += 1


if __name__ == '__main__':
    get_label("formspring_data.csv")
