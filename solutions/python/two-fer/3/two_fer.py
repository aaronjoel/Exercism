def two_fer(name=None):
    if name:
        return f'One for {name}, one for me.'
    else:
        return 'One for you, one for me.'

#    if isinstance(name, str):
#        if len(name) > 0:
#            return f"One for {name}, one for me."
#        else:
#            return f"One for you, one for me."
#    elif not isinstance(name, str):
#        raise TypeError('expected argument of type str')
#    else:
#        raise TypeError("missing 1 required positional argument: 'name'")
#
#    if name and isinstance(name, str):
#        return f"One for {name}, one for me."
#    elif name == '':
#        return "One for you, one for me."

#    raise TypeError("missing 1 required positional argument: 'name'")
       
            
            
if __name__ == '__main__':
    print(two_fer('Joel'))
    print(two_fer())
