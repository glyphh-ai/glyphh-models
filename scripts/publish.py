#!/usr/bin/env python3
"""
Package a model directory into a .glyphh file for release.

Usage:
    python scripts/publish.py <model_dir> [--version <version>]

The .glyphh file is a zip archive containing the model's manifest,
config, encoder, build script, and data directory.
"""

import argparse
import sys
import zipfile
from pathlib import Path

import yaml

PACKAGE_INCLUDES = [
    "manifest.yaml",
    "config.yaml",
    "encoder.py",
    "build.py",
    "tests.py",
    "data",
    "tests",
]


def package_model(model_dir: Path, version: str | None = None) -> Path:
    manifest_path = model_dir / "manifest.yaml"
    if not manifest_path.exists():
        print(f"Error: {manifest_path} not found", file=sys.stderr)
        sys.exit(1)

    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    model_id = manifest.get("model_id", model_dir.name)

    if version:
        manifest["version"] = version

    out_file = Path(f"{model_id}.glyphh")

    with zipfile.ZipFile(out_file, "w", zipfile.ZIP_DEFLATED) as zf:
        # Write manifest (possibly with updated version)
        zf.writestr("manifest.yaml", yaml.dump(manifest, default_flow_style=False, sort_keys=False))

        for include in PACKAGE_INCLUDES:
            if include == "manifest.yaml":
                continue  # already written above
            item = model_dir / include
            if item.is_file():
                zf.write(item, include)
            elif item.is_dir():
                for child in sorted(item.rglob("*")):
                    if child.is_file() and not child.name.startswith("."):
                        zf.write(child, str(child.relative_to(model_dir)))

    size_kb = out_file.stat().st_size / 1024
    print(f"Packaged {model_id} v{manifest.get('version', '?')} -> {out_file} ({size_kb:.1f} KB)")
    return out_file


def main():
    parser = argparse.ArgumentParser(description="Package a Glyphh model")
    parser.add_argument("model_dir", type=Path, help="Path to model directory")
    parser.add_argument("--version", "-v", help="Override version in manifest")
    args = parser.parse_args()

    package_model(args.model_dir, args.version)


if __name__ == "__main__":
    main()
