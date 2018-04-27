global tap_positions
bits = input("Length of the shift register:")
tap_positions = input("Enter the tap positions:").split(',')
inp_data = list(input("Seed value:"))
inp_data = [int(i) for i in inp_data]
op_bits = input("Number of clock cycles:")

tap_positions = [int(i) for i in tap_positions]

def xor():
    xor = temp_list1[inp_leng-1]
    for i in range(len(tap_positions)-1):
        xor = temp_list1[tap_positions[i]] ^ xor
    temp_list2.append(xor)
    return temp_list2



inp_data.insert(0,inp_data[len(inp_data)-1])
inp_data.pop()

output = [0]
inp_leng = len(inp_data)
temp_list1 = inp_data
temp_list2 = []
for i in range(int(op_bits)):
    output.insert(0,temp_list1[inp_leng-1])
    xor()
    for i in range(inp_leng - 1):
        temp_list2.append(temp_list1[i])

    temp_list1 = temp_list2
    temp_list2 = []


output.pop()
output.reverse()
output_data = ''.join(str(x) for x in output)
print(output_data)