
## Description

This utility is designed to merge multiple text files within a specified folder into a single file. It's equipped with a simple graphical user interface (GUI) for ease of use, allowing users to select folders and merge all text files contained within. The merged file will be saved in the same folder with the name "merged", taking the same file extension as the input files.

## Features

- **Easy to Use:** Simple GUI to select folders and merge files.
- **Efficient Merging:** Quickly merges all text files in a selected folder.
- **Flexible:** Works with any text files, regardless of the extension.

## Installation

To use this utility, follow these steps:

1. Download the latest release from the [Releases page](https://github.com/[YourUsername]/[YourRepository]/releases).
2. Unzip the downloaded file.
3. Run the executable file (`FileMergerUtility.exe`).

## Usage

1. Open the application.
2. Click on `Browse Folder` and select the folder containing the text files you want to merge.
3. The application will automatically merge the files and save a new file named `merged` with the appropriate extension in the same folder.
4. If you want to merge files from another folder, simply repeat the process.

## Building from Source

If you prefer to build the application from the source code:

1. Clone the repository:

```
1. git clone https://github.com/thebestryan/txtmerge.git
```

2. Navigate to the cloned directory and run:

```
pyinstaller --onefile --windowed app.py
```

Replace `app.py` with the path to the script if it's different.

## Contributing

Contributions are welcome! If you have suggestions for improving this utility, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Icon designed by thebestryan
- Another quality product by HairyAreolas

