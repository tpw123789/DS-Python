
class Stack1:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack2:
    """reverse"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)


def par_checker(symbol_string):
    """判斷括號符號對稱"""
    stack = Stack1()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            stack.push(symbol)  # 左符號push到stack
        else:
            if stack.is_empty():  # 不是左符號但是stack為空，不對稱
                balanced = False
            else:
                top = stack.pop()  # pop出右符號
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and stack.is_empty():
        return True  # balanced=True 且stack為空，對稱
    else:
        return False  # stack還有殘留左括號


def matches(par_open, par_close):
    opens = '([{'
    closers = ')]}'
    return opens.index(par_open) == closers.index(par_close)


def divide_by_2(dec_number, base):
    """轉換進制"""
    digits = '123456789ABCDEF'
    stack = Stack1()

    while dec_number > 0:
        rem = dec_number % base  # 除2的餘數
        stack.push(rem)
        dec_number = dec_number // base
    bin_string = ''

    while not stack.is_empty():
        bin_string += digits[stack.pop()]

    return bin_string


def infix2postfix(infix_expr):
    import string
    priority = dict()  # 優先級別
    priority['*'] = 3
    priority['/'] = 3
    priority['-'] = 2
    priority['('] = 1

    stack = Stack1()
    postfix_list = []
    token_list = infix_expr.split()  # 分割中序式
    for token in token_list:
        if token in string.ascii_uppercase:
            postfix_list.append(token)
        elif token == '(':
            pass


