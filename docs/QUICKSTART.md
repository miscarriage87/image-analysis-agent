# Quick Start Guide

## Installation

### Option 1: Automated Setup (Recommended)

**On macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```cmd
setup.bat
```

### Option 2: Manual Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Configuration

### For OpenAI (Cloud)

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-key-here
```

### For Ollama (Local - Free)

1. **Install Ollama**
   - Visit https://ollama.ai and download for your OS
   - Or use package managers:
     ```bash
     # macOS
     brew install ollama

     # Linux
     curl -fsSL https://ollama.ai/install.sh | sh
     ```

2. **Pull a vision model**
   ```bash
   ollama pull llava
   # or for the latest Llama vision model
   ollama pull llama3.2-vision
   ```

3. **Verify Ollama is running**
   ```bash
   ollama list
   ```

   If Ollama isn't running, start it:
   ```bash
   ollama serve
   ```

## Running the Agent

### Using OpenAI

#### Continuous Monitoring (Default)
```bash
python run.py
```

#### Process Once and Exit
```bash
python run.py --once
```

### Using Ollama (Local)

#### Continuous Monitoring
```bash
python run.py --model ollama/llava
```

#### Process Once and Exit
```bash
python run.py --model ollama/llava --once
```

#### Using Different Ollama Models
```bash
# Llama 3.2 Vision
python run.py --model ollama/llama3.2-vision

# BakLLaVA
python run.py --model ollama/bakllava
```

### Common Options

This will:
- Watch `./input_images` for new images
- Analyze each image automatically
- Save results to `./analysis_output`
- Keep running until you press Ctrl+C

### Custom Directories
```bash
# OpenAI
python run.py --watch /path/to/screenshots --output /path/to/reports

# Ollama
python run.py --model ollama/llava --watch /path/to/screenshots --output /path/to/reports
```

### Adjust Check Interval
```bash
# OpenAI
python run.py --interval 10

# Ollama
python run.py --model ollama/llava --interval 10
```

## Testing the Agent

1. Start the agent:
```bash
python agent.py
```

2. In another terminal, copy an image to the watch directory:
```bash
cp /path/to/test-image.jpg input_images/
```

3. Watch the agent detect and analyze the image automatically!

4. Check the results:
```bash
ls analysis_output/
cat analysis_output/*_analysis.txt
```

## Integration with Other Programs

### Example: Screenshot Tool Integration

If you have a program that saves screenshots to a directory:

```bash
python agent.py --watch /path/to/screenshot/folder --output ./screenshot-analysis
```

### Example: Batch Processing

Process a folder of existing images:

```bash
python agent.py --watch /path/to/image/archive --output ./archive-analysis --once
```

### Example: Python Integration

```python
from agent import ImageAnalysisAgent

agent = ImageAnalysisAgent(
    watch_directory="./my_images",
    output_directory="./my_analysis"
)

agent.run_continuous()
```

## Output Files

For each image, you'll get:
- `imagename_timestamp_analysis.txt` - Human-readable report
- `imagename_timestamp_analysis.json` - Machine-readable JSON

## Tips

- The agent remembers processed images (stored in `processed_images.json`)
- Delete `processed_images.json` to reprocess all images
- Use `--model gpt-4o` for best results (default)
- Monitor your OpenAI API usage to control costs

## Troubleshooting

**"No module named 'openai'"**
- Run: `pip install -r requirements.txt`

**"Authentication error"**
- Check your API key in `.env` file
- Verify the key is valid in your OpenAI dashboard

**"No new images found"**
- Ensure images are in the correct directory
- Check supported formats: JPG, PNG, GIF, BMP, WEBP
- Verify file permissions

## Need Help?

Run with `--help` to see all options:
```bash
python agent.py --help
```
