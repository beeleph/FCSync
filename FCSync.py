import os

# prepare list of files from dirac file catalogue. FClist
FCfile = open('FClist', 'r')
FClist = []
for line in FCfile:
    line = line.strip()
    FClist.append(line)
FCfile.close()
#print(FClist)
#print("list DONE")
for subdir, dirs, files in os.walk("TestFolda"):
    for file in files:
        print("/" + os.path.join(subdir, file))
        #filepath = subdir + os.sep + file
        #print(filepath)
        if (FClist.remove("/" + os.path.join(subdir, file))):
            # file path exists on EOS but not on the file catalogue. 
            # add counter of addTo files, add this file path to SyncResult.txt to addTo chapter. 
# everything that remains in list is missing on the EOS and, presumably, should be deleted from file catalogue. 
# also need to count list and add all the members of it to SyncResult.txt to Missing chapter. 
