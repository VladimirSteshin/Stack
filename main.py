from stack import Stack
from task import rows

if __name__ == '__main__':
    brackets = Stack()
    for row in rows:
        brackets.stack = []  # cleaning stack
        if row:
            good = True  # creating condition for the final check below
        else:
            good = False
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
            print('Balanced')
        else:
            print('Unbalanced')
