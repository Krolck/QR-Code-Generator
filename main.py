import re
import sys
from pathlib import Path

import qrcode


def validate_url(value: str) -> str:
    url = value.strip()
    if not url:
        raise ValueError("URL must not be blank.")
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError('URL must begin with "http://" or "https://".')
    return url


def slugify_url(url: str) -> str:
    slug = url.lower()
    slug = slug.replace("http://", "").replace("https://", "")
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = slug.strip("_")
    return slug or "qr_code"


def build_output_path(url: str, output_dir: Path) -> Path:
    slug = slugify_url(url)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{slug}.png"
    counter = 1
    while output_path.exists():
        output_path = output_dir / f"{slug}_{counter}.png"
        counter += 1
    return output_path


def main() -> int:
    url_input = input("Enter the URL to encode: ").strip()
    url = validate_url(url_input)

    image = qrcode.make(url)

    output_dir = Path("output")
    output_path = build_output_path(url, output_dir)
    image.save(output_path)

    print(f"Saved QR code to: {output_path.resolve()}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)
