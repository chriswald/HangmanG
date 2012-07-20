import sys

lines = []
sys.stdout.write('Read...')
sys.stdout.flush()
for name in sys.argv[1:]:
    wordsfile = open(name, 'r')
    for line in wordsfile.readlines():
        lines.append(line)
    wordsfile.close()
sys.stdout.write('Done\n')

print(str(len(lines)) + ' lines read')

sys.stdout.write('Lower...')
sys.stdout.flush()
for i in range(len(lines)):
    lines[i] = lines[i].lower()
sys.stdout.write('Done\n')

sys.stdout.write('Sort...')
sys.stdout.flush()
lines.sort()
sys.stdout.write('Done\n')

sys.stdout.write('Clean...')
sys.stdout.flush()
index = 0
while True:
    end = len(lines) - 1
    if index == end:
        break;
    if lines[index] == lines[index+1]:
        lines.remove(lines[index])
        index -= 1
    index += 1
sys.stdout.write('Done\n')

print(str(len(lines)) + ' lines final count')

sys.stdout.write('Write...')
sys.stdout.flush()
wordsfile = open('output.txt', 'w')
for line in lines:
    wordsfile.write(line)
wordsfile.close()
sys.stdout.write('Done\n')
print('DONE')
