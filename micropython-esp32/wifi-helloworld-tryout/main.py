from m5stack import lcd

lcd.print('hello world!\n')

import machine, network, utime

lcd.print("")
lcd.print("Starting WiFi ...")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("logic_debug",'ohzei7eexaimo3Ae')
tmo = 50
while not sta_if.isconnected():
    lcd.print('retrying connect \n')
    utime.sleep_ms(1000)
    tmo -= 1
    if tmo == 0:
        sta_if.disconnect()
        break

lcd.print('ip address: ')
lcd.print(sta_if.ifconfig()[0])
lcd.print('\n')

if tmo > 0:
    lcd.print("WiFi started...\n")
    utime.sleep_ms(500)

    rtc = machine.RTC()
    lcd.print("Synchronize time from NTP server ...\n")
    rtc.ntp_sync(server="hr.pool.ntp.org")
    tmo = 100
    while not rtc.synced():
        utime.sleep_ms(100)
        tmo -= 1
        if tmo == 0:
            break

    if tmo > 0:
        lcd.print("Time set\n")
        utime.sleep_ms(500)
        t = rtc.now()
        utime.strftime("%c")
        lcd.print(utime.strftime("%c"))
        lcd.print('\n')
