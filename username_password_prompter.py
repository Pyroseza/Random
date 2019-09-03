import getpass

# a generic input function that can prompt a user for something
# and if it is a password it will not echo back what is typed in
# also can force a user to enter something that is not blank
def get_input(prompt='', password=False, can_be_empty=False):
  return_string = ''
  while True:
    if password == True:
      return_string = getpass.getpass(prompt=prompt)
    else:
      return_string = input(prompt)
    # if allowed to be empty then break regardless of input
    if can_be_empty == True:
      break
    # if not allowed to be empty then check what has been entered
    if can_be_empty == False and len(return_string.strip()) > 0:
      break
  return return_string

def username_password():
  # ask for a username
  username = get_input(prompt="Please enter your username: ")
  print(f"Hello {username}")
  attempts=5
  # ask for the password, the user has n attempts
  for attempt in range(attempts):
    password = get_input(prompt='Please enter your password: ', password=True)
    if username == 'pyro' and password == 'p@ssw0rd':
      print(f'Correct, welcome {username}')
      break
    al = attempts-attempt-1
    if al == 0:
      print("sorry you failed to enter the correct credentials")
      break
    print('Incorrect credentials')
    print(f"try again, {al} attempt{'s' if al > 1 else ''} left...")

username_password()

