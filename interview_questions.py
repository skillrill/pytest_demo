st1 = 'eldor86ilyosov2015US2022Nissan2022'

def reverse_words_keep_numbers(st1):
    st2 = ''
    word = ''
    for i in st1:
        if not i.isdigit():
            word += i
        else:
            st2 += word[::-1]
            word = ''
            st2 += i
    st2 += word[::-1]
    return st2

print(reverse_words_keep_numbers(st1))