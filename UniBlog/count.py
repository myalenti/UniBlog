fruit = ['apple','orange','grape','kiwi','orange','apple'] #defining the list

def analyze_count(l):
    try:
            
        counts = {}
    
        for i in l:
            print ('Fount item' + ' ' + i)
            #if i in counts:
            counts[i] = counts[i] + 1
            #else:
            #    counts[i] = 1
            
        return counts
    except  Exception as e:
        print "we got an execption hombre", type(e), e
        return counts
c = analyze_count(fruit)
print c