import tokenize
reader = open('p028.py').next
tokens = tokenize.generate_tokens(reader)
tokens.next()
tokens.next()
