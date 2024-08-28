# Vokalräkning
VOKAL=["a","e","i","o","u","y","å","ä","ö"]
def main():
    counter=0
    text=input("")
    texten=text.lower()
    for i in range(0,len(texten)):
        if texten[i] in VOKAL:
            counter+=1
    print(f'{counter}')
if __name__ == "__main__":
    main()