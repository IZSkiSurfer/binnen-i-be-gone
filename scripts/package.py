#!/usr/bin/env python3
"""Build browser-specific archives from the tracked extension source."""
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
version = manifest["version"]
out = ROOT / "dist"
out.mkdir(exist_ok=True)
files = [ROOT / name for name in ("background.js", "binnenibegone.js", "options.js", "options.html", "LICENSE")]
for directory in ("images", "css"):
    files.extend(p for p in (ROOT / directory).rglob("*") if p.is_file())
for browser in ("chrome", "edge", "firefox"):
    config = dict(manifest)
    suffix = "zip"
    if browser == "firefox":
        config["manifest_version"] = 2
        config["background"] = {"scripts": ["background.js"]}
        config["browser_action"] = config.pop("action")
        config["browser_specific_settings"] = {"gecko": {"id": "binnen-i-be-gone@izskisurfer.github.io"}}
        suffix = "xpi"
    target = out / f"binnen-i-be-gone-{version}-{browser}.{suffix}"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("manifest.json", json.dumps(config, ensure_ascii=False, indent=2) + "\n")
        for path in sorted(files):
            archive.write(path, path.relative_to(ROOT).as_posix())
    print(target)
