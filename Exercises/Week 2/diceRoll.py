from random import randint
select = 1
while(select == 1):
    diceOne = randint(1,6)
    diceTwo = randint(1,6)

    sum = diceOne + diceTwo

    print(f'Sum is {sum}')

    if (sum == 7 or sum == 11):
        print('You win!')
    else:
        print('You lose')

    select = int(input("Type 1 to roll again, or anything else to end: "))