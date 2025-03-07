import os

def list(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All contents:", os.listdir(path))

def access(path):
    print("Path exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

def info(path):
    if os.path.exists(path):
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path doesn't exist")

def count(path):
    with open(path, 'r') as file:
        print("Number of lines:", sum(1 for line in file))

def write(path, lst):
    with open(path, 'w') as file:
        file.write(" ".join(lst))
    print("Succesfully written")

def generate():
    for char in range(65, 91): 
        with open(f"{chr(char)}.txt", 'w') as file:
            file.write(f"This is a new file")
    print("Succesfully generated")

def f_copy(src, dest):
    with open(src, 'r') as source, open(dest, 'w') as copy:
        copy.write(source.read())
    print(f"Contents copied from {src} to {dest}")

def delete(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("Deleted")
