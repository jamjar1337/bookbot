def count_words_in_book(file_text: str):
    book_text = file_text.split()
    return len(book_text)


def breakdown_of(input_text: str):
    output = dict()
    for char in input_text:
        char = char.lower()
        if char in output:
            output[char] += 1
        else:
            output.update({char: 1})
    return output


def dictionary_to_sortable(
        input_dict: dict, 
        first: str='char', 
        second: str='num'
    ):
    output = list()
    for key, val in input_dict.items():
        output.append({first: key, second: val})
    return  output

def sort_on(items):
    return items["num"]

def sorted_character_list(input_data: list[dict]):
    input_data.sort(reverse=True, key=sort_on)
    # for i in input_data:
    #     if not i['char'].isalpha():
    #         input_data.pop(input_data.index(i))
    
    return input_data
