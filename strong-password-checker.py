import re


def isValidPassword(password):
    validPasswordRegex = re.compile(r'(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{8}')
    return validPasswordRegex.search(password) != None


def checkPassword(password):
    isValid = isValidPassword(password)
    print(f'valid: {password}' if isValid else f'INVALID: {password}')


passwords = [
    'abcd',
    '12345678',
    '',
    'ABCDEFGH',
    '123ABCz',
    'ABCdef12',
    '1VcV3Dad',
    'aaaaaa4F',
    'ASDFASDFASDFASDF234234TRWERT456adfgsdfg234624sg45'
]
for password in passwords:
    checkPassword(password)
