 1. Scaffold the repo and write CLAUDE.md
Change: Create the project folder, initialize git, and write a CLAUDE.md that documents the run command, the venv setup steps, where output files go, and any conventions Claude should follow.
Verify: A fresh Claude session can read CLAUDE.md and execute the project without asking clarifying questions.
2. Create project structure
Change: Create the output/ subfolder and empty main.py.
Verify: ls -R confirms both exist.
3. Set up a virtual environment
Change: Initialize and activate a venv inside the project root.
Verify: which python points to the venv, not the system interpreter.
4. Install dependencies
Change: pip install qrcode[pil] to pull in the library and Pillow.
Verify: pip show qrcode and pip show Pillow both return version numbers.
5. Freeze requirements
Change: pip freeze > requirements.txt to lock versions.
Verify: requirements.txt lists qrcode and Pillow with pinned versions.
6. Accept and validate URL input
Change: Prompt for a URL and reject empty strings or anything not starting with http:// or https://.
Verify: Blank and non-URL inputs both exit with a clear error before generating anything.
7. Generate the QR code