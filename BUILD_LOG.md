## Task 1 — Scaffold repo and CLAUDE docs
- Brief: Create the project folder, initialize git, and write CLAUDE.md.
- What was proposed: Add root-level entrypoint guidance and Claude-specific usage conventions.
- Verification: Confirmed `CLAUDE.md` exists and documents venv setup, run command, output location, and conventions.

## Task 2 — Create project structure
- Brief: Create the output/ subfolder and empty main.py.
- What was proposed: Establish the app structure and output directory before implementing logic.
- Verification: Confirmed `output/` and `main.py` exist in the repository root.

## Task 3 — Set up a virtual environment
- Brief: Initialize and activate a venv inside the project root.
- What was proposed: Create `.venv` and use it for isolated Python execution.
- Verification: Confirmed the local `.venv` was created and used for installs.

## Task 4 — Install dependencies
- Brief: pip install qrcode[pil] to pull in the library and Pillow.
- What was proposed: Install QR code generation and image support dependencies.
- Verification: Confirmed `qrcode` and `Pillow` were installed into `.venv`.

## Task 5 — Freeze requirements
- Brief: pip freeze > requirements.txt to lock versions.
- What was proposed: Capture dependency versions in `requirements.txt`.
- Verification: Confirmed `requirements.txt` contains pinned `qrcode` and `Pillow` versions.

## Task 6 — Accept and validate URL input
- Brief: Prompt for a URL and reject empty strings or anything not starting with http:// or https://.
- What was proposed: Add input validation to prevent invalid URL values.
- Verification: Confirmed blank and invalid scheme inputs raise clear `ValueError` messages.

## Task 7 — Generate the QR code
- Brief: Pass the validated URL into qrcode.make() and store the result.
- What was proposed: Use the `qrcode` library to create a PIL image from the URL.
- Verification: Confirmed `qrcode.make(url)` returns a PIL image object.

## Task 8 — Build the output file path
- Brief: Slugify the URL and join it to output/ using pathlib.Path.
- What was proposed: Generate a safe filename from the URL and place it in `output/`.
- Verification: Confirmed the resolved path is well-formed and contains no illegal filename characters.

## Task 9 — Save the image
- Brief: Call .save(output_path) to write the PNG to disk.
- What was proposed: Persist the generated QR code image into the output folder.
- Verification: Confirmed the file appears in `output/` after saving.

## Task 10 — Scan the QR code
- Brief: No code change — functional validation only.
- What was proposed: Verify a scanner decodes the generated QR back to the original URL.
- Verification: Confirmed the saved QR code scans to the entered URL.

## Task 11 — Auto-create the output folder if missing
- Brief: Add output_dir.mkdir(parents=True, exist_ok=True) before saving.
- What was proposed: Ensure the output directory exists automatically when saving.
- Verification: Confirmed deleting `output/` and rerunning the script recreates it cleanly.

## Task 12 — Handle duplicate filenames
- Brief: Append a counter suffix (_1, _2) if the target file already exists.
- What was proposed: Avoid overwriting existing QR files for duplicate URLs.
- Verification: Confirmed subsequent runs with the same URL produce separately suffixed files.

## Task 13 — Add error handling and a __main__ guard
- Brief: Wrap logic in if __name__ == "__main__": and a try/except that prints a clean error.
- What was proposed: Prevent raw tracebacks and return a clean error message on failure.
- Verification: Confirmed the script exits with a readable `Error:` message when an exception is raised.

## Task 14 — Print the output path on success
- Brief: Print the resolved absolute path of the saved file after saving.
- What was proposed: Show the user the full saved file path on successful generation.
- Verification: Confirmed the script prints the absolute output path after saving.
