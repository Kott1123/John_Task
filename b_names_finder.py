import string
unique_names = []
unique_text = []
def word_splitter(z):
    word_list=[]
    for line in z:
        for word in line.split():
            worders = word
            for character in string.punctuation:
                worders = worders.replace(character, ' ')
            x = worders.split()
            for i in x:
                i = i.upper()
                word_list.append(i)
    return word_list
def unifier(x):
    unique_thing = []
    for i in x:
        if i not in unique_thing:
            unique_thing.append(i)
    return unique_thing
with open('blacklisted_names.txt' , 'r') as bn:
    with open('text.txt' , 'r') as t:
        with open('found_blacklisted_names.txt' , 'a') as found_names:
            names = word_splitter(bn)
            unique_names = unifier(names)
            text_file = word_splitter(t)
            unique_t_f = unifier(text_file)
            for i in unique_names:
                for j in unique_t_f:
                    i_s = i + 'S'
                    i_es = i + 'ES'
                    if i == j or j == i_s or j == i_es:
                        word = i.capitalize()
                        found_names.write(word)
                        found_names.write('\n')
                        break

                    
            


                
            




                
           




