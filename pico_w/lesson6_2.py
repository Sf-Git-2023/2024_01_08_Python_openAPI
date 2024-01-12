from machine import Pin
import time

start_ticks = time.ticks_ms()

while True:
    var_ticks = time.ticks_ms()
    if var_ticks - start_ticks > 1000
    led25.value(1)
    time.sleep(1)
    led25.value(0)
    time.sleep(1)