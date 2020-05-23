import time
import webbrowser

hours = input('Enter the no of Hours: ')                                       # Gets no of hours
no_of_breaks = input("No. of Breaks: ")                                        # Gets no of Breaks

try:
    seconds = float(hours)                                                    # It can take no of hours in float as well to calculate exact no of seconds
    int_secs = int(seconds * 60 *60)                                          # Calculate no of seconds in given hours
    print("Total no. of Seconds: ",int_secs)
    m = int(no_of_breaks)                                                     # Converts no of break into int
    print("No. of Breaks: ",m)
    equal_interval = (int_secs//m)                                            # calculates exact no of secs. afer which a break should be scheduled
    print("Break in every ",equal_interval, " Seconds")                       # Displays exact interval between every break

except:
    print('Invalid entry')                                                    
    

for i in range(m):                                                           # for loop for no of breaks

    for j in range (equal_interval):                                                            # for loop for no of secs. afer which a break should be scheduled
        brk_time =  "Time remaining until break is " + str(equal_interval-j) + " Seconds..."
        print( brk_time + "\r", end="" )                                                        # displays no of secs remaining for next break 
        time.sleep(1)                                                                           # stops code for 1 sec
    webbrowser.open_new_tab("https://www.rgmechanics-games.com/")                                              # opens the link when break should accour
    input("\n Press 'Enter' to start next session")                           # waits/pause the execution for user to comeback from break & resume the execution manually
