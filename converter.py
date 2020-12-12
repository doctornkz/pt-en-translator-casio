f = open('Portuguese-English.tab', 'r')
print('File opened')
lines = f.readlines()
f.close()

pt_en = {}

print('File processing')
for line in lines:
    value = ''
    line_content = line.split('\t')
    key = line_content[0] # word
    value = line_content[1].rstrip()
    #print(key, line_contents)
    #print(key,value)
    pt_en[key] = value

print('Number of words processed:', len(pt_en))
f = open('pt_en.json', 'w')
print('File saving')
f.write(str(pt_en))
f.close()