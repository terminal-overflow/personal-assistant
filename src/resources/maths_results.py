import math

def math_results(text):
    text_list = text.split(' ')
    for i in range(len(text_list)):
        if (text_list[i] == 'square' and text_list[i+1] == 'root') or text_list[i] == '√':
            # check for square root and give answer
            for i in range(len(text)):
                try:
                    f_number = float(text[i:])
                    if str(f_number).endswith('.0'):
                        f_number = int(f_number)
                    sqrt_num = math.sqrt(f_number)
                    sqrt_num = round(sqrt_num, 5)
                    if str(sqrt_num).endswith('.0'):
                        sqrt_num = int(sqrt_num)
                    return f'the square root of {f_number} is {sqrt_num}'
                    break
                except ValueError:
                    pass

    for i in range(len(text_list)):
        if (text_list[i] == 'the' and text_list[i+1] == 'power' and 
        text_list[i+2] == 'of') or ('^' == text_list[i]) or ('raised' == text_list[i] and
        'to' == text_list[i+1]):
        # check for x raised to the power of x and give answer
            for i in range(len(text_list)):
                try:
                    f_number = float(text_list[i])
                    s_number = float(text_list[-1])
                    if str(f_number).endswith('.0'):
                        f_number = int(f_number)
                    if str(s_number).endswith('.0'):
                        s_number = int(s_number)
                    pow_num = math.pow(f_number, s_number)
                    pow_num = round(pow_num, 5)
                    if str(pow_num).endswith('.0'):
                        pow_num = int(pow_num)
                    return f'{f_number} to the power of {s_number} is {pow_num}'
                    break
                except ValueError:
                    pass

    if 'squared' in text_list and 'root' not in text_list and '-' in text_list:
        # check for x squared
        for i in range(len(text_list)):
            try:
                f_number = float(text_list[i])
                if str(f_number).endswith('.0'):
                    f_number = int(f_number)
                sqrd_num = math.pow(f_number, 2)
                sqrd_num = round(sqrd_num, 5)
                if str(sqrd_num).endswith('.0'):
                    sqrd_num = int(sqrd_num)
                return f'-{f_number} squared is {sqrd_num}'
                break
            except ValueError:
                pass
    elif 'squared' in text_list and 'root' not in text_list:
        # check for x squared
        for i in range(len(text_list)):
            try:
                f_number = float(text_list[i])
                if str(f_number).endswith('.0'):
                    f_number = int(f_number)
                sqrd_num = math.pow(f_number, 2)
                sqrd_num = round(sqrd_num, 5)
                if str(sqrd_num).endswith('.0'):
                    sqrd_num = int(sqrd_num)
                return f'{f_number} squared is {sqrd_num}'
                break
            except ValueError:
                pass
    else:
        pass

    if 'cubed' in text_list and '-' in text_list:
        # check for x cubed
        for i in range(len(text_list)):
            try:
                f_number = float(text_list[i])
                if str(f_number).endswith('.0'):
                    f_number = int(f_number)
                cbd_num = math.pow(f_number, 3)
                cbd_num = round(cbd_num, 5)
                if str(cbd_num).endswith('.0'):
                    cbd_num = int(cbd_num)
                return f'-{f_number} cubed is -{cbd_num}'
                break
            except ValueError:
                pass
    elif 'cubed' in text_list:
        # check for x cubed
        for i in range(len(text_list)):
            try:
                f_number = float(text_list[i])
                if str(f_number).endswith('.0'):
                    f_number = int(f_number)
                cbd_num = math.pow(f_number, 3)
                cbd_num = round(cbd_num, 5)
                if str(cbd_num).endswith('.0'):
                    cbd_num = int(cbd_num)
                return f'{f_number} cubed is {cbd_num}'
                break
            except ValueError:
                pass
    else:
        pass

    for i in range(len(text_list)):
        if (text_list[i] == '+' or text_list[i] == '-' or text_list[i] == '*'
        or text_list[i] == 'x' or text_list[i] == '/'):
        # check for simple equations (+, -, *, /) and give answer
            for i in range(len(text)):
                try:
                    if text[i] == '-' and (text[i+1] == type(int) or 
                    type(float)):
                        text_final = text[i:]
                        for i in range(len(text_final)):
                            if text_final[i] == 'x':
                                text_final = str(text_final).replace('x', '*')
                        evaled = eval(text_final)
                        evaled = round(evaled, 5)
                        if str(evaled).endswith('.0'):
                            evaled = int(evaled)
                        return f'the answer is {evaled}'
                        break
                    else:
                        f_number = float(text[i])
                        text_final = text[i:]
                        for i in range(len(text_final)):
                            if text_final[i] == 'x':
                                text_final = str(text_final).replace('x', '*')
                        evaled = eval(text_final)
                        evaled = round(evaled, 5)
                        if str(evaled).endswith('.0'):
                            evaled = int(evaled)
                        return f'the answer is {evaled}'
                        break
                except ValueError:
                    pass

    return ''