import os


def create_dummy_file(filename, size_mb):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "wb") as f:
        f.write(os.urandom(size_mb * 1024 * 1024))
    print(f"[+] Created {filename} ({size_mb} MB)")
    return path


if __name__ == "__main__":
    # Tạo 1 file nhỏ và 1 file lớn để test
    create_dummy_file("test_small.mp3", 1)
    create_dummy_file("test_large.mp4", 10)
