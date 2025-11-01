a=b'h\x65llo'
print(list(a))
print(a)
def to_str(bytes_or_str,):
    if isinstance(bytes_or_str,bytes):
        value=bytes_or_str.decode('utf-8')
    else:
        value=bytes_or_str
    return value#str实例
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
