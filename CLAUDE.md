# Project Instructions for Claude

## Run the project
1. Open the repository root:
   - `e:\Software Projects\Hirewheel\QR-Code-Generator`
2. Activate the Python virtual environment.
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows CMD: `.venv\Scripts\activate.bat`
   - macOS/Linux: `source .venv/bin/activate`
3. Install dependencies if needed:
   - `python -m pip install -r requirements.txt`
4. Execute the project:
   - `python main.py`

## Expected behavior
- The script prompts for a URL.
- It rejects empty input and any value that does not start with `http://` or `https://`.
- It generates a QR code image and saves it in `output/`.
- The saved filename is a sanitized slug of the URL, with a counter suffix added if a duplicate file already exists.
- On success, it prints the absolute path to the saved PNG file.

## Output location
- Generated files are stored in the repository root under:
  - `output/`
- Example output file path:
  - `output/example_com_page.png`

## Virtual environment setup
1. From the repository root, create the environment if it does not exist:
   - `python -m venv .venv`
2. Activate it as shown above.
3. Install packages:
   - `python -m pip install -r requirements.txt`

## Conventions Claude should follow
- Use the root `main.py` file as the program entry point.
- Do not modify `src/main.py`; this repository uses `main.py` at the root.
- Keep all generated assets inside the `output/` directory.
- Avoid asking clarifying questions for basic usage flow; follow the documented run command and error handling.
- Handle invalid input with a clean error message and non-zero exit code.
