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

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-key-here
```

## Running the Agent

### Continuous Monitoring (Default)
```bash
python agent.py
```

This will:
- Watch `./input_images` for new images
- Analyze each image automatically
- Save results to `./analysis_output`
- Keep running until you press Ctrl+C

### Process Once and Exit
```bash
python agent.py --once
```

### Custom Directories
```bash
python agent.py --watch /path/to/screenshots --output /path/to/reports
```

### Adjust Check Interval
```bash
python agent.py --interval 10
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
