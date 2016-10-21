numberList = []                                         #Creating the user's input list
print "(Note: pressing enter will print the results of the list)" #Tells the user presses "Enter"(Or non-number) breaks loop / prints.
numberLoop = '_'                                        #Creating the loop
while numberLoop !='':
    numberInput = raw_input("Please enter a number:")   #User interaction with raw_input
    
    if numberInput == '':
        break                                           #Break the loop if a number is not entered
    else:
        numberInput = float(numberInput)                #Insuring that all the numbers are a float for the average
        numberList.append(numberInput)                  #Adds the last item entered to the end of the list
    print numberList

#Ends of the users interaction

smallest = 0                                            #smallest number assigned
largest = 0                                             #largest number assigned

for number in numberList:
    if smallest == 0 or smallest > number:              #Comparing numbers down the list
        smallest = number
    if largest == 0 or largest < number:                #Comparing which is largest
        largest = number
#Print the user results of largest/smallest
print "The largest number is...", largest               
print "The smallest number is...", smallest

listSum = 0                                             #Adding all the numbers in numberList to create the sum
for number in numberList:
    listSum = listSum + number
print "The sum of your list is...", listSum

average = listSum/len(numberList)                       #Finds the average of list "/"(divide) len is to divide listSum by length
print "The average is...", average


#End of all interactions and program
