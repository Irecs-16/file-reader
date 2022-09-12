def create_dict(filename):
    mydict={}
    with open(filename) as f:
        for file in f:
            letter = file.split(':')[0].lower()
            flower = file.split(':')[1]
            mydict[letter]=flower
        return(mydict)


def main():
    flower_dict = create_dict('flowers.txt')
    fullname = input('enter your first [space] last name  ')
    firstname = fullname[0]
    firstletter = firstname[0]
    print(f"your flower according to the first letter of your name : {firstletter} is {flower_dict[firstletter]}")

main()
