
#FANG 
source="silent"

target="listen"

is_kangraoo_word = True

for ch in target:

    if ch not in source:

        is_kangraoo_word = False

        break

print(is_kangraoo_word)


