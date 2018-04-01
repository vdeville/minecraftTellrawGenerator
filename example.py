from minecraftTellrawGenerator import minecraftTellrawGenerator as mctellraw

hover = mctellraw(text='Hooooooooooover text', bold=True, color='blue')

a = mctellraw(
    text='My super text',
    color='light_purple',
    italic=True,
    bold=True,
    insertion='/say hello',
    click='Hello all !',
    hover=hover
)


b = mctellraw(
    text="Another text",
    underlined=True,
    strikethrough=True
    )

c = mctellraw(text="JUST FOR FUN", obfuscated=True, bold=True)

# Get output:
print(a)
# Or in certain case you need to cast
print(str(a))

# Get all messages in one:
print(mctellraw.multiple_tellraw(a, b, c))

# OR old / classic method
print('[' + str(a) + ', ' + str(b) + ', ' + str(c) + ']')
