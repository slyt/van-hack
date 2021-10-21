from pyvit.hw import cantact

dev = cantact.CantactDev("COM3")
dev.set_bitrate(500000)

dev.start()
while True:
      print(dev.recv())