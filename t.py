import rstr 


# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# RegExp literal
t_RCONST = r'R\"([^\\\n]|(\\.))*?\"'


# Template literal
t_TCONST = r'T\"([^\\\n]|(\\.))*?\"'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''


# Comments
t_comment = r'(/\*(.|\n)*?\*/)|(//.*\n?)'
	
for i in range(0, 10):
	n = rstr.xeger(t_RCONST)
	print (n)
