import RPi.GPIO as GPIO
import time
import sys
from timeit import default_timer as timer

PIN_OUT = 3
PIN_INT = 11
T_HIGH = 0.100

t_start = 0
t_max = 0
t_min = 1
t_total = 0
sum_dt = 0

def save_val(dt,flag):
    global t_max,t_min,t_total,sum_dt
    if dt > t_max:
        t_max = dt
    if dt < t_min:
        t_min = dt
    t_total+=dt
    if flag == True:
        sum_dt+=1

def extint_callback(channel):
    dt_flag=False
    if GPIO.input(PIN_INT) == 0:
        end = timer()                
        print('end:',end)
        dt = end - t_start
        print('dt:',dt)
        dt_flag=True
    save_val(dt,dt_flag)    


GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_INT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(PIN_INT, GPIO.FALLING, callback=extint_callback, bouncetime=1)

GPIO.setup(PIN_OUT, GPIO.OUT)
GPIO.output(PIN_OUT, GPIO.LOW)

def pulse():    
    GPIO.output(PIN_OUT, GPIO.HIGH)
    start = timer()
    print('t_high')    
    print('start:',start)
    time.sleep(T_HIGH)
    GPIO.output(PIN_OUT, GPIO.LOW)
    print('t_low')
    return start


# args[0] = numero de pulsos
# args[1] = periodo


if __name__ == "__main__":      
    args = sys.argv[1:]        

    pulse_total = int(args[0])
    period = int(args[1])

    for i in range (pulse_total):
        t_start = pulse()        
        time.sleep(period - T_HIGH)

print('t_max:',t_max)
print('t_min:',t_min)
print('t_medio:',t_total/pulse_total)
print('total_int:',sum_dt)