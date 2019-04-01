print("\n\n----- >>>>> Checksum Generator & Checker <<<<< -----\n\n")

n = int(input("Number of Data : "))
bits = int(input("Number of Bits per Data : "))
data = []
data_y = []
sum_x = '0000'
sum_y = '0000'


print("--- >>> Checksum Generator <<< ---")
print(' ')

for i in range(n):
    data.append(input("Enter Data No." + str(i+1) + " : ")[:bits])
    sum_x = bin(int(data[i], 2) + int(sum_x, 2))[2:]
    if len(sum_x) > bits:
        sum_x = bin(int('1', 2) + int(sum_x, 2))[3:]

 
for i in range(bits):
    if sum_x[i:i+1] == '0':
        sum_x = sum_x[:i] + '1' + sum_x[i+1:]
    else:
        sum_x = sum_x[:i] + '0' + sum_x[i+1:]

print('\nChecksum : ' + sum_x)


# Checksum checker
print("\n\n\n--- >>> Checksum Checker <<< ---\n")


for i in range(n):
    data_y.append(input("Enter Data No." + str(i+1) + " : ")[:bits])
    sum_y = bin(int(data_y[i], 2) + int(sum_y, 2))[2:]
    if len(sum_y) > bits:
        sum_y = bin(int('1', 2) + int(sum_y, 2))[3:]


result = bin(int(sum_x, 2) + int(sum_y, 2))[2:]
check = '1'*bits
if result == check:
    print("\nData is Valid")
else:
    print("\nData is corrupted")