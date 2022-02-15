import os
import time

# watchDirectory is the directory we're pulling information from
watchDirectory = "C:\\Users\Joebf\Desktop\Auto-Backup\Auto-backup\Test1"
# backupDirectory is where we're putting the information
backupDirectory = "C:\\Users\Joebf\Desktop\Auto-Backup\Auto-backup\Test2"
# deletedDirectory is where we put files that were backed up but later deleted
deletedDirectory = "C:\\Users\Joebf\Desktop\Auto-Backup\Auto-backup\Test3"

# Gathering the information that we need from both of the directories
while(1 == 1):
    wfiles = os.listdir(watchDirectory)
    wfileStats = []
    for f in wfiles:
        wfileStats.append(os.stat(watchDirectory + "\\" + f))

    bfiles = os.listdir(backupDirectory)
    bfileStats = []
    for f in bfiles:
        bfileStats.append(os.stat(backupDirectory + "\\" + f))



    #### Bubble sorting algorithm

    ## Order watch directory in terms of creation time
    n = len(wfiles)
    inOrder = 0
    changes = 0
    counter = 0
    while(inOrder == 0):
        while(counter < n - 1):
            if(wfileStats[counter].st_ctime > wfileStats[counter + 1].st_ctime):
                temp = wfileStats[counter + 1]
                temp2 = wfiles[counter + 1]
                wfileStats[counter + 1] = wfileStats[counter]
                wfiles[counter + 1] = wfiles[counter]
                wfileStats[counter] = temp
                wfiles[counter] = temp2
                changes = changes + 1
            counter = counter + 1
            if(changes == 0):
                inOrder = 1
            changes = 0

    ## Order backup directory in terms of creation time
    n = len(bfiles)
    if(n > 0):
        inOrder = 0
        changes = 0
        counter = 0
        while(inOrder == 0):
            while(counter < n - 1):
                if(bfileStats[counter].st_ctime > bfileStats[counter + 1].st_ctime):
                    temp = bfileStats[counter + 1]
                    temp2 = bfiles[counter + 1]
                    bfileStats[counter + 1] = bfileStats[counter]
                    bfiles[counter + 1] = bfiles[counter]
                    bfileStats[counter] = temp
                    bfiles[counter] = temp2
                    changes = changes + 1
                counter = counter + 1
                if(changes == 0):
                    inOrder = 1
                changes = 0

    # Compare backup directory inventory to watch directory inventory and delete anything there that doesn't match
    for f in bfiles:
        found = 0
        for j in wfiles:
            if(f == j):
                found = 1
                break
        if(found == 0):
            os.system("robocopy \"" + backupDirectory + "\" \"" + deletedDirectory + "\" \"" + f + "\" /MOV /DCOPY:T")
            os.system("robocopy \"" + backupDirectory + "\\" + f + "\" \"" + deletedDirectory + "\" /DCOPY:T")

    
    os.system("robocopy \"" + watchDirectory + "\" \"" + backupDirectory + "\" /MIR")
    print("END")
    #runs every 30 minutes
    time.sleep(1800)
