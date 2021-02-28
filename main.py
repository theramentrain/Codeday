print('Ay yo, welcome!')

ans = input('Do you think you have perfect pitch? (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. What note is this? ')
    if ans == 'B':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
    ans = input('2. What note is this? ')
    if ans == 'G':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ('3. What note is this? ')
    if ans == 'F':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('4. What note is this? ')
    if ans == 'C#':
            score += 1
            print('Correct')
    else:
        print('Incorrect')

    ans = input('5. What note is this? ')
    if ans == 'D':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

print('Thank you for playing, you got ', score, " notes correct.")
mark = (score/total_q) * 10