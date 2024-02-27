# LINE TOO LONG HAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHHAAHAHAHAHAHAHAHAHAHAH
source = "How I need a drink alcoholic of course, after " \
         "all those lectures involving quantum mechanics"
list_of_things_im_bad_at_naming = source.split()
print(list_of_things_im_bad_at_naming)
cnt = 0
for thing in list_of_things_im_bad_at_naming:
    print(cnt+1, "word: length", len(thing))
    cnt = cnt + 1
