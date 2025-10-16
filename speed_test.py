#!/usr/bin/env python3

import speedtest

def run_speed_test():
    """Run internet speed test and display results."""
    st = speedtest.Speedtest()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    print("Getting ping...")
    st.get_servers()
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

    return download_speed, upload_speed, ping

if __name__ == "__main__":
    run_speed_test()
