import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".java", ".cpp", ".c", ".sh"],
    "Installers": [".exe", ".msi"],
}


def get_category(extension: str) -> str:
    """Return the folder name for a file extension, or 'Other'."""
    extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"


def unique_destination(dest: Path) -> Path:
    """If dest already exists, return 'name (1).ext', 'name (2).ext', ..."""
    if not dest.exists():
        return dest
    counter = 1
    while True:
        candidate = dest.with_name(f"{dest.stem} ({counter}){dest.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(folder: Path, apply: bool) -> None:
    moved = 0
    for item in folder.iterdir():
        if not item.is_file():
            continue

        category = get_category(item.suffix)
        target_dir = folder / category
        destination = unique_destination(target_dir / item.name)

        print(f"{'MOVE' if apply else 'WOULD MOVE'}: {item.name}  ->  {category}/{destination.name}")

        if apply:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
        moved += 1

    print(f"\n{moved} file(s) {'moved' if apply else 'would be moved'}.")
    if not apply and moved:
        print("This was a dry run. Add --apply to actually move files.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize files into folders by type.")
    parser.add_argument("folder", help="Path to the folder to organize")
    parser.add_argument("--apply", action="store_true", help="Actually move files (default is dry run)")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid folder.")
        return

    organize(folder, args.apply)


if __name__ == "__main__":
    main()
