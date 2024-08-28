# Medelvärde

def main():
    talet=input()
    talen=talet.split(", ")
    antal=len(talen)
    zalen=[]
    for i in range(0,antal):
        zalen.append(int(talen[i]))
    print(f'{sum(zalen)/antal}')
if __name__ == "__main__":
    main()
