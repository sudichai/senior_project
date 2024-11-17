import subprocess
import time
from datetime import datetime, timedelta

# รับเวลาปัจจุบัน
currentTime = datetime.now()
print(currentTime.strftime("%H:%M:%S"))
startTime = datetime.combine(currentTime.date(), datetime.strptime("18:35:00", "%H:%M:%S").time())

# ถ้าถึงเวลาเริ่มแล้ว เลื่อนไปอีกวัน
if startTime.time() < currentTime.time():
    startTime += timedelta(days=1)

# คำนวณเวลาต่าง
timeDifference = (startTime - currentTime).total_seconds()
print(timeDifference)

# ถ้ามีเวลาที่เหลือ
if timeDifference > 0:
    # รัน tcpdump
    tcpdumpCommand = ["sudo", "tcpdump", "-w", "captureSta4.pcap"]
    tcpdumpProcess = subprocess.Popen(tcpdumpCommand)

    # รอจนถึงเวลาที่ตั้งไว้
    print(f"Time left {int(timeDifference)} seconds")
    time.sleep(timeDifference)

    # รัน hping3
    hpingCommand = ["hping3", "-1", "-V", "-d", "300k", "-p", "80", "--faster", "10.0.0.2"]
    subprocess.run(hpingCommand)
else:
    print("No time left")
