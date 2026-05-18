with open("output.txt", "w") as f:
    f.write("Hello from Python\n")
    f.write("Second line\n")

print("File written")

with open("output.txt", "r") as f:
    content = f.read()

print(content)

import json

config = {
    "model": "claude-sonnet-4-6",
    "temperature": 0.7,
    "max_tokens": 1024
}

with open("config.json", "w") as f:
    json.dump(config, f)

print("JSON written")


with open("config.json", "r") as f:
    loaded = json.load(f)

print(loaded)
print(type(loaded))
print(loaded["model"])