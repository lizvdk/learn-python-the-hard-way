from sys import argv

script, user_name = argv
prompt = '--> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "How old are you?"
age = raw_input(prompt)

print "I got it, you are %s" % age
