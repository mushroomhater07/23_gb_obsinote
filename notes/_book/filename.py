import os

def add_filename(directory):
  for filename in os.listdir(directory):
    if filename.endswith(".md"):
      with open(os.path.join(directory, filename), "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.write("# " + os.path.splitext(filename)[0] + "\n" + content)

if __name__ == "__main__":
  directory = "./"
  add_filename(directory)