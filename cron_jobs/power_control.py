from gpiozero import OutputDevice as Power

light = Power('BOARD5')

light.on()

sleep(2)

light.off()