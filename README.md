# Image Analysis AI Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

An autonomous AI agent that continuously monitors a directory for new images and generates extensive, detailed analysis and descriptions using GPT-4 Vision or local LLMs via Ollama.

## 🌟 Features

- **Continuous Monitoring**: Real-time directory watching for new images
- **Extensive Analysis**: 10-point comprehensive image descriptions
- **Multiple Formats**: Support for JPG, PNG, GIF, BMP, WEBP
- **Persistent Tracking**: Remembers processed images
- **Dual Output**: Human-readable text + machine-readable JSON
- **Flexible Modes**: Continuous or single-run processing
- **Local & Cloud LLMs**: Support for OpenAI GPT-4 Vision and local models via Ollama

## 📋 Quick Start

### Option 1: Using OpenAI (Cloud)

```bash
git clone https://github.com/YOUR_USERNAME/image-analysis-agent.git
cd image-analysis-agent
./scripts/setup.sh
```

Edit `.env` and add your OpenAI API key, then:

```bash
python run.py
```

### Option 2: Using Ollama (Local - Free)

1. Install Ollama from https://ollama.ai
2. Pull a vision model:
```bash
ollama pull llava
# or
ollama pull llama3.2-vision
```

3. Run the agent:
```bash
python run.py --model ollama/llava
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

### Using OpenAI (Cloud)
```bash
python run.py --watch ./images --output ./analysis
```

### Using Ollama (Local)
```bash
# Make sure Ollama is running and you have pulled a vision model
python run.py --model ollama/llava --watch ./images --output ./analysis
```

### Single Run Mode
```bash
# OpenAI
python run.py --watch ./images --output ./analysis --once

# Ollama
python run.py --model ollama/llava --watch ./images --output ./analysis --once
```

### Custom Configuration
```bash
python run.py --watch ./screenshots --output ./reports --interval 10 --model gpt-4o
```

### Programmatic Usage
```python
from src.agent import ImageAnalysisAgent

# Using OpenAI
agent = ImageAnalysisAgent(
    watch_directory="./images",
    output_directory="./analysis",
    model="gpt-4o"
)

# Using Ollama
agent = ImageAnalysisAgent(
    watch_directory="./images",
    output_directory="./analysis",
    model="ollama/llava"
)

agent.run_continuous()
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
- **For OpenAI**: OpenAI API key with GPT-4 Vision access
- **For Ollama**: Ollama installed locally (free, no API key needed)
- Dependencies: `openai`, `watchdog`, `pillow`, `python-dotenv`

## 🎯 Supported Models

### OpenAI Models
- `gpt-4o` (recommended)
- `gpt-4-vision-preview`
- `gpt-4-turbo`

### Ollama Models (Local)
- `ollama/llava` (recommended for general use)
- `ollama/llama3.2-vision` (latest Llama vision model)
- `ollama/bakllava` (alternative vision model)

To use Ollama models, prefix with `ollama/` (e.g., `--model ollama/llava`)

## 💰 Cost Comparison

### OpenAI GPT-4 Vision
- **Cost**: ~$0.01 per image (varies by detail level)
- **Speed**: Fast (network dependent)
- **Quality**: Excellent
- **Setup**: Easy (just API key)
- **Hardware**: None required

### Ollama (Local)
- **Cost**: $0 (completely free)
- **Speed**: Fast (no network latency)
- **Quality**: Very good (model dependent)
- **Setup**: Moderate (install + download model)
- **Hardware**: 8GB+ RAM required

**Example**: Analyzing 1000 images
- OpenAI: ~$10
- Ollama: $0

## 📖 Documentation

- [Full Documentation](docs/README.md)
- [Quick Start Guide](docs/QUICKSTART.md)
- [Examples](examples/)

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with OpenAI's GPT-4 Vision API and Ollama for advanced image understanding.

---

**Note**:
- **OpenAI**: Requires an API key and will incur costs based on usage. Monitor your API usage dashboard.
- **Ollama**: Free and runs locally. No API costs, but requires sufficient hardware (8GB+ RAM recommended).
