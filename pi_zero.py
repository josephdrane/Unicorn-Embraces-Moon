#!/usr/bin/env python3

from gpiozero import OutputDevice as Power


class PiZero:
    def __init__(self) -> None:
        self.switch: Power = Power("BOARD5")

    def power_off(self) -> None:
        self.switch.off()

    def power_on(self) -> None:
        self.switch.on()
