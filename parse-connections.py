#!/usr/bin/env python3

import pandas as pd

STARTS = ["🟡", "🟢", "🔵", "🟣"]

connections = []
with open("connection-archive.txt") as file:
    for line in file:
        if line[0] in STARTS:
            clue, words = line[1:].split(":")
            row = [w.strip() for w in words.split(",")] + [clue.strip()]
            connections.append(row)

df = pd.DataFrame(connections, columns=[0, 1, 2, 3, "clue"])
df.to_csv("connections.csv", index=False)
