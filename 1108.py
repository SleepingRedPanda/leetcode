def defangIPaddr(address: str) -> str:
    # return address.replace('.', '[.]')
    return '[.]'.join(address.split('.'))

print(defangIPaddr("1.1.1.1"))