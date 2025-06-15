# template_py
python project template

# Setup macOS / WSL
`chmod +x scripts/*.sh` : grant permission to execute all scripts in scripts folder.

To get started with this project, clone the repository and then run the following command to set up the development environment and install the necessary dependencies:

```bash
scripts/init_uv.sh
```
This script will:
1.  Check for and install `uv` if it's not already present.
2.  Create a virtual environment in `.venv`.
3.  Install the Python dependencies specified in `pyproject.toml`.

Once the script has finished, activate the virtual environment:
```bash
source .venv/bin/activate
```
