

def xor_bytes(str1, str2):
    return bytes(a ^ b for (a, b) in zip (str1, str2))

def xor(x):
    return bytearray.fromhex(x)

KEY1 = xor("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")

KEY2 = xor("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2 = xor_bytes(KEY2, KEY1)


KEY3 = xor("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
KEY3 = xor_bytes(KEY3, KEY2)

FLAG123 = xor("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
FLAG123 = xor_bytes(FLAG123, KEY1)
FLAG123 = xor_bytes(FLAG123, KEY2)
FLAG123 = xor_bytes(FLAG123, KEY3)

print(FLAG123)

    