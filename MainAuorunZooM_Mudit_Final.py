import datetime
import webbrowser
import smtplib
email = 'dontreplymudit@gmail.com'
send_to_email = input("Enter Your GMail Id Here  ")
messagea = 'Your Zoom metting Will Start Shortly'
messageb = 'Your Zoom metting has started And Its Currently running'
print("Enter the Zoom Link:")
url = input("-->  ") 
print("  ")
timenow = datetime.datetime.now()
Actual_Time = timenow.strftime('%H:%M')
print("  **USE 24 HOUR CLOCK FORMAT**  ")
hour = input("Enter the Hour Time in HH format  ")
password = '@_mudit@_vasu'
minutes = input("Enter the Minute Time in MM format  ")
beforetime = input("How Many Minutes Before Do You Want To recive The first Mail  ")
minutesint = int(minutes)
hourint = int(hour)
beforetimeint = int(beforetime)
minutesfinal = minutesint - beforetimeint
if (minutesfinal < 0):
       munutesfinal = minutesint + 60
       hourint = hourint - 1
minutesfinal = str(minutesfinal)
hourstr = str(hourint)
hourstr = hourstr.zfill(2)
minutesfinal = minutesfinal.zfill(2)
finaltime = hourstr + ":" + minutesfinal
hour = hour.zfill(2)
minutes = minutes.zfill(2)
Set_Alarm = hour + ":" + minutes
print("Started")
print("")
print("First Mail Time  " + finaltime)
print("Meeting Starting Time  " + Set_Alarm)
while (Actual_Time != Set_Alarm):
    timenow = datetime.datetime.now()
    Actual_Time = timenow.strftime('%H:%M')
    currenttime = timenow.strftime('%H:%M:%S')
    print("Current TimE:- " + Actual_Time)
    if (Actual_Time == finaltime):
           server = smtplib.SMTP('smtp.gmail.com', 587)
           server.starttls() 
           server.login(email, password) 
           server.sendmail(email, send_to_email , messagea)
           finaltime = 3
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" 
w = webbrowser.get(chrome)
if (Actual_Time == Set_Alarm):
    print ("You should see your webpage now :-")
    w.open(url)
    server.sendmail(email, send_to_email , messageb)
    print("Second Mail Sent")

server.quit()
