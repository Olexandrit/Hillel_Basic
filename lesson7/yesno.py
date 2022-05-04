def yes_or_no(message='Yes or No? ', valid_answer='yes'):
    """
    -- Docstring - строка документації. Описує що робить функція. --
    Asks user Yes or No. If user answers anything except "yes" - app will exit.
    Message and correct answer can be modified with arguments `message` and `valid_answer`
    """
    answer = input(message)
    if answer.lower() != valid_answer:
        print('Okay ;(')
        exit()


def ask_to_show(name, show):
    print(f'Do you want to see {name}?')
    yes_or_no()
    print(f'Wow, take a look: {show}')


while True:
    ask_to_show('cucumber', '🥒')
    ask_to_show('banana', '🍌')

    yes_or_no('Want to try again? Enter "+" to run again: ', '+')