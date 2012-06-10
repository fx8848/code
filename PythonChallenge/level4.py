import urllib

nothing = '12345'
while True:
    print nothing
    content = urllib.urlopen('http://pythonchallenge.com/pc/def/linkedlist.php?nothing=%(nothing)s' % locals()).read()
    try:
        nothing = str(int(content.split(' ')[-1]))
    except ValueError:
        if 'Divide' in content:
            nothing = str(int(nothing) / 2)
        else:
            break

print content
