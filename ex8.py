#print("Its fleece was white as {}.".format('snow'))
#অ্যাটমে বাংলায় কমেন্ট করা যায়
formatter = "{} {} {} {}"
#these entity within format will put into curly bracec that is assined in variale named formatter
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"or a song about fear"
))
