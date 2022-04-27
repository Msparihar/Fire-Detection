import cv2
import numpy as np
import smtplib
import playsound
import threading

Alarm_Status = False
Email_Status = False
Fire_Reported = 0

def play_alarm_sound_function():
	while True:
		playsound.playsound('AlarmSound.mp3',True)



print("Analysis Type")
print("Enter 1 for Image")
print("Enter 2 for Video")
a = input("Enter a number: ")
a=int(a)
if a==1:
    frame = cv2.imread('C:\\Users\\manis\\Desktop\\Fire-Detection-System-in-python-master\\fire_fire_fighting_brand.jpg') # If you want to use webcam use Index like 0,1.
    while True:
        frame = cv2.resize(frame, (960, 540)) 
        blur = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        lower = [18, 50, 50]
        upper = [35, 255, 255]
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(hsv, lower, upper)
 
        output = cv2.bitwise_and(frame, hsv, mask=mask)
    
        no_red = cv2.countNonZero(mask)
    
        if int(no_red) > 25000:
            Fire_Reported = Fire_Reported + 1
            cv2.imshow("output", output)

        if Fire_Reported >= 1:
    
    	    if Alarm_Status == False:
                threading.Thread(target=play_alarm_sound_function).start()
                Alarm_Status = True
        


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
    cv2.destroyAllWindows()
    frame.release()

if a==2:
    video = cv2.VideoCapture('Fire.mov') # If you want to use webcam use Index like 0,1.
 
    while True:
        (grabbed, frame) = video.read()
        if not grabbed:
          break

        frame = cv2.resize(frame, (960, 540)) 
 
        blur = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
        lower = [18, 50, 50]
        upper = [35, 255, 255]
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(hsv, lower, upper)
 
        output = cv2.bitwise_and(frame, hsv, mask=mask)
    
        no_red = cv2.countNonZero(mask)
    
        if int(no_red) > 25000:
          Fire_Reported = Fire_Reported + 1

        cv2.imshow("output", output)

        if Fire_Reported >= 1:
    
    	    if Alarm_Status == False:
    		    threading.Thread(target=play_alarm_sound_function).start()
    		    Alarm_Status = True

    	    


        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
 
    cv2.destroyAllWindows()
    video.release()

