languages = ['spanish.txt', 'german.txt', 'english.txt']

def make_frequency_list(filename):
    with open(filename, 'r', errors='ignore') as myfile:
        data = myfile.read()
        datastrip = data.strip("'|©!@#$%^&*()-_=+,.;:?/<>'")
        bigword = datastrip.split()
        counts = dict()
        for word in bigword:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
                
    
        freq_dict = {}
        total = sum(counts.values())
        for word, count in counts.items():
            freq_dict[word] = (1.0 * count)/total
           
        pairlist = sorted(freq_dict.items(), key=lambda kv: kv[1], reverse=True) 
        return pairlist[0:10]

def diff_frequency(known, unkown):
   diff = 0
   for i in range(len(known)):
       kn = known[i]
       for unk in unkown:
           if kn[0] == unk[0]:
               diff += abs(kn[1] - unk[1])
   return diff

frequencies = []
for lang in languages:
    freq = make_frequency_list(lang)
    print(freq)
    frequencies.append(freq)
    
unkown = make_frequency_list('unknown.txt')

winner = -1
smallest = 100000

for i in range(len(languages)):
    diff = diff_frequency(frequencies[i], unkown)
    if diff < smallest:
        smallest = diff
        winner = i
        
print('The closest matching language is ', languages[i])
