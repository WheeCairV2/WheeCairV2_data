import board
import busio
import adafruit_binascii
import circuitpython_csv as csv
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from secrets import secrets
import circuitpython_base64 as base64
import json
import adafruit_sdcard
import storage
import bitbangio
import os
import io

spi = bitbangio.SPI(board.CLK, board.CMD, board.DAT0)
cs = DigitalInOut(board.DAT3)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

with open("/sd/testwrite.csv", mode="w", encoding="utf-8") as writablefile:
    csvwriter = csv.writer(writablefile)
    csvwriter.writerow(["I", "love", "CircuitPython", "!"])
    csvwriter.writerow(["Spam"] * 3)

print("ESP32 Initialize")

esp32_cs = DigitalInOut(board.D5)
esp32_ready = DigitalInOut(board.D9)
esp32_reset = DigitalInOut(board.D6)
esp32_gpio0 = DigitalInOut(board.D10)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

esp = adafruit_esp32spi.ESP_SPIcontrol(
    spi, esp32_cs, esp32_ready, esp32_reset, esp32_gpio0
)

print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except OSError as e:
        print("could not connect to AP, retrying: ", e)
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)
print("My IP address is", esp.pretty_ip(esp.ip_address))

# Initialize a requests object with a socket and esp32spi interface
requests.set_socket(socket, esp)

oauth_token = secrets["github_token"]

with open("/sd/testwrite.csv", "rb", encoding="utf-8") as file:
    data = file.read()

# Create a new file
base_url = "https://api.github.com/repos/WheeCairV2/WheeCairV2_data/contents/Test3.csv"
encoded = base64.encodebytes(bytes((data),"utf-8"))#base64.encodebytes((bytes(data, "utf-8")))
data = {
    "message": str("Creating a new CSV file", "utf-8"),
    "content": str(encoded, "utf-8")
    ,  # base64_string.decode('utf-8')
}
response = requests.put(
    base_url,
    data=json.dumps(data),
    headers={"Authorization": "token {}".format(oauth_token)},
)

print(response.status_code)
print(response.json())
io.BytesIO(data, "utf-8")
