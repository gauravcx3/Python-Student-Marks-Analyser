# CITS1401 Computational Thinking with Python - Project1 submission
# Project1Gaurav.py - A python program to read a csv file(marksheet of students) and output various stats.
# Author - Gaurav Chakraverty, Student ID - 22750993


# main function that takes in the name of a csv file
def main(csvfile):
    # open the file and set as read
    openfile = open(csvfile, 'r')
    # store all lines in the file as a list
    readlines = openfile.readlines()
    openfile.close()
    errval = filevalidator(readlines)
    mn = round4dec(minimum(readlines))
    mx = round4dec(maximum(readlines))
    avg = round4dec(average(readlines))
    std = round4dec(stdev(readlines))
    cor = round4dec(corel(readlines))
    # if there 2 students have same score and name
    if errval == False:
        print ("error - two students have same score and name!!")
        return (None,None,None,None,None)
    # else if file has no error
    return mn, mx, avg, std, cor


# function to convert a list of strings to numbers
def str2num(strlist):
    numlist = []
    for stritem in strlist:
        numitem = float(stritem)
        numlist.append(numitem)
    # return the converted list
    return numlist


# function to convert a list of sums to a list of averages
def sum2avg(sumlist, readlines):
    avglist = []
    for sumitem in sumlist:
        avgitem = sumitem/(len(readlines)-1)
        avglist.append(avgitem)
    # return the converted list
    return avglist


# function to convert a list of items to a list of zeros
def str2zero(strlist):
    zerolist = []
    for stritem in strlist:
        zerolist.append(0)
    return zerolist


# function to find sqrt of a list of numbers
def sqrtlist(numlist):
    sqrtlst = []
    for numitem in numlist:
        sqrtitem = float(numitem) ** 0.5
        sqrtlst.append(sqrtitem)
    # return the converted list
    return sqrtlst


# function to calculate the corellation between two ranked lists
def corcalc(rankedcolumn, rankedtotal):
    d2sum = 0
    for column in range(0, len(rankedcolumn)):
        d = rankedcolumn[column] - rankedtotal[column]
        d2 = d**2
        d2sum = d2sum + d2
    n = len(rankedcolumn)
    calcoutput = 1 - ((6*d2sum)/((n**3)-n))
    return calcoutput


# function to round a list to 4 decimal places
def round4dec(numlist):
    roundlist = []
    for numitem in numlist:
        numitem = round(float(numitem), 4)
        roundlist.append(numitem)
    # return the rounded list
    return roundlist


def minimum(readlines):
    # split and store the 2nd line of the list
    tempoutput = readlines[1].split(',')
    # skip the first 2 non-number columns
    minoutput = tempoutput[2:]
    # split and store the initial line
    currentline = readlines[1].split(',')
    temptotal = 0
    linetotal = 0
    # need the score of the first student to compare rest
    for column in range(2, len(currentline)):
        # find total score of first student in list
        temptotal = temptotal + float(currentline[column])
    # go through each row (skip first one)
    for row in range(1, len(readlines)):
        # split each line
        currentline = readlines[row].split(',')
        # go through each column (skip first two)
        for column in range(2, len(currentline)):
            linetotal = linetotal + float(currentline[column])
            # since minoutput has 2 items less
            if float(currentline[column]) < float(minoutput[column-2]):
                # store current column value in minoutput
                minoutput[column-2] = currentline[column]
        if linetotal < temptotal:
            temptotal = linetotal
        mintotal = temptotal
        linetotal = 0
    minoutput = str2num(minoutput)
    minoutput.append(mintotal)
    return minoutput


def maximum(readlines):
    # split and store the 2nd line of the list
    tempoutput = readlines[1].split(',')
    # skip the first 2 non-number columns
    maxoutput = tempoutput[2:]
    # split and store the initial line
    currentline = readlines[1].split(',')
    temptotal = 0
    linetotal = 0
    # need the score of the first student to compare rest
    for column in range(2, len(currentline)):
        # find total score of first student in list
        temptotal = temptotal + float(currentline[column])
    # go through each row (skip first one)
    for row in range(1, len(readlines)):
        # split each line
        currentline = readlines[row].split(',')
        # go through each column (skip first two)
        for column in range(2, len(currentline)):
            linetotal = linetotal + float(currentline[column])
            # since maxoutput has 2 items less
            if float(currentline[column]) > float(maxoutput[column-2]):
                # store current column value in maxoutput
                maxoutput[column-2] = currentline[column]
        if linetotal > temptotal:
            temptotal = linetotal
        maxtotal = temptotal
        linetotal = 0
    maxoutput = str2num(maxoutput)
    maxoutput.append(maxtotal)
    return maxoutput


def average(readlines):
    # split and store the 2nd line of the list
    tempoutput = readlines[1].split(',')
    # skip the first 2 non-number columns and convert items to zero
    sumoutput = str2zero(tempoutput[2:])
    temptotal = 0
    linetotal = 0
    # go through each row (skip first one)
    for row in range(1, len(readlines)):
        # split each line
        currentline = readlines[row].split(',')
        # go through each column (skip first two)
        for column in range(2, len(currentline)):
            # add and store current column value to sumoutput
            sumoutput[column-2] = float(currentline[column]) + float(sumoutput[column-2])
            # keep adding current column value to linetotal
            linetotal = linetotal + float(currentline[column])
        # keep adding linetotal to temptotal
        temptotal = linetotal + temptotal
        sumtotal = temptotal
        linetotal = 0
    # find the average. Need ignore the first row.
    avgtotal = sumtotal / (len(readlines) - 1)
    sumoutput = str2num(sumoutput)
    avgoutput = sum2avg(sumoutput, readlines)
    avgoutput.append(avgtotal)
    return avgoutput


# Work out the Mean (the simple average of the numbers) ->avglist, avgtotal
# Then for each number: subtract the Mean and square the result.
# Then work out the mean of those squared differences.
# Take the square root of that and return values. ->sqrtlist(numlist)
def stdev(readlines):
    avglist = average(readlines)
    # store the average of the total seperately
    avgtotal = float(avglist[(len(avglist)-1):][0])

    # split and store the 2nd line of the list
    tempoutput = readlines[1].split(',')
    # skip the first 2 non-number columns and convert items to zero
    sumoutput = str2zero(tempoutput[2:])
    temptotal = 0
    linetotal = 0
    # go through each row (skip first one)
    for row in range(1, len(readlines)):
        # split each line
        currentline = readlines[row].split(',')
        # go through each column (skip first two)
        for column in range(2, len(currentline)):
            a = float(currentline[column])
            b = float(sumoutput[column-2])
            c = float(avglist[column-2])
            # subtract avgmean and square each column value then add to sumoutput
            sumoutput[column-2] = ((a - c)**2) + b
            # keep adding current column value to linetotal
            linetotal = linetotal + float(currentline[column])
        # subtract avgtotal and square each value then add to temptotal
        temptotal = ((linetotal - avgtotal)**2) + temptotal
        sumtotal = temptotal
        linetotal = 0
    # find the average. Need ignore the first row.
    avgtotal = sumtotal / (len(readlines) - 1)
    sumoutput = str2num(sumoutput)
    avgoutput = sum2avg(sumoutput, readlines)
    avgoutput.append(avgtotal)
    sqrtoutput = sqrtlist(avgoutput)
    return sqrtoutput


def corel(readlines):
    coroutput = []
    linetotal = 0
    # list containing total of each subject
    storetotal = []
    # list containing the name of students
    namecolumn = []
    # list containing grades of a column/subject
    storecolumn = []
    # go through each row (skip first one) ->loop for finding list of totals
    for row in range(1, len(readlines)):
        # split each line
        currentline = readlines[row].split(',')
        # go through each column (skip first two)
        for column in range(2, len(currentline)):
            # keep adding current column value to linetotal
            linetotal = linetotal + float(currentline[column])
        # store each linetotal inside storetotal
        storetotal.append(linetotal)
        linetotal = 0
    # loop to store list of student names
    for column in range(0, 1):
        for row in range(1, len(readlines)):
            currentline = readlines[row].split(',')
            namecolumn.append(currentline[column])
    # loop to store list of subject scores
    for column in range(2, len(currentline)):
        for row in range(1, len(readlines)):
            currentline = readlines[row].split(',')
            storecolumn.append(float(currentline[column]))
        # rank the subject scores in each column
        rankedcolumn = ranksorter(namecolumn, storecolumn)
        # rank the total column
        rankedtotal = ranksorter(namecolumn, storetotal)
        # calculate corellation between ranked subject and total
        corcolumn = corcalc(rankedcolumn, rankedtotal)
        coroutput.append(corcolumn)
        storecolumn = []
    # calculate corellation between total and total and append at end
    coroutput.append(corcalc(rankedtotal, rankedtotal))
    return coroutput


# function to sort subjectmarks or totalmarks by rank
def ranksorter(namecolumn, valuecolumn):
    # serial corrosponds to valuecolumn
    serialcolumn = []
    # list of sorted numbers the size of valuecolumn
    rankedcolumn = []
    for column in range(1, len(namecolumn)+1):
        # serial corrosponds to valuecolumn
        serialcolumn.append(column)
        # list of sorted numbers the size of valuecolumn
        rankedcolumn.append(column)
    for i in range(len(valuecolumn)):
        for j in range(i + 1, len(valuecolumn)):
            # checks the numbers
            if valuecolumn[i] < valuecolumn[j]:
                temp1, temp2, temp3 = valuecolumn[j], namecolumn[j], serialcolumn[j]
                valuecolumn[j], namecolumn[j], serialcolumn[j] = valuecolumn[i], namecolumn[i], serialcolumn[i]
                valuecolumn[i], namecolumn[i], serialcolumn[i] = temp1, temp2, temp3
            # checks the names
            if valuecolumn[i] == valuecolumn[j]:
                if namecolumn[i] > namecolumn[j]:
                    temp1, temp2, temp3 = namecolumn[j], valuecolumn[j], serialcolumn[j]
                    namecolumn[j], valuecolumn[j], serialcolumn[j] = namecolumn[i], valuecolumn[i], serialcolumn[i]
                    namecolumn[i], valuecolumn[i], serialcolumn[i] = temp1, temp2, temp3
    # now revert the previous sort and arrange by original serial again
    for i in range(len(serialcolumn)):
        for j in range(i + 1, len(serialcolumn)):
            # checks the numbers
            if serialcolumn[i] > serialcolumn[j]:
                temp1, temp2, temp3, temp4 = serialcolumn[j], rankedcolumn[j], namecolumn[j], valuecolumn[j]
                serialcolumn[j], rankedcolumn[j], namecolumn[j], valuecolumn[j] = serialcolumn[i], rankedcolumn[i], namecolumn[i], valuecolumn[i]
                serialcolumn[i], rankedcolumn[i], namecolumn[i], valuecolumn[i] = temp1, temp2, temp3, temp4
    return rankedcolumn


# function to check if file has same name and score
def filevalidator(readlines):
    linetotal = 0
    # list containing total of each subject
    storetotal = []
    # list containing the name of students
    namecolumn = []
    # list containing grades of a column/subject
    storecolumn = []
    # go through each row (skip first one) ->loop for finding list of totals
    for row in range(1, len(readlines)):
        # split each line
        currentline = readlines[row].split(',')
        # go through each column (skip first two)
        for column in range(2, len(currentline)):
            # keep adding current column value to linetotal
            linetotal = linetotal + float(currentline[column])
        # store each linetotal inside storetotal
        storetotal.append(linetotal)
        linetotal = 0
    # loop to store list of student names
    for column in range(0, 1):
        for row in range(1, len(readlines)):
            currentline = readlines[row].split(',')
            namecolumn.append(currentline[column])
    # loop to store list of subject scores
    for column in range(2, len(currentline)):
        for row in range(1, len(readlines)):
            currentline = readlines[row].split(',')
            storecolumn.append(float(currentline[column]))
        # validate the subject scores in each column
        validatecolumn = rankvalidator(namecolumn, storecolumn)
        # validate the total column
        validatetotal = rankvalidator(namecolumn, storetotal)
        # calculate corellation between ranked subject and total
        storecolumn = []
        # validate subjects and total
        if ((validatecolumn == False) or (validatetotal == False)):
            return False
    return True


# function to check if file has same name and score
def rankvalidator(namecolumn, valuecolumn):
    for i in range(len(valuecolumn)):
        for j in range(i + 1, len(valuecolumn)):
            if valuecolumn[i] == valuecolumn[j]:
                if namecolumn[i] == namecolumn[j]:
                    #validator = False
                    return False
    return True

