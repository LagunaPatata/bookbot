def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_charackters(text):
    lower_text = text.lower()
    dict_characters = {}
    for l in lower_text:
        if l not in dict_characters:
            dict_characters[l] = 1
        else:
            dict_characters[l] += 1

    return dict_characters

def sort_on(dict):
    return dict["value"]


def number_report(counts_of_letters):
    dict_list = []
    for i in counts_of_letters:
        dictionary = {}
        dictionary["letter"] = i
        dictionary["value"] = counts_of_letters[i]
        dict_list.append(dictionary)
    
    dict_list.sort(reverse=True, key=sort_on)    
    return(dict_list)
    
   
