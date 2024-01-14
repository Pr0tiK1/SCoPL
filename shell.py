import basic

print('''
   _____ ______      ____  __ 
  / ___// ____/___  / __ \/ / 
  \__ \/ /   / __ \/ /_/ / /  
 ___/ / /___/ /_/ / ____/ /___
/____/\____/\____/_/   /_____/
   _____ __  __________    __ 
  / ___// / / / ____/ /   / / 
  \__ \/ /_/ / __/ / /   / /  
 ___/ / __  / /___/ /___/ /___
/____/_/ /_/_____/_____/_____/

SCoPL (acronym for 'super cool programming language')                           
use in terminal environment only
''')

while True:
	text = input('$- ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))