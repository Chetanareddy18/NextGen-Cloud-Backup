import hashlib

def calculate_checksum(file_path: str):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_integrity(original_file: str, restored_file: str):
    orig = calculate_checksum(original_file)
    restored = calculate_checksum(restored_file)
    if orig == restored:
        print("Integrity verified — both files are identical.")
        return True
    else:
        print("Integrity check failed — files differ!")
        return False
