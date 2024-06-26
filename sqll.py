import sqlite3
from datetime import datetime

def update_database(devices):
    # Connect to the database
    conn = sqlite3.connect('devices.db')
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS devices
                 (ip TEXT, mac TEXT, first_seen TEXT, last_seen TEXT)''')

    # Update database with new devices
    for device in devices:
        ip = device['ip']
        mac = device['mac']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            c.execute("INSERT INTO devices (ip, mac, first_seen, last_seen) VALUES (?, ?, ?, ?)", (ip, mac, timestamp, timestamp))
        except sqlite3.Error as e:
            print("SQLite error:", e)
            print("Failed to insert data for device:", device)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    devices = [{'ip': '192.168.1.1', 'mac': '00:11:22:33:44:55'}, {'ip': '192.168.1.2', 'mac': '66:77:88:99:AA:BB'}]
    update_database(devices)
