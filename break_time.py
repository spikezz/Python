import time
import webbrowser

count=0
t=0

while (count<3):
    print("Start work now!It's "+time.ctime() )
    while(t<11):
        
        time.sleep(1)
        print('work time last',10-t,'second')
        t=t+1
        
    count=count+1
    t=0
    print(count,'st Break start')
    webbrowser.open("https://www.youtube.com/watch?v=iIrmhf9pRH0")
    
    while(t<11):
        
        time.sleep(1)
        print('rest time last',10-t,'second')
        t=t+1
    t=0
