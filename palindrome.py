# Palindrome

def main():
    palidrom=True
    ordet=input()
    ordet.lower()
    gånger=len(ordet)
    for n in range(0,gånger):
        if ordet[n]!=ordet[gånger-n-1]:
            palidrom=False
    print(palidrom)

if __name__ == "__main__":
    main()
