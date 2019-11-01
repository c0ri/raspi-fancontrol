# raspi-fancontrol
I wrote this code for my Raspberry Pi 4 because it came with a fan, but I don't like it running all the time because it's annoying.

The Fans typically can wire directly to pin 4 (power) and pin 6 (ground). 
Just wire the power wire to GPIO4 on Pin 7 and leave the ground on pin 6.

Then run this code in a cron job once a min.

Someone may wanna daemonize it so it just runs real-time. I may add that later.

