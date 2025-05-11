# The Real Python Project Template

## Toolchain

- `uv` for package management
- `pytest` (a python package) for testing
- `black` for formatting
- `isort` to sort imports

## Instructions


### Setup
1. Clone this repository
2. Replace `.gitignore` with the custom gitignore you want
3. Run `uv venv --python [version]`
4. Activate with `source .venv/bin/activate`
5. `uv pip install -r requirements.txt`
6. Cd to mypackage, install the package in editable mode `pip install -e .`

### Running
7. To run the main file, do `python -m mypackage.main`  or cd into mypackage and do `python main.py`
8. Try making a change to the package, you should see it reflected 

### Testing
9. Run pytest anywhere, it should work now.

### Formatting
10. `uv pip install black`
11. `black .`

12. `uv pip install isort`



