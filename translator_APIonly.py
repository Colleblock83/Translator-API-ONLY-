import requests
text = "Welcome to \033[1;35mLoopAnalyses\033[1;35m!"
middle = text.center(130)
print(middle)
hd2 = "Made by \033[33mColleblock83\033[0m"
middle2 = hd2.center(125)
print(middle2)
hd3 = "Donation on \033[34mPayPal\033[0m: @FabioBaensch"
middle3 = hd3.center(125)
print(middle3)
print()
print()
print("\033[0;31mExample\033[1;35m: ")
print("Gaming, Love, Minecraft usw.")
print()
print()

languages = {
    "German" : "de",
    "Russian": "ru",
    "English": "en",
    "Espaniol": "es",
    "Arabian": "ar"
}

#--------------------------------------------------------------------
#Defining Functions and giving it parameters
def translator(text, original_language, target_language):
    
    url = "https://libretranslate.com/translate"
    

    params = {
        'q' : text,  #Text which is stored in the variable text from the input "choice"
        'source' : original_language,
        'target' : target_language
    }
    send_request = requests.post(url, data=params)
    if send_request.status_code == 200:
        json_data = send_request.json().get('translatedText')   #get the translated data of the json datatype and print it
        print(f"Translated Text: \n", {json_data})
    else:
        print(f"CRITICAL ERROR: Error Code: {send_request.status_code} ") 
    





#--------------------------------------------------------------------------------------

for liste in["Available Languages: ", "English", "Arabian", "Russian", "Espaniol", "German"]:
    print(liste)
choice = input("Enter the phrase or the word you want to translate: ")
choice2 = input("Type in the usual language (Example: English): ")
choice3 = input("Type in the language you want to translate in (Example: German): ")

if choice2 in languages:
    source = languages[choice2] #wenn aus dem dictionary "languages" eines zutrifft wird dieses ausgewählt und source gegeben
    
else:
    print("CRITICAL ERROR: Language not found!")
    source = None

if choice3 in languages:
    source2 = languages[choice3]
    
else:
    print("CRITICAL ERROR: Language not found!")
    source2 = None


#Checking if all 3 inputs are valid:
if choice2 and choice3:
    translator(choice, source, source2)
else: 
    print("CRITICAL ERROR: One or more invalid inputs.")

