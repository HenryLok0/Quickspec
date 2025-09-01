

# quickspec

[![Code Size](https://img.shields.io/github/languages/code-size/HenryLok0/Quickspec?style=flat-square&logo=github)](https://github.com/HenryLok0/Quickspec)
![PyPI - Version](https://img.shields.io/pypi/v/quickspec)
[![MIT License](https://img.shields.io/github/license/HenryLok0/Quickspec?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/HenryLok0/Quickspec?style=flat-square)](https://github.com/HenryLok0/Quickspec/stargazers)

Instantly display your computer hardware specs in the terminal. Supports Windows/macOS/Linux. One command shows CPU, memory, disk, GPU, motherboard, BIOS, and more.

## Features

- One command for all major hardware specs
- `--detail` flag shows motherboard, BIOS, network adapters, display resolution, boot time, cache, virtualization, battery, and more (Windows only)
- Cross-platform: Windows, macOS, Linux
- Minimal dependencies, easy installation

## Installation

```bash
pip install quickspec
```

## Quick Start

```bash
# Install
pip install quickspec

# Show main hardware specs
quickspec

# Show all detailed hardware info (Windows)
quickspec --detail
```

## Usage

```bash
# Basic usage
quickspec

# Show detailed info
quickspec --detail
```

## Options

| Option         | Description |
|----------------|-------------|
| `--detail`     | Show motherboard, BIOS, network adapters, display resolution, boot time, cache, virtualization, battery, and more (Windows only) |

## Examples

```bash
# Show main hardware specs
quickspec

# Show all detailed hardware info
quickspec --detail
```

## Comparison

| Feature         | quickspec | lshw | inxi | dmidecode |
|-----------------|-----------|------|------|-----------|
| CPU/Memory/Disk | Yes       | Yes  | Yes  | Yes       |
| GPU             | Yes       | Yes  | Yes  | No        |
| Motherboard/BIOS| Yes (Win) | Yes  | Yes  | Yes       |
| Battery         | Yes (Win) | No   | Yes  | No        |
| One-line install| Yes       | No   | No   | No        |
| Cross-platform  | Yes       | Partial| Partial| No    |

## Why quickspec?

- Instantly get all major hardware info for quick checks, reports, or sharing
- Advanced details on Windows: motherboard, BIOS, battery, etc.
- Minimal dependencies, easy install, no admin required
- Cross-platform, works in any environment

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=HenryLok0/Quickspec&type=Date)](https://star-history.com/#HenryLok0/Quickspec&Date)

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Support

If you have questions or suggestions, please open an issue on GitHub.

Thanks to all contributors and the open-source community for your support!

---

## Troubleshooting

- Command not found: try `python -m quickspec`.
- Windows path/encoding issues: run from a local folder and ensure UTF-8 console.
- Permission issues: if install or run fails, try running as administrator.
