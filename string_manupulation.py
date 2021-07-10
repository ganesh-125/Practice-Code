# I/P -> aaabbccaad
# O/P -> a3b2c2a2d1


def encode(message):
    count = 0
    chatacter = ''
    previous_char = message[0]
    result = ''
    length = len(message) 
    
    i = 0
    while (i != length ):
        chatacter = message[i]
        
        if previous_char == chatacter :
            count = count + 1
        else :
            result = result + previous_char  + str(count)
            count = 1
        #print(str(i) + str(chatacter) + str(previous_char) + "          " + str(result))
        previous_char = chatacter
        i = i + 1
        
    return result  + str(previous_char)+ str(count)


encoded_message=encode("aaabbccaad")
print(encoded_message)

