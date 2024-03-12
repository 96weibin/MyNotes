def trim(s: str) -> str:
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ': 
        return trim(s[:-1])
    else:
        return s
    
hello = "   hello world    "
print(trim(hello))