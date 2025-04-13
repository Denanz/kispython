def main(x):
    U1 = (x >> 0) & 0b11111
    U3 = (x >> 8) & 0b111111111
    U4 = (x >> 17) & 0b111111111
    U5 = (x >> 26) & 0b1111
    U6 = (x >> 30) & 0b1111111 

    result = 0
    result |= (U5 << 0)
    result |= (U3 << 4)
    result |= (U6 << 13)           
    result |= (U4 << 20)           
    result |= (U1 << 32)          

    return str(result)