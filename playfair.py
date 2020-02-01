text=input("Enter message: ")
key=input("Enter key: ")
abc="abcdefghijklmnopqrstuvwxyz"
st=""
for c in key:
    if c not in st:
        st+=c
for c in abc:
	if c == "j":
		c = "i"
	if c not in st:
		st+=c
print(st)
l1=list(st)
matrix=[[],[],[],[],[]]
for i in range(5):
    for j in range(5):
        matrix[i].append("a")
i=0
j=0
for k in st:
    matrix[i][j]=k
    j=j+1
    if j>4:
        i=i+1
        j=0
print(matrix)

pair_text = []
def pair(text):
    for pp in range(0,len(text),2):
        pair_text.append(text[pp:pp+2])

    for p in range(0,len(pair_text)):
        if pair_text[p][0]== pair_text[p][1]:
            pair_text[p][1] = 'x'

    print(pair_text)
    return pair_text

print("Plaintext is divided into pais, which are :---->")
pair(text)

def Type1(loc_first_alpha_1i,loc_first_alpha_1j,loc_second_alpha_2i,loc_second_alpha_2j):
    for i in range(0,len(pair_text)):
        cipher_pair = matrix[loc_first_alpha_1i][loc_second_alpha_2j]
        cipher_pair = cipher_pair + matrix[loc_second_alpha_2i][loc_first_alpha_1j]
    
    #print(cipher_pair) 
    return cipher_pair  


def Type2(loc_first_alpha_1i,loc_first_alpha_1j,loc_second_alpha_2i,loc_second_alpha_2j):
    for i in range(0,len(pair_text)):
        if loc_first_alpha_1j ==4:
            cipher_pair = matrix[loc_first_alpha_1i][0]
            cipher_pair = cipher_pair + matrix[loc_first_alpha_1i][loc_second_alpha_2j+1]

        if loc_second_alpha_2j ==4:
            cipher_pair = matrix[loc_first_alpha_1i][loc_first_alpha_1j+1]
            cipher_pair = cipher_pair + matrix[loc_first_alpha_1i][0]

        if (loc_first_alpha_1j!=4) and (loc_second_alpha_2j!=4):
            cipher_pair = matrix[loc_first_alpha_1i][loc_first_alpha_1j+1]
            cipher_pair = cipher_pair + matrix[loc_second_alpha_2i][loc_second_alpha_2j+1]
    #print(cipher_pair)
    return cipher_pair 


def Type3(loc_first_alpha_1i,loc_first_alpha_1j,loc_second_alpha_2i,loc_second_alpha_2j):
    for i in range(0,len(pair_text)):

        if loc_first_alpha_1i ==4:
            cipher_pair = matrix[0][loc_first_alpha_1j]
            cipher_pair = cipher_pair + matrix[loc_second_alpha_2i+1][loc_second_alpha_2j]

        if loc_second_alpha_2i ==4:
            cipher_pair = matrix[loc_first_alpha_1i+1][loc_first_alpha_1j]
            cipher_pair = cipher_pair + matrix[0][loc_second_alpha_2j]

        if (loc_first_alpha_1i!=4) and (loc_second_alpha_2i!=4):
            cipher_pair = matrix[loc_first_alpha_1i+1][loc_first_alpha_1j]
            cipher_pair = cipher_pair + matrix[loc_second_alpha_2i+1][loc_second_alpha_2j]

    #print(cipher_pair)
    return cipher_pair 


cipher_pair=[]

cipher_text=[]

def encryption(matrix,pair_text,cipher_pair):

    #print("Encrypted Ciphertext is ----->")
    for pp in pair_text:
        for i in range(0,5):
            for j in range(0,5):

                if pp[0] == matrix[i][j]:
                    loc_first_alpha_1i=i
                    loc_first_alpha_1j=j

                if pp[1] == matrix[i][j]:
                    loc_second_alpha_2i=i
                    loc_second_alpha_2j=j



        if (loc_first_alpha_1i!=loc_second_alpha_2i) and (loc_first_alpha_1j!=loc_second_alpha_2j):
            #print("{}------>".format(pp),end=" ")
            cipher_Type1 =Type1(loc_first_alpha_1i, loc_first_alpha_1j, loc_second_alpha_2i, loc_second_alpha_2j)
            cipher_text.append(cipher_Type1)
           
           
 
        if loc_first_alpha_1i == loc_second_alpha_2i:
            #print("{}---->".format(pp), end =" ") 
            cipher_Type2 = Type2(loc_first_alpha_1i, loc_first_alpha_1j, loc_second_alpha_2i, loc_second_alpha_2j)
            cipher_text.append(cipher_Type2)

        if loc_first_alpha_1j == loc_second_alpha_2j:
            #print("{}---->".format(pp), end=" ")
            cipher_Type3 = Type3(loc_first_alpha_1i, loc_first_alpha_1j, loc_second_alpha_2i, loc_second_alpha_2j)
            cipher_text.append(cipher_Type3)


encryption(matrix,pair_text,cipher_pair)
print("Ciphertext is --->")

for c in cipher_text :
    print("".join(c), end="")













    
