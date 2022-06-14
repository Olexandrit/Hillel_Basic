# Заголовок (H1)
## Підзаголовок (H2)
### Підпідзаголовок (H3)

Це буде відображатися
однією строкою.

А це буде на іншій.

**Цей текст буде жирненьким.**

_А цей курсивом._

__Так__ також буде жирненькиим, а *так* курсивом, але краще використовувати * - для жирного, _ - для курсиву.

***А так буде і жирненьким і курсивом.***

> Ось це цитата

> ## Це цитата
>
> на декілька строк
> з **жирним** та _курсивним_ текстом

> А трохи нижче цитата в цитаті
>> Я тут, в мене є ще цитата:
>>> Привіт)

>>>>>>>>>>>>>> Це може зайти доволі далеко

### Списки:

Нумерований список:
1. Перший
2. Другий
3. Третій
4. Четвертий

Все ще нумерований список:
1. Перший
1. Другий
1. Третій
1. Четвертий

Списки в списках:
1. Перший
    1. ПідПерший
    1. ПідДругий
1. Другий
    1. ПідПерший
        1. ПідПідПерший
        1. ПідПідДругий
    1. ПідДругий
        1. ПідПідПерший
        1. ПідПідДругий
1. Третій
    1. ПідПерший
        1. ПідПідПерший
            1. ПідПідПідПерший
            1. ПідПідПідДругий
        1. ПідПідДругий
            1. ПідПідПідПерший
            1. ПідПідПідДругий
    1. ПідДругий
        1. ПідПідПерший
            1. ПідПідПідПерший
            1. ПідПідПідДругий
        1. ПідПідДругий
            1. ПідПідПідПерший
            1. ПідПідПідДругий
1. Четвертий

Ненумерований список:
- Огірок
- Помідор
- Баклажан
- Гарбуз

Списки в списках:
- Перший
    - ПідПерший
        - ПідПідПерший
            - ПідПідПідПерший
            - ПідПідПідДругий
            - ПідПідПідТретій
        - ПідПідДругий
            - ПідПідПідПерший
            - ПідПідПідДругий
    - ПідДругий
- Другий

`print('таким чином можна відобразити код')`

```
message = '''
А таким чином багато строк коду
'''

print(message)
```

```python
message = 'Також можна вказати мову програмування.'
langs = 'Тут можна знайти список мов, що (зазвичай) підтримуються:'
link = 'https://rdmd.readme.io/docs/code-blocks#language-support'

print(' '.join((message, langs, link)))
```

---

Ось там зверху лінія якою можно розділити якісь секції

Отак виглядає [посилання](https://uk.wikipedia.org/wiki/Посилання)

Можна навіть додати спливаючий текст до [посилання](https://uk.wikipedia.org/wiki/Посилання "це посилання на посилання :)")


Зображення з котиком:

![Тут буде котик](http://placekitten.com/200/300)


Шпаргалка де можна знайти більше про синтаксіс Markdown: https://www.markdownguide.org/cheat-sheet/