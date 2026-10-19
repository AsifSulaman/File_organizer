# File Organizer

A small Python CLI tool that sorts files in a folder into subfolders by file type (Images, Documents, Archives, etc.).

## Features

- Sorts files into categories by extension; unknown types go to `Other/`
- **Dry run by default**: previews changes before moving anything
- Never overwrites: name collisions become `file (1).ext`, `file (2).ext`, ...
- No dependencies: standard library only (Python 3.8+)

## Usage

```bash
# Preview (nothing is moved)
python file_organizer.py "C:\Users\you\Downloads"

# Actually move files
python file_organizer.py "C:\Users\you\Downloads" --apply
```

Example output:

```
WOULD MOVE: photo.jpg  ->  Images/photo.jpg
WOULD MOVE: report.pdf  ->  Documents/report.pdf

2 file(s) would be moved.
This was a dry run. Add --apply to actually move files.
```

## Customizing

Edit the `CATEGORIES` dictionary at the top of `file_organizer.py` to add or change folders and extensions.

## Notes

- Only files directly inside the target folder are moved; existing subfolders are left untouched.
- Move the script out of the target folder first, or it will organize itself into `Code/`.

## License

MIT
