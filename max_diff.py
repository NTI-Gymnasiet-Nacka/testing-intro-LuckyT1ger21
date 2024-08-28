# Största skillnad

def main():
    tal=input()
    sorttal=sorted(tal.split(", "))
    diff=abs(int(sorttal[len(sorttal)-1])-int(sorttal[0]))
    print(f'{tal} - {diff}')
if __name__ == "__main__":
    main()
