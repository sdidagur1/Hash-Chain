import hashlib

def hash_data(data):
    """Hash data using SHA-256"""
    return hashlib.sha1(data).hexdigest()

def hash_file(filepath):
    with open(filepath, "rb") as f:
        file_data = f.read()
    return hash_data(file_data)

def merkle_tree(hashes):
    """Build a Merkle tree return the root hash."""
    if not hashes:
        return None

    if len(hashes) == 1:
        return hashes[0]

    if len(hashes) % 2 != 0:
        hashes.append(hashes[-1])

    next_level = []
    for i in range(0, len(hashes), 2):
        combined = (hashes[i] + hashes[i + 1]).encode("utf-8")
        combined_hash = hash_data(combined)
        next_level.append(combined_hash)

    return merkle_tree(next_level)

if __name__ == "__main__":
    file_paths = input("Enter file names separated by spaces: ").split()

    leaf_hashes = []
    for path in file_paths:
        h = hash_file(path)
        leaf_hashes.append(h)
        print(f"{path}: {h}")
       
    root_hash = merkle_tree(leaf_hashes)
    print("\nTop Hash:", root_hash)
