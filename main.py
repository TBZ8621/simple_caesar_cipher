from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_direction, start_text, shift_amount):
    cipher_alphabet = alphabet[shift_amount:] + alphabet[:shift_amount]
    text_list = list(start_text)
    end_text = ""
    
    for n in range(len(text_list)):
        if cipher_direction == "encode":
            for c in range(len(alphabet)):
                if text_list[n] == alphabet[c]:
                    end_text += cipher_alphabet[c]
        elif cipher_direction == "decode":
            for c in range(len(cipher_alphabet)):
                if text_list[n] == cipher_alphabet[c]:
                    end_text += alphabet[c]
                    
        if text_list[n] == " ":
            end_text += " "
            
    print(f"The {cipher_direction}d text is {end_text}")

should_continue =  True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "encode" and direction != "decode":
        print("Error invalid value!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        
    input_text = input("Type your message:\n").lower()
    while input_text == "":
        print("Error invalid value!")
        input_text = input("Type your message:\n").lower()
        
    shift = int(input("Type the shift number:\n")) % 26    
    caesar(cipher_direction=direction, start_text=input_text, shift_amount=shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if result == "no":
        should_continue = False
        print("Goodbye")
        
 
    
    
    