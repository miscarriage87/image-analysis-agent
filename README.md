# Image Analysis AI Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

An autonomous AI agent that continuously monitors a directory for new images and generates extensive, detailed analysis and descriptions using GPT-4 Vision.

## 🌟 Features

- **Continuous Monitoring**: Real-time directory watching for new images
- **Extensive Analysis**: 10-point comprehensive image descriptions
- **Multiple Formats**: Support for JPG, PNG, GIF, BMP, WEBP
- **Persistent Tracking**: Remembers processed images
- **Dual Output**: Human-readable text + machine-readable JSON
- **Flexible Modes**: Continuous or single-run processing

## 📋 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/image-analysis-agent.git
cd image-analysis-agent
./scripts/setup.sh
```

Edit `.env` and add your OpenAI API key, then:

```bash
python run.py
```

See [Quick Start Guide](docs/QUICKSTART.md) for detailed instructions.

## 📁 Project Structure

```
image-analysis-agent/
├── src/
│   ├── __init__.py
│   └── agent.py              # Core agent implementation
├── examples/
│   └── basic_usage.py        # Usage examples
├── scripts/
│   ├── setup.sh              # Unix setup script
│   └── setup.bat             # Windows setup script
├── docs/
│   ├── README.md             # Full documentation
│   └── QUICKSTART.md         # Quick start guide
├── run.py                    # Main entry point
├── requirements.txt          # Dependencies
├── .env.example             # Configuration template
└── LICENSE                   # MIT License
```

## 🚀 Usage

### Basic Usage
```bash
python run.py --watch ./images --output ./analysis
```

### Single Run Mode
```bash
python run.py --watch ./images --output ./analysis --once
```

### Custom Configuration
```bash
python run.py --watch ./screenshots --output ./reports --interval 10 --model gpt-4o
```

### Programmatic Usage
```python
from src.agent import ImageAnalysisAgent

agent = ImageAnalysisAgent(
    watch_directory="./images",
    output_directory="./analysis"
)
agent.run_continuous()
```

## 📊 Analysis Output

Each image generates:
- **Text Report**: Detailed human-readable analysis
- **JSON Report**: Structured data for automation

Analysis includes:
1. Overall scene description
2. Main subjects and objects
3. Actions and activities
4. Environment and setting
5. Colors and lighting
6. Composition and perspective
7. Text/signage detection
8. Technical details
9. Context and implications
10. Sequential pattern analysis

## 🔧 Requirements

- Python 3.8+
- OpenAI API key with GPT-4 Vision access
- Dependencies: `openai`, `watchdog`, `pillow`, `python-dotenv`

## 📖 Documentation

- [Full Documentation](docs/README.md)
- [Quick Start Guide](docs/QUICKSTART.md)
- [Examples](examples/)

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with OpenAI's GPT-4 Vision API for advanced image understanding.

---

**Note**: This project requires an OpenAI API key and will incur costs based on usage. Monitor your API usage dashboard.
