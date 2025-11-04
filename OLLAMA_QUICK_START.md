# Quick Reference: Local LLM Usage

## Installation

### 1. Install Ollama
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai
```

### 2. Pull a Vision Model
```bash
ollama pull llava
```

## Usage

### Basic Commands

```bash
# Single run with Ollama
python run.py --model ollama/llava --once

# Continuous monitoring with Ollama
python run.py --model ollama/llava

# With custom directories
python run.py --model ollama/llava --watch ./my_images --output ./my_analysis

# With custom check interval
python run.py --model ollama/llava --interval 10
```

### Model Options

```bash
# LLaVA (recommended)
python run.py --model ollama/llava

# Llama 3.2 Vision (best quality)
python run.py --model ollama/llama3.2-vision

# BakLLaVA (faster, smaller)
python run.py --model ollama/bakllava
```

### Switching Between OpenAI and Ollama

```bash
# Use OpenAI
python run.py --model gpt-4o

# Use Ollama
python run.py --model ollama/llava
```

## Programmatic Usage

```python
from src.agent import ImageAnalysisAgent

# Create agent with Ollama
agent = ImageAnalysisAgent(
    watch_directory="./images",
    output_directory="./analysis",
    model="ollama/llava"
)

# Run once
agent.run_once()

# Or run continuously
agent.run_continuous()
```

## Troubleshooting

### Ollama not found
```bash
# Check if Ollama is installed
which ollama

# If not installed, install it
brew install ollama  # macOS
```

### Model not found
```bash
# List available models
ollama list

# Pull the model if missing
ollama pull llava
```

### Connection refused
```bash
# Start Ollama service
ollama serve

# Check if it's running
curl http://localhost:11434
```

### Slow performance
- Close other applications
- Use a smaller model (bakllava)
- Ensure you have 8GB+ RAM

## Cost Savings

**Example: 1000 images**
- OpenAI GPT-4 Vision: ~$10
- Ollama (local): $0

**Example: 10,000 images**
- OpenAI GPT-4 Vision: ~$100
- Ollama (local): $0

## More Information

- Full setup guide: `docs/OLLAMA_SETUP.md`
- Implementation details: `docs/LOCAL_LLM_IMPLEMENTATION.md`
- Examples: `examples/basic_usage.py`
