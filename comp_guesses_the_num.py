print('Загадай число от 1 до 100.')
print('А я его буду отгадывать.')
print('Отвечай 1 - если я угадал, 2 - если твое число больше моего и 3 - если твое число меньше моего.')
attempt = 50
counter = 1
minimal_possible = 1
maximal_possible = 100
while True:
  #next_attempt = int((maximal_possible - minimal_possible)/ 2)
  answer = input('Ты загадал ' + str(attempt) + '? ' )
  if answer == '2':
    minimal_possible = attempt + 1
    attempt += round((maximal_possible - minimal_possible)/ 2)
  elif answer == '3':
    maximal_possible = attempt - 1
    attempt -= int((maximal_possible - minimal_possible)/ 2)
  elif answer == '1':
    break
  else:
    print('Отвечай только 1, 2 или 3!')
  counter += 1
print('Я угадал! Число попыток:', counter)
