from pathlib import Path
import shutil

root = Path(".")
src = Path(__file__).resolve().parent.parent / "bundle_discoverability"

required = ["sitemap.xml", "robots.txt", "llms.txt"]
missing = [name for name in required if not (src / name).exists()]
if missing:
    raise SystemExit("Missing bundled files: " + ", ".join(missing))

for name in required:
    shutil.copy2(src / name, root / name)
    print(f"Replaced {name}")

print("Done: sitemap.xml, robots.txt, and llms.txt were replaced with the updated v44 versions.")
