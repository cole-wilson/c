import os,time

os.chdir('/')

while True:
  l = os.system('ls')
  

  #print(f)
  print('-------------------------------------------------------------------------------------------------------')
  print(  '1. Edit, 2. CD,  3. View, 4. Delete, 5. Git,  6. New File, 7. New Directory, 8. Run')
  print('-------------------------------------------------------------------------------------------------------')
  
  try:
    ch = input('>>>')
  except:
    print('INCORRECT CHOICE!!')
    os.system('clear')
  
  if int(ch) == 2:
    c = input('Directory: ')
    try:
      os.chdir(os.getcwd() + '/' + c)
    except NotADirectoryError:
      print(c + ' is not a directory.')
    except FileNotFoundError:
      print(c + ' is not a file or directory')
    os.system('clear')
  elif int(ch) == 3:
    c = input('File: ')
    os.system('clear')
    try:
      os.system('cat ' + c + '')
      input('\n\n\n\n\n\n\n\n\n\n\n\n\u001b[0m\u001b[7m Press enter key to continue.\u001b[0m')
    except:
      print(c + ' is not a directory.')
    
  elif int(ch) == 7:
    os.system('mkdir ' + input('Directory Name:'))
    os.system('clear')
  elif int(ch) == 6:
    os.system('touch ' + input('File Name:'))
    os.system('clear')
  elif int(ch) == 4:
    os.system('rm -r' + input('Name:'))
    os.system('clear')
  elif int(ch) == 5:
    os.system('git ' + input('URL:'))
    os.system('clear')
  elif int(ch) == 8:
    ff = input('File:')
    os.system('chmod +x ' + ff)
    if '.py' in ff:
      os.system('python3 ' + ff)
    elif '.sh' in ff:
      os.system('sh ' + ff)
    os.system('clear')
    