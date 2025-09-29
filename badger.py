import sys, pathlib

BADGES = [
  "[![License](https://img.shields.io/badge/license-MIT-informational)](#)",
  "![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)",
  "![Made with Python](https://img.shields.io/badge/made%20with-Python-blue)"
]

def add_badges(path):
    p = pathlib.Path(path)
    if not p.exists(): 
        print("README not found"); return
    text = p.read_text(encoding="utf-8")
    p.write_text("\n".join(BADGES) + "\n\n" + text, encoding="utf-8")
    print("Badges injected.")

if __name__ == "__main__":
    readme = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    add_badges(readme)
