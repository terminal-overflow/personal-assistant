from os.path import dirname
import random

#break up functions section in README
def get_list(text):
    #get file path and read the file
    file_path = dirname(dirname(dirname(__file__)))
    file = open(f'{file_path}/README.md', 'r')
    func = file.readlines()
    file.close()

    #get starting index of functions section
    for i in range(len(func)):
        if 'Functions' in func[i-1]:
            s_mark = i-1
            s_mark = s_mark +7
            break

    #get ending index of functions section
    for i in range(len(func[s_mark:])):
        i = i+s_mark
        if func[i-1] == '\n':
            e_mark = i-1
            break

    #complete list
    final_ls = func[s_mark:e_mark]

    #remove unessessary information
    for i in range(len(final_ls)):
        final_ls[i] = final_ls[i].replace(' for', '')
        final_ls[i] = final_ls[i].replace('...', '')
        final_ls[i] = final_ls[i].rstrip()

    #return full list
    if text == 'full':
        return final_ls

    #remove more unessessary information
    for i in range(len(final_ls)):
        final_ls[i] = final_ls[i].replace('* ', '')
        final_ls[i] = final_ls[i].replace('What can you do', '')
        final_ls[i] = final_ls[i].strip()
        final_ls[i] = final_ls[i].replace(final_ls[i], f'\'{final_ls[i]}\'')

    #create a list with two examples
    random_ls = []
    while len(random_ls) != 2:
        random_chc = random.choice(final_ls)
        if random_chc not in random_ls and random_chc != '':
            random_ls.append(random_chc)

    #finalise output
    out_ls = ['i can perform various tasks such as', 'my functions include', 'my abilities include']
    random_ls = ' and '.join(random_ls)
    final_out = f'{random.choice(out_ls)} {random_ls}'

    return final_out