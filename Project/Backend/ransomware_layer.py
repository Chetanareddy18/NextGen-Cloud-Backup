# Backend/ransomware_layer.py
import math
from collections import Counter

def shannon_entropy(data: bytes) -> float:
    """Calculate Shannon entropy — higher means more randomness (likely encrypted)."""
    if not data:
        return 0.0
    counts = Counter(data)
    length = len(data)
    ent = -sum((count / length) * math.log2(count / length) for count in counts.values())
    return ent

def is_probably_encrypted(file_path: str, entropy_threshold: float = 7.5) -> bool:
    """
    Read a small chunk and decide if the file is likely encrypted/compressed.
    Returns True if entropy >= threshold.
    """
    try:
        with open(file_path, "rb") as f:
            chunk = f.read(4096)
        ent = shannon_entropy(chunk)
        # print for debug/CLI runs
        print(f" Entropy of {file_path}: {ent:.2f}")
        return ent >= entropy_threshold
    except Exception as e:
        print(f" Error scanning {file_path}: {e}")
        return False

def check_ransomware(file_path: str, entropy_threshold: float = 7.5):
    """
    Primary function for the frontend to call.
    Returns a tuple: (entropy_value: float, verdict: "infected"|"clean"|"error")
    """
    try:
        with open(file_path, "rb") as f:
            data = f.read(4096)
        ent = shannon_entropy(data)
        verdict = "infected" if ent >= entropy_threshold else "clean"
        return ent, verdict
    except Exception as e:
        print(f"Error in check_ransomware: {e}")
        return 0.0, "error"

def ransomware_check(file_path: str, entropy_threshold: float = 7.5) -> bool:
    """
    Backwards-compatible wrapper used by some backend scripts:
    Returns True if file is *safe* (NOT ransomware-like), False if blocked.
    """
    ent, verdict = check_ransomware(file_path, entropy_threshold)
    if verdict == "infected":
        print(f"Ransomware-like file detected (entropy={ent:.2f}) — blocked: {file_path}")
        return False
    if verdict == "error":
        print(f" Error while scanning {file_path}; treating as unsafe.")
        return False
    print(f" {file_path} passed ransomware check (entropy={ent:.2f}).")
    return True
