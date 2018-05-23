from random import randint

def main():
    words = ['hi.','why hello there!','How are you?', 'you can do it!', 'how was your day?','I like greenhams.','what\'s your favorite color?','what\'s your favorite type of cookie?','Bonjour!','2+2=?','Good luck!','An apple a day keeps the doctor away!','Why don\'t woodchucks chuck wood?','Is it pronounced crayon or crayon?']

    r=randint(0,len(words)-1)
    a = False
    if (r==5):
        r=0
        a = True

    if(a):
        print("flag{" + words[r] + "}")
    else:
        print(words[r])
main()
