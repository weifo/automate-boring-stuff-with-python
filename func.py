# print('apple'*3)

def somefunc():
    thenum=23
    while True:
        num=int(input('give me a number: '))
        if num<thenum:
            print('too low')
        elif num>thenum:
            print('too big')
        else:
            print('correct')
            break
# print(somefunc.__name__)
# print(dir(somefunc))
# somefunc()

def bacon():
    eggs=99
    spam(eggs)
    print(eggs)

def spam(eggs):
    eggs=eggs+10
    print(eggs,'in the spam')
    ham=101

# bacon()

# 3 turn a integer into 1
def collatz(num):
    if num%2==0:
        return num/2
    else:
        return 3*num+1

def main():
    try:
        num=int(input('give me a number: '))
        while num!=1:
            num=collatz(num)
        print(f'done,the num is {num} now')
    except Exception as e:
        print(e)

main()