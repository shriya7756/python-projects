from speedtest import Speedtest 

wifi = speedtest.Speedtest()
download_speed = wifi.download()  # Measure download speed
upload_speed = wifi.upload()      # Measure upload speed
print(f"Download speed: {download_speed / 1_000_000:.2f} Mbps")
print(f"Upload speed: {upload_speed / 1_000_000:.2f} Mbps")
