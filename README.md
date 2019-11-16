# raspi-fancontrol
I wrote this code for my Raspberry Pi 4 because it came with a fan, but I don't like it running all the time because it's annoying.

The Raspberry Pi puts out only 3.5 volts dc and the fan requires 5 volts dc. Therefore you will need a to soldier some things together
to make it work.

You'll need:
1. 1 NPN 2N2222 Transitor
2. 1 x 1k Ohm Resistor
3. 1 x 1N4004 Diode (optional protection)

1. Wire 5vdc power directly to fan red wire.
2. Wire the negative from the fan to the collector side of a transistor.
3. Wire the control leg of the transistor to the GPiO Pin of your choice with a 1k Ohm resistor between the GPiO Pin and the control leg (center pin)
4. Wire the emitter of the transistor to ground.
5. Optionally you may want a diode between the postive and negative wires on the fan.
      a. splice grey stripe side into the negative wire between the fan and ground on the ground wire.
      b. splice the other side to the positive side of the fan where it wires into the NPN Transitor.

All of those should be soldiered together properly.

You can test with the raspi-fancontrol.py script to figure out the correct pin assignments. Then use that info to setup the raspi-fancontrol-daemon.py and run it at startup. It will deamonize and run every minute by default. You can change the time delay.

It also keeps track of the temperature history of your py in /root/temphistory.txt.

This scripts must be run as root because RPIO lib requires it.


