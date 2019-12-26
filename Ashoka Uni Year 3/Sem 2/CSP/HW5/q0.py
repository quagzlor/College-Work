xor_num = '01001100100010100100010111100100110010110001111111110011101011100000110000010010001110110000111001111010010011101101001010000010'
input_num = '100011001101110101110010110110111010001110101011111111001110110'
pre_state = '0111101000110010000110111111000001010010010001110001100000111000'

def pad(num):
    bin_num = num
    bin_num = bin_num + "1"
    bin_num = bin_num + "0"*(63-len(bin_num))
    bin_num = bin_num + "1"

    return (bin_num)

def xor(a,b): #XOR function, easier than using python's built in
    xor_ed = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            xor_ed = xor_ed + '0'
        else:
            xor_ed = xor_ed + "1"
    return xor_ed

def left_Shift(num):
    shift_val = num[:8]
    to_xor = '01100101'
    shift_val = xor(shift_val,to_xor)
    shift_val = int(shift_val,2)
    shift_val = shift_val%128


    shifted_array = num[shift_val:] + num[:shift_val]
    
    return shifted_array

state_num = xor(input_num,pre_state)
state_num = state_num + '0'*(64)

count = 0
while count < 20:
    state_num = xor(state_num,xor_num)

    state_num = left_Shift(state_num)

    count += 1

print (state_num[:56])
