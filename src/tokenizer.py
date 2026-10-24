def tokenize(text: str) -> list[str]:
    token = []
    for c in text.split(' '):
        if '_' or '-' in c:
            c.split('_' or '-')
        token.append(c)
    return token
    
