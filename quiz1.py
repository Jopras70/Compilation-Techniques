def is_keyword(s):
    keyword_list = ['while', 'int', 'float', 'const', 'main']
    return s in keyword_list

def tokenize(s):
    tokens = []
    lexemes = []
    x = 0
    while x < len(s):
        if s[x].isspace():
            x += 1
        elif s[x:x+2] == '//':
            x = s.find('\n', x)
        elif s[x:x+2] == '/*':
            x = s.find('*/', x)
            if x == -1:
                # Handle unclosed multi-line comment
                break
            x += 2
        elif s[x].isalpha():
            y = x + 1
            while y < len(s) and (s[y].isalpha() or s[y].isdigit()):
                y += 1
            token_value = s[x:y]
            if is_keyword(token_value):
                tokens.append('keyword')
                lexemes.append(token_value)
            else:
                tokens.append('identifier')
                lexemes.append(token_value)
            x = y
        else:
            x += 1
    return tokens, lexemes

text = 'int main(){const float payment = 384.00;float bal;int month = 0;bal=15000;while (bal>0){printf("Month: %2d Balance: %10.2f\n", month, bal);bal=bal-payment+0.015*bal;month=month+1;}}'

tokens, lexemes = tokenize(text)

for token, lexeme in zip(tokens, lexemes):
    print(f"{token}: {lexeme}")
