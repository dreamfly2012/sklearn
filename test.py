from nltk.corpus import names 



if __name__ == "__main__":
    print("\nNumber of male names:")
    print (len(names.words('male.txt')))
    print("\nNumber of female names:")
    print (len(names.words('female.txt')))
    male_names = names.words('male.txt')
    female_names = names.words('female.txt')
    print("\nFirst 10 male names:")
    print (male_names[0:15])
    print("\nFirst 10 female names:")
    print (female_names[0:15])
