# WheeCairV2_data

This repository is a subset or continuation in a different direction to https://github.com/dr-fischer/wheeCAIR. Basically same concept except the microcontroller (Teensy 4.1) have a ESP32 WIFI module that allows it to upload its data to github which then can be processes by other programming languages in real time. (Ex. for this repo it is Julia).

Why don't I just use Ardunio IOT? Well because as much as that service is interesting it also comes at the cost of the data not being as open source, making it difficult for others to interpret the data with whatever method they choose (plus it a service).

## The Plan
- [x] Cry
- [x] Access the interwebs with a Teensy 4.1 connected to a ESP32 module
- [x] Access GitHub with CircuitPython requests.py
- [x] Read and Write CSV files to SD storage on Teensy 4.1
- [x] Upload CSV file to GitHub 
- [ ] Connect BME280 sensor and have its data appended to a CSV that uploads to Github Repo every x minutes
- [ ] Connect Plantower PM sensor and have its data appended to a CSV that uploads to Github Repo every x minutes
- [ ] Cry
- [ ] Build a website for Julia to work with.
- [ ] Run Julia on a Virtual Private Server and builds said website
- [ ] Write some funny program that allows Julia to get the data CSV and plot it in realtime using Makie.jl
- [ ] Cry
- [ ] Create a PCB to connect everything together in a small formfactor
- [ ] Build a weather proof housing for the electronics
- [ ] (Optional) Build a WIFI Manager Access Point for ease of use accessing WIFI in different locations
