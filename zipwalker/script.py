import struct
import sys


CD = "504b0102"   # Central Directory
LFH = "504b0304"  # Local File Header
EOCD = "504b0506" # End of central directory


def little_endian_to_int(hexstr: str):
    hexbytes = bytearray.fromhex(hexstr)
    hexbytes.reverse()
    return int(hexbytes.hex(), 16)

file_in = open("dump.zip", "rb")

bytestring = file_in.read().hex()

# gather positions of valid central directory headers
positions = []
start = 0
while (cur := bytestring.find("504b0506", start)) != -1:  # Find All "EOCDs"
    offset_start = cur + 2 * 16                           # Get offset of "CD"  
    pos = little_endian_to_int(bytestring[offset_start: offset_start + 2 * 4]) * 2
    positions.append(pos)

    start = cur + 1

# collect valid headers and flag letters
flag_letters = dict()
for pos in positions:
    central = bytestring[pos: bytestring.find("504b0102", pos + 1)]     # Central Diretory
    local_pos = little_endian_to_int(central[2 * 42: 2 * 46]) * 2
    local = bytestring[local_pos: bytestring.find("504b0304", local_pos + 1)]   # Local File Header

    if local[60:68] == "flag".encode("utf8").hex():
        data = bytes.fromhex(local[68:74]).decode("ascii")
        flag_letters[int(data[0:2])] = data[2]

flag = ""
items = list(flag_letters.items())
items.sort()
for (key, value) in items:
    flag += value
print("The flag is: " + flag)