# Bambu-Connect - Python Library for Bambu Lab Printers

## Overview
Bambu-Connect is a Python library designed to provide an easy and intuitive way to interact with Bambu Lab Printers. The goal of this project is to simplify the process of monitoring printers, sending print jobs, watching camera feeds, and performing other operations for users of Bambu Lab Printers. This library encapsulates the complexity of direct device communication, offering a user-friendly interface for various printer-related tasks.

## Features
- **Printer Status Monitoring**: Retrieve real-time status information from your printer, including temperatures, print progress, and more.
- **Camera Feed Access**: Stream live feed from your printer's camera to monitor print jobs remotely.
- **Send Print Jobs**: Easily send new print jobs to your printer directly from Python scripts.
- **G-code Execution**: Execute G-code commands for advanced printer control and customization.
- **Printer Stats Dump**: Fetch detailed printer statistics and operational data for analysis and troubleshooting.

## Installation
To install Bambu-Connect, simply use pip:
```
pip install bambu-connect
```

## Setup
**Note: I couldn't find a good wiki page for IP and Access Code, and I only have a P1S so I'll try to stay general**

IP: `Settings > WLAN > IP`

Access Code: `Settings > WLAN > Access Code`

Serial Number:  https://wiki.bambulab.com/en/general/find-sn

## Usage

Checkout the `examples` folder for uses


## Contributing
Contributions to Bambu-Connect are welcome! Whether it's bug reports, feature requests, or code contributions, feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/mattcar15/bambu-connect).

## License
Bambu-Connect is released under the [MIT License](https://opensource.org/licenses/MIT).

---

*Note: Bambu-Connect is an independent project and is not affiliated with Bambu Lab.*

