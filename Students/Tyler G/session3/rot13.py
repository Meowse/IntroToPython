# Returns a dictionary of the alphabet encrypted. The shift value is 13 by default.
def code_shift(shift = None):
    if shift == None:
        shift = 13
    letters = "abcdefghijklmnopqrstuvwxyz"
    coder = {}
    x = 0
    for i in range(len(letters)):
        if i < (len(letters)-shift):
            coder[letters[i]] = letters[i + shift]
        else:
            coder[letters[i]] = letters[x]
            x += 1
    return coder

def rot13(n):
    encrypted = code_shift()
    holder = " "
    for char in n:
        if char.lower() in encrypted:
            if char == char.lower():
                holder += encrypted[char.lower()]
            else:
                holder += encrypted[char.lower()].upper()
        else:
            holder += char
    return holder.lstrip(" ")
            
        
        