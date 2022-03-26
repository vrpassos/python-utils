import sys

def crc16(buff, crc = 0):
    i = 0
    l = len(buff)
    while i < l:
        byte = ord(buff[i])
        cnt = 0
        while cnt < 8:
            if (crc & 1) ^ (byte & 1):
                crc = (crc >> 1) ^ 0xa001
            else:
                crc = crc >> 1
            byte = byte >> 1
            cnt = cnt + 1
        i = i + 1
    return crc
    
if __name__ == "__main__":      
    args = sys.argv[1:]

    in_str = str(args[0])    

    with open(in_str) as file:
        file_str = file.read()    
    
    print(file_str)

    print(crc16(file_str))