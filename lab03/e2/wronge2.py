def get_first_par_and_remove_dots_commas_tolower(whole_text):
    paragraph = []
    toggle = False
    for line in whole_text:
        line = line.replace(".", "")
        line = line.replace(",", "")
        line = line.replace("\n", "")
        if line[0:11] == "One morning":
            toggle = True
        if toggle == True and line.endswith("looked") :
            toggle = False
            paragraph.append(line.lower())
        if toggle:
            paragraph.append(line.lower())
    return paragraph 


def mk_text(paragraph):
    ret = str()
    for line in paragraph:
        ret += line + '\n'
    #  remove annoying new line at the end and string are immutable on python zzz...
    ret2 = ret[0:len(ret)-1]
    return ret2


def f1(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)


def f2(text: str):
    cnt = 0
    words = text.split()
    for word in words:
        if word.startswith('h') and word.endswith('e'):
            cnt += 1
    return cnt


def f3(text: str):
    cnt = 0
    words = text.split()
    for word in words:
        if len(word) == 5:
            cnt += 1
    return cnt


def f4(text: str):
    cnt = 0
    words = text.split()
    for word in words:
        if word.__contains__("as"):
            cnt += 1
    return cnt


def f5(text: str):
    cnt = 0
    words = text.split()
    for word in words:
        if word.__contains__("as") or word.__contains__("sa"):
            cnt += 1
    return cnt


def f6(text: str):
    cnt = 0
    words = text.split()
    for word in words:
        if word[0] == word[len(word) - 1]:
            cnt += 1
    return cnt


whole_text = []
file = open("Metamorphosis.txt", "r")
for line in file:
    whole_text.append(line)
file.close()

paragraph = get_first_par_and_remove_dots_commas_tolower(whole_text)
paragraph = mk_text(paragraph)
print("Paragraph:\n----------------------------------------------------------------------")
print(paragraph)
print("----------------------------------------------------------------------")
print(f"Count of unique words in first paragraph: {f1(paragraph)}")
print(f"Count of words which start with 'h' and end with 'e': {f2(paragraph)}")
print(f"Count of words with length of 5: {f3(paragraph)}")
print(f"Count of words which contain 'as': {f4(paragraph)}")
print(f"Count of words which contain 'as' or 'sa': {f5(paragraph)}")
print(f"Count of words which start and end with the same letter: {f6(paragraph)}")
