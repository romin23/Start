import time
import webbrowser

def countdown(equal_interval):                                                  # function for countdown timer
    while equal_interval > 0:                                                  # runs the code till time goes 0
        min ,sec =divmod(equal_interval,60)                                     # converts seconds into into min  hours
        hrs , min = divmod(min , 60)                                            # converts seconds into into min  hours
        t_left ='Time left for break ' + str(hrs)+":"+str(min)+":"+str(sec)
        print(t_left,"\r", end = "")                                            # displays countdown for next break
        time.sleep(1)                                                           # pauses code execution for 1 sec 
        equal_interval -= 1                                                     # reduces value of variable by 1

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
    print('Breaks left', m-i, '0f', m)                                         # shows number of break left

    countdown(equal_interval)                                                # calls the function to do countdown for next break
    
    webbrowser.open_new_tab("https://www.rgmechanics-games.com/")            # opens the link when break should accour
    input("\n Press 'Enter' to start next session")                           # waits/pause the execution for user to comeback from break & resume the execution manually
print('End of work time!!')    



#============================================================================output==============================================================================================
''' 
Enter the no of Hours: 0.0625                                           #(3.75 min)
No. of Breaks: 3
Total no. of Seconds:  225
No. of Breaks:  3
Break in every  75  Seconds
Breaks left 3 0f 3
Time left for break 0:0:1
 Press 'Enter' to start next session
Breaks left 2 0f 3
Time left for break 0:0:1
 Press 'Enter' to start next session
Breaks left 1 0f 3
Time left for break 0:0:1
 Press 'Enter' to start next session 
 End of work time!!   
'''
