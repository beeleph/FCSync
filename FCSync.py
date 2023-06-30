import os

# prepare list of files from dirac file catalogue. FClist
FCfile = open('FClist', 'r')
FClist = []
for line in FCfile:
    line = line.strip()
    FClist.append(line)
FCfile.close()
addToCounter = 0 # how much is missing in the FC
result = open('FCSyncResult.txt', 'w')
result.write('Files that was not added to file catalogue: \n')
print('Number of files that was not added to file catalogue: ', end='')
for subdir, dirs, files in os.walk("TestFolda"): #there should be bmn.jinr.ru. 
    for file in files:
        filepath = "/" + subdir + os.sep + file
        try:
            FClist.remove(filepath)
        except ValueError: # file path exists on EOS but not on the file catalogue.             
            addToCounter += 1
            result.write(filepath + '\n')
if addToCounter == 0:
    result.write('None\n')
    print('None')
else:
    result.write('Addto count:' + str(addToCounter) + '\n\n')
    print(str(addToCounter))
result.write('Files missing from the EOS: \n')
print('Number of files missing from the EOS: ', end='')
if FClist: # everything that remains in list is missing on the EOS and, presumably, should be deleted from file catalogue.
    for path in FClist: 
        result.write(path + '\n')
    result.write('Missing count:' + str(len(FClist)) + '\n')
    print(str(len(FClist)))
else:
    result.write('None\n')
    print('None')
print('Sync results in the FCSyncResult.txt \n')
# also need to count list and add all the members of it to SyncResult.txt to Missing chapter. 
result.close()
