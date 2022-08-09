from stack import Stack
from task import rows

if __name__ == '__main__':
    brackets = Stack()
    for row in rows:
        good = True
        for item in row:
            if item in '([{':
                brackets.push(item)
            elif item in ')]}':
                if brackets.is_empty():
                    good = False
                    break
                else:
                    left_bracket = brackets.pop()
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
        if good and brackets.size() == 0:
            print('Balanced')
        else:
            print('Unbalanced')
