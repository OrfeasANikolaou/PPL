txt = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
# setup
cnt = [0] * 26
txt = txt.upper()
# print(txt)

# count iterations
for character in txt:
    if character >= 'A' and character <= 'Z':
        cnt[ord(character) - ord('A')] += 1

# output [character] count: cnt
list_sz = range(len(cnt))
for i in list_sz:
    english_alphabet = chr(ord('A') + i)
    print(f'[{english_alphabet}] count: {cnt[i]:02d}')
