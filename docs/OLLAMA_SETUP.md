# Ollama Setup Guide

This guide will help you set up Ollama for local, free image analysis.

## What is Ollama?

Ollama is a tool that lets you run large language models locally on your computer. This means:
- ✅ **Free** - No API costs
- ✅ **Private** - Your images never leave your computer
- ✅ **Fast** - No network latency
- ⚠️ **Hardware Requirements** - Needs 8GB+ RAM (16GB recommended)

## Installation

### macOS

**Option 1: Download from website**
1. Visit https://ollama.ai
2. Download the macOS installer
3. Open the downloaded file and follow installation instructions

**Option 2: Using Homebrew**
```bash
brew install ollama
```

### Linux

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Windows

1. Visit https://ollama.ai
2. Download the Windows installer
3. Run the installer and follow the instructions

## Verify Installation

After installation, verify Ollama is working:

```bash
ollama --version
```

## Pull a Vision Model

Ollama needs to download models before you can use them. For image analysis, you need a vision model:

### Recommended: LLaVA (7GB)
```bash
ollama pull llava
```

### Alternative: Llama 3.2 Vision (7.9GB)
```bash
ollama pull llama3.2-vision
```

### Alternative: BakLLaVA (4.7GB)
```bash
ollama pull bakllava
```

## Start Ollama Service

Ollama usually starts automatically after installation. If not:

```bash
ollama serve
```

Keep this terminal open while using the image analysis agent.

## Test Ollama

Test that Ollama is working:

```bash
ollama list
```

You should see the models you pulled.

## Using with Image Analysis Agent

Once Ollama is set up, use it with the agent:

```bash
# Using LLaVA
python run.py --model ollama/llava

# Using Llama 3.2 Vision
python run.py --model ollama/llama3.2-vision

# Using BakLLaVA
python run.py --model ollama/bakllava
```

## Troubleshooting

### "Connection refused" error
- Make sure Ollama is running: `ollama serve`
- Check if Ollama is listening on port 11434: `curl http://localhost:11434`

### "Model not found" error
- Pull the model first: `ollama pull llava`
- List available models: `ollama list`

### Slow performance
- Vision models require significant RAM (8GB minimum, 16GB recommended)
- Close other applications to free up memory
- Consider using a smaller model like `bakllava`

### Out of memory errors
- Try a smaller model
- Reduce the number of concurrent processes
- Upgrade your RAM if possible

## Model Comparison

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| llava | 7GB | Medium | High | General use (recommended) |
| llama3.2-vision | 7.9GB | Medium | Very High | Best quality |
| bakllava | 4.7GB | Fast | Good | Lower-end hardware |

## Additional Resources

- Ollama Documentation: https://github.com/ollama/ollama
- Ollama Models: https://ollama.ai/library
- Community Discord: https://discord.gg/ollama
