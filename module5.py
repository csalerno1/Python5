mycode = """
def code(x,y,z):
	return (x*y*z)+2

print(code(2,4,6))"""

exec(mycode)

def stringinmiddle(string, word):
	return string[:6]+word+string[6:]

print(stringinmiddle("small  large","medium"))
