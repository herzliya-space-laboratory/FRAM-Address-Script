import pandas as pd
data = pd.read_csv("FRAM_Addresses.csv")

f = open("output.txt", "w")

addresses = []
sizes = []

for i in range(int(data["define address name"].count())):
    if pd.notna(data["define address name"][i]) and pd.notna(data["Start Addr.[hex]"][i]) and pd.notna(data["Size [bytes]"][i]):
        if len(str(data["Start Addr.[hex]"][i])) == 1:
            f.write("#define " + str(data["define address name"][i]) +
                    "_FRAM_ADDR     " + "0x0" + str(data["Start Addr.[hex]"][i]) + ";" + "\n")
        else:
            f.write("#define " + str(data["define address name"][i]) +
                    "_FRAM_ADDR     " + "0x" + str(data["Start Addr.[hex]"][i]) + ";" + "\n")
        addresses.append(int(str(data["Start Addr.[hex]"][i]), 16))
        f.write("#define " + str(data["define address name"][i]) +
                "_DELAY_FRAM_SIZE     " + str(int(data["Size [bytes]"][i])) + ";" + "\n")
        sizes.append(int(data["Size [bytes]"][i]))
        f.write("\n")
f.close()

locations = []
count = 0
for i in range(len(addresses) - 1):
    for j in range(addresses[i], addresses[i] + sizes[i]):
        for c in locations:
            if j == c:
                print("OVERLAPING: " +
                      str(data["define address name"][count]))
        locations.append(j)
    count += 1
