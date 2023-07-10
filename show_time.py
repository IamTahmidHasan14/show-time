import time

hr = int(time.strftime("%H"))
hr = (hr + 6) % 24
print("Time:", hr, end="")
ms = time.strftime(":%M:%S")
print(ms)
hr2 = hr % 12
if (hr >= 12):
  if (hr2 == 0):
    hr2 = 12
  print(hr2, "pm")
else:
  if (hr2 == 0):
    hr2 = 12
  print(hr2, "am")
