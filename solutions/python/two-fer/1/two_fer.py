def two_fer(name):
    if name and isinstance(name, str):
        return f"One for {name}, one for me."
    elif name == '':
        return "One for you, one for me."

    raise TypeError("missing 1 required positional argument: 'name'")
       
            
            
if __name__ == '__main__':
    print(two_fer('Joel'))
    print(two_fer(''))
    print(two_fer(1))
