text = open("raw.txt", encoding="utf-8").read()

start = text.find("*** START OF")
start = text.find("\n", start)
text = text[start + 1:]

end = text.find("*** END OF")
text = text[:end]

lines = text.splitlines()
keepLines = []
skipNext = False
started = False

for line in lines:
    line = line.strip()

    if line == "":
        continue

    if skipNext:
        skipNext = False
        continue

    if line.startswith("CHAPTER") and line.endswith("."):
        started = True
        skipNext = True
        continue

    if not started:
        continue

    if line.startswith("*") or line.startswith("["):
        continue
    if line == "THE END" or line == "CHORUS." or line == "Contents":
        continue

    keepLines.append(line)

text = "\n".join(keepLines)

text = text.replace("_", "")
text = text.replace("(", "")
text = text.replace(")", "")
text = text.replace("—", " ")
text = text.replace("“", "")
text = text.replace("”", "")
text = text.replace("‘", "")
text = text.replace("’", "'")
text = text.replace(":", "")

text = text.lower()

open("source.txt", "w", encoding="utf-8").write(text)
print("Done")