import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

#Create empty data lists
xData = []
typeItOutData = []
plus30SecondsData = []

#Set min and max
minMark = 0
maxMark = 180

#Calculates how many button presses required to enter a time into the microwave
def typeIt(seconds):
    
    #You always hit enter
    ans = 1
    minutes = 0
    while seconds >= 100:     #You can put 99 seconds
        seconds -= 60         #But they only carry by 60
        minutes += 1
    if minutes > 0:
        ans += len(str(minutes)) + 2 #There are always two seconds places after the minutes
    else:
        ans += len(str(seconds))      #Checks if seconds < 10 or not
    return ans


def plus30(seconds):
    ans = int(-(-seconds // 30))       #You just hit +30 until you are over the number, ceiling round without math module
    return ans

#Goes through every number between minMarn and maxMark and fills the data lists
for number in range( max(1,minMark) , maxMark ):
    xData.append(number)
    typeItOutData.append(typeIt(number))
    plus30SecondsData.append(plus30(number))


#Make a pyplot figure
fig, axs = plt.subplots()

#Adds the point where the lines first meet
axs.scatter(61,3)

#Plots the two lines
axs.plot(xData, typeItOutData, label = "Typed out")
axs.plot(xData, plus30SecondsData, label = "+30 seconds")

#Sets titles
plt.suptitle('Microwave "+30 Seconds" button\n'
             'only saves time until 61 seconds', fontsize='large', fontweight='bold')
plt.legend(title = "Entry method")
plt.xlabel("Seconds", fontsize='large', fontweight='bold')
plt.ylabel("Button presses", fontsize='large', fontweight='bold')

#Set the ticks
#Major ticks every 30 seconds
plt.xticks(range(minMark, maxMark+1, 30))
axs.tick_params(axis='x', which='minor', length=2, width=1)
axs.tick_params(axis='x', which='major', length=5, width=1)
#Minor tick between every major tick
axs.xaxis.set_minor_locator(AutoMinorLocator(n=2))

fig.show()
