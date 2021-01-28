

def mainMenu():
  print('Введите пункт меню, который желаете открыть:')
  print('1 - Камень, ножницы, бумага')
  print('2 - Угадай число')
  choice = input('')
  if choice == '1':
    rock_paper_scissors()
  elif choice == '2':
    guess_the_number()
  else:
    print('Введите только номер пункта: 1 или 2')
    mainMenu()
