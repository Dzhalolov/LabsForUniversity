import random


def fi(n):
    f = n
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2
        f = f // 2
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i
            f = f // i
            f = f * (i-1)
        i = i + 2
    if n > 1:
        f = f // n
        f = f * (n-1)
    return f


def find_d(e, n):
    for d in range(1000000):
            if e * d % (n) == 1:
                return d
            
            
def str_to_numbers(mes):
    for i in range(0, len(mes)):
        mes[i] = ord(mes[i]); #конвертируем из string в long int
        
    return mes


def numbers_to_str(mes):
    mes_list = list(map(chr, mes))
    mes_str = "".join(mes_list)
    
    return mes_str


def encode_A(string, e, n):
    out1 = []
    mes = str_to_numbers(string)
    for i in range(0,len(mes)): #от нуля до конца массива
        c=mes[i]**e
        c=c%n
        out1.append(c)
    
    result = numbers_to_str(out1)
    
    return result


def decode_A(encoding_string, d, n):
    out2 = []
    out_encoded = str_to_numbers(encoding_string)
    for i in range(0, len(out_encoded)):
        c = out_encoded[i] ** d
        c = c % n
        out2.append(c)
    
    result = numbers_to_str(out2)
    
    return result


def encode_B(string, e, n):
    out1 = []
    mes = str_to_numbers(string)
    for i in range(0,len(mes)): #от нуля до конца массива
        c=mes[i]**e
        c=c%n
        out1.append(c)
    
    result = numbers_to_str(out1)
    
    return result


def decode_B(encoding_string, d, n):
    out2 = []
    out_encoded = str_to_numbers(encoding_string)
    for i in range(0, len(out_encoded)):
        c = out_encoded[i] ** d
        c = c % n
        out2.append(c)
    
    result = numbers_to_str(out2)
    
    return result

if __name__ == '__main__':
    string = input('Enter message: ')
    string_list = list(string)
    
    while True:
        p = random.randint(900, 2000)
        k = random.randint(10, 100)
        e = random.randint(10, 100)
        if isprime(p) and coprime(fi(p), k) and coprime(fi(p), e):
#             print(p, q)
            break
    
    fi_p = fi(p)
    d = find_d(e, fi_p)
    f = find_d(k, fi_p)

    mes_encode_A = encode_A(string_list, e, p)    
    print(f'Alice encoding message with e-key: {mes_encode_A}')
    
    mes_encode_B = encode_B(list(mes_encode_A), k, p)    
    print(f'Alice encoding message with e-key: {mes_encode_B}')

    mes_decode_A = decode_A(list(mes_encode_B), d, p)    
    print(f'Alice encoding message with e-key: {mes_decode_A}')

    mes_decode_B = decode_B(list(mes_decode_A), f, p)    
    print(f'Alice encoding message with e-key: {mes_decode_B}')
