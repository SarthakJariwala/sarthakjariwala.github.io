import os


# to start with the same til-index state
file_content = [line for line in open("content/til/_index.md")][:7]

folders = sorted([
    folder
    for folder in os.listdir("content/til")
    if os.path.isdir("content/til/" + folder)
])

for folder in folders:
    file_content.append("\n")
    file_content.append(f"- [{folder.capitalize()}]({folder}" + "/)")
    file_content.append(f" : *{len(os.listdir('content/til/' + folder)) - 1} posts*\n")

file_content.append("\n---\n")

with open("content/til/_index.md", "w") as writer:
    for line in file_content:
        writer.write(line)
