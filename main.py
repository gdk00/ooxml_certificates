from process_sheet import get_graduates_list
from process_doc import create_sertificates
from config import sheet_fpath, template, fields_columns

def get_one_from_option(list):
    print('Choose one of these types: {}')
    for i, v in enumerate(list):
        print('{}: {}'.format(i + 1, v))
    chose = input()
    if chose.isnumeric():
        ind = int(chose) - 1
        if 0 <= ind < len(list):
            return list[ind]
    return None

def change_person(person):
    option = get_one_from_option(list(person.keys()))
    if option:
        if option == 'qualification':
            qualification_list = list(template.keys())
            chosen_type = get_one_from_option(qualification_list)
            if not chosen_type is None:
                person['qualification'] = chosen_type
        else:
            person[option] = input('Print new value: ')
    return person

def edit_graduates(graduates):
    to_change = True
    while(to_change):
        to_change = False
        for i, person in enumerate(graduates):
            person_info = ' '.join(list(person.values()))
            print('{}: {}'.format(i + 1, person_info))
        chose = input('Chooose number to change or press another key to continue: ')
        if chose.isnumeric():
            ind = int(chose) - 1
            if 0 <= ind < len(graduates):
                graduates[ind] = change_person(graduates[ind])
                to_change = True
    return graduates


if __name__ == '__main__':
    graduates = get_graduates_list(sheet_fpath, fields_columns)
    edit_graduates(graduates)
    create_sertificates(data=graduates, template=template)
