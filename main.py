from stack import Stack


def check_row(row):
    good = True  # creating condition for the final check below
    brackets = Stack()
    brackets.stack = []  # cleaning stack
    if row:
        for item in row:
            if item in '([{':  # finding left bracket
                brackets.push(item)
            elif item in ')]}':  # finding right bracket
                if brackets.is_empty():
                    good = False
                    break
                else:
                    left_bracket = brackets.pop()  # take the upper bracket from stack and compare
                    if left_bracket == '(' and item == ')':
                        continue
                    elif left_bracket == '[' and item == ']':
                        continue
                    elif left_bracket == '{' and item == '}':
                        continue
                    else:
                        good = False
                        break
            else:
                good = False
                break
        if good and brackets.size() == 0:  # if our condition status is 'good' and the stack is clean
            return 'Balanced'
        else:
            return 'Unbalanced'
    else:
        return 'Unbalanced'


if __name__ == '__main__':
    print(check_row(''))

