def two_fer(name=''):
    return f'One for {name}, one for me.' if name else 'One for you, one for me.'
 
            
if __name__ == '__main__':
    print(two_fer('Joel'))
    print(two_fer())
