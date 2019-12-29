import sys

a=sys.argv[1]
fname = open('/sys/class/backlight/intel_backlight/brightness','r+')
brightness_val = int(fname.read())

if(a=='-u'):
    new_val = brightness_val+6000
    if(new_val>120000):
        new_val = 120000

if(a=='-d'):
    new_val = brightness_val-6000
    if(new_val<1200):
        new_val = 1200

fname.write(str(new_val))
fname.close()

