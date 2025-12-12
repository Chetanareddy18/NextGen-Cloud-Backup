# Backend/corrupt_simulate.py
import os
import random

def simulate_corruption(file_path: str):
    """Simulate corruption of a backup file (e.g., Azure version)."""
    try:
        if not os.path.exists(file_path):
            print(f"File not found to corrupt: {file_path}")
            return None

        with open(file_path, "rb") as f:
            data = bytearray(f.read())

        if len(data) > 0:
            # Flip one random byte to simulate data corruption
            index = random.randint(0, len(data) - 1)
            data[index] ^= 0xFF  # invert bits

        corrupted_file = f"corrupted_{os.path.basename(file_path)}"
        with open(corrupted_file, "wb") as f:
            f.write(data)

        print(f"[Simulated corruption and saved as {corrupted_file}")
        return corrupted_file

    except Exception as e:
        print(f"Failed to corrupt file: {e}")
        return None
