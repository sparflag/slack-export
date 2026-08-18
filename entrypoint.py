#!/usr/bin/env python3
"""Slack Export — real mini-challenge (slack-export)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", None)


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    clue = CHALLENGE_KEY or mat["delivery_blob"][:40] + "..."
    export = {
        "messages": [
            {"user": "alice", "text": "standup at 9", "deleted": False},
            {"user": "bob", "text": "deploy done", "deleted": False},
            {
                "user": "admin",
                "text": f"vault seed (deleted): {clue}",
                "deleted": True,
                "ts": "1690000000.001",
            },
        ]
    }
    with open("/challenge/export.json", "w") as f:
        json.dump(export, f, indent=2)
    print("Slack Export: deleted message in export.json; base64-decode flag.enc.")


if __name__ == "__main__":
    main()
