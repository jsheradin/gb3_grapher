#Read .gb3 files from GeekBench 3 Battery benchmark
import glob, sys, matplotlib.pyplot as plt

#Find file to open
files = glob.glob("./*.gb3")
if len(files) == 0:
    print("0 .gb3 files found")
    sys.exit()
elif len(files) == 1:
    print("1 file found, opening \"{}\"".format(files[0]))
    raw_full = open(files[0], "r").read().split("{")
else:
    print("{} files found\n".format(len(files)))
    for n in range(len(files)):
        print("{}: {}".format(n, files[n]))
    raw_full = open(files[int(input("\nEnter file number: "))], "r").read().split("{")

#Dice up to lists
raw_info = raw_full[:25]
raw_battery = raw_full[25:]

battery_entries = []
for entry in raw_battery:
    battery_entries.append(entry.split(","))

battery_level, battery_time = [], []
for n in range(len(battery_entries)):
    a = [battery_entries[n][0].split(" ")]
    battery_level.append(int(a[0][1]))

    a = [battery_entries[n][2].split(" ")]
    battery_time.append(int(a[0][2])/60)

#Make graph
title = input("Graph Title: ")
plt.figure(1)
plt.plot(battery_time, battery_level)
plt.title(title)
axes = plt.gca()
axes.set_ylim([0, 100])
axes.set_xlim([0, battery_time[-1]])
plt.yscale('linear')
plt.ylabel('Battery level (%)')
plt.xscale('linear')
plt.xlabel('Time (minutes)')
plt.grid(True)
plt.savefig(title)
