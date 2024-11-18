import subprocess
import time
from datetime import datetime, timedelta

# รับเวลาปัจจุบัน
currentTime = datetime.now()
print(currentTime.strftime("%H:%M:%S"))

# กำหนดเวลาเริ่มต้น
startTime = datetime.combine(currentTime.date(), datetime.strptime("15:27:00", "%H:%M:%S").time())

# ถ้าเวลาปัจจุบันเกินเวลาเริ่มต้น ให้เลื่อนเวลาเริ่มต้นเป็นวันถัดไป
if startTime.time() < currentTime.time():
    startTime += timedelta(days=1)

# คำนวณเวลาที่เหลือ
timeDifference = (startTime - currentTime).total_seconds()
print(timeDifference)

# หากยังมีเวลาที่เหลือ
if timeDifference > 0:
    # เริ่มคำสั่ง tcpdump เพื่อจับแพ็กเก็ต
    tcpdumpCommand = ["sudo", "tcpdump", "-w", "captureSta4.pcap"]
    tcpdumpProcess = subprocess.Popen(tcpdumpCommand)

    # รอจนถึงเวลาที่กำหนด
    print(f"Time left {int(timeDifference)} seconds")
    time.sleep(timeDifference)

    # เรียกคำสั่ง hping3 เพื่อส่ง TCP SYN packets
    hpingCommand = ["hping3", "-S", "-v", "-k", "-d", "300k", "-p", "80", "--faster", "10.0.0.2"]
    subprocess.run(hpingCommand)
else:
    print("No time left")
