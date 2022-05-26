# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        return f.read()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    form_text = text.replace(",", "").replace("?", "")
    word_dic = {}
    for word in form_text.split():
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    return word_dic

    # return {"as": 10, "would": 20}


print(read_file_content("story.txt"))
print(count_words())

