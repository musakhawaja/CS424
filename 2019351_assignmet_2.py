from collections import defaultdict

grammar = {
    'E': [
        ('T', '-', 'E'),
        ('T',)
    ],
    'T': [
        ('F', '*', 'T'),
        ('F',)
    ],
    'F': [
        ('id',)
    ]
}

parsing_table = defaultdict(dict)
parsing_table[0]['id'] = ('s', 5)
parsing_table[0]['('] = ('s', 4)
parsing_table[1]['-'] = ('s', 6)
parsing_table[2]['$'] = ('accept',)
parsing_table[3]['*'] = ('s', 7)
parsing_table[3]['-'] = ('r', 2)
parsing_table[3][')'] = ('r', 2)
parsing_table[3]['$'] = ('r', 2)
parsing_table[4]['id'] = ('s', 5)
parsing_table[4]['('] = ('s', 4)
parsing_table[5]['*'] = ('r', 4)
parsing_table[5]['-'] = ('r', 4)
parsing_table[5][')'] = ('r', 4)
parsing_table[5]['$'] = ('r', 4)
parsing_table[6]['id'] = ('s', 5)
parsing_table[6]['('] = ('s', 4)
parsing_table[7]['id'] = ('s', 5)
parsing_table[7]['('] = ('s', 4)
parsing_table[8]['*'] = ('r', 3)
parsing_table[8]['-'] = ('r', 3)
parsing_table[8][')'] = ('r', 3)
parsing_table[8]['$'] = ('r', 3)

# Define the LR(1) parser function
def lr1_parser(input_str):
    input_str += '$'
    stack = [0]
    symbols = ['$', 'E']
    i = 0
    
    while True:
        state = stack[-1]
        lookahead = input_str[i]
        
        if (state, lookahead) not in parsing_table:
            return False
        
        action, value = parsing_table[state][lookahead]
        
        if action == 's':
            stack.append(value)
            symbols.append(lookahead)
            i += 1
        elif action == 'r':
            lhs, rhs = grammar[symbols[-1]][value]
            for _ in range(len(rhs)):
                stack.pop()
                symbols.pop()
            state = stack[-1]
            stack.append(parsing_table[state][lhs][1])
            symbols.append(lhs)
        elif action == 'accept':
            return True

# Test the LR(1) parser function
input_str = 'id * id - id $'
result = lr1_parser(input_str)
print(result)
