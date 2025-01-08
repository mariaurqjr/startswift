# StartSwift

StartSwift is a Python-based utility designed to speed up the Windows startup process by managing programs that launch at boot. It provides an easy-to-use command-line interface to list and disable startup programs.

## Features

- List all programs that are set to run at Windows startup.
- Disable unwanted startup programs to improve boot time.

## Requirements

- Windows Operating System
- Python 3.x
- Administrator privileges (to modify startup settings)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/startswift.git
   ```
2. Navigate to the StartSwift directory:
   ```bash
   cd startswift
   ```

## Usage

Run StartSwift using Python:

```bash
python startswift.py
```

### Options

- **List all startup programs**: Displays all programs currently set to run on startup.
- **Disable a startup program**: Allows you to specify a program by name to disable from running at startup.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Modifying startup programs can affect the functionality of your machine. Ensure that you know what each program does before disabling it. The author is not responsible for any issues that arise from using this software.