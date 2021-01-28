import random

def rock_paper_scissors():
  comp = random.choice(['камень', 'ножницы', 'бумага'])
  player = input('Введите "камень", "ножницы" или "бумага", чтобы показать соответствующий жест:\n')
  if player == 'камень' or player == 'ножницы' or player == 'бумага':
    print(f'Вы выбрали {player}, у компьютера - {comp}...')
    if (player == 'камень' and comp == 'ножницы') or (player == 'ножницы' and comp == 'бумага') or (player == 'бумага' and comp == 'камень'):
      print('Вы победили!')
    elif player == comp:
      print('Ничья!')
    else:
      print('Вы проиграли!')
    print('1 - сыграть еще раз')
    print('0 - выйти в главное меню')
    choice = input()
    if choice == '1':
      rock_paper_scissors()
    elif choice == '0':
      mainMenu()
    else:
      print('Не понял, чего Вы хотите. Выхожу в главное меню.')
      mainMenu()
  else:
    print('Введите "камень", "ножницы" или "бумага", чтобы показать соответствующий жест.\nДругое вводить не надо!\n')
    rock_paper_scissors()

def guess_the_number():
  comp_number = random.randint(1, 100)
  print('Я загадал число от 1 до 100. Попробуй его отгадать!')
  attempts = 1
  while True:
    player = input()
    if player.isdigit():
      player = int(player)
    else:
      print('Вводи только целые числа!')
      print('Давай попробуем еще раз.')
      guess_the_number()
  
    if player == comp_number:
      print(f'Надо же! Угадал с {attempts} попытки. Молодец!')
      break
    elif player < comp_number:
      print('Попробуй взять число побольше.')
      attempts += 1
      continue
    else:
      print('Мое число меньше...')
      attempts += 1
      continue
  print('1 - сыграть еще раз')
  print('0 - выйти в главное меню')
  choice = input()
  if choice == '1':
    rock_paper_scissors()
  elif choice == '0':
    mainMenu()
  else:
    print('Не понял, чего Вы хотите. Выхожу в главное меню.')
    mainMenu()
