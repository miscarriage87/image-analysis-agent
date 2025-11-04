# Image Analysis AI Agent

An autonomous AI agent that continuously monitors a directory for new images and generates extensive, detailed analysis and descriptions of what's happening in each image.

## Features

- **Continuous Monitoring**: Watches a directory for new images in real-time
- **Extensive Analysis**: Generates comprehensive descriptions including:
  - Overall scene description
  - Main subjects and objects
  - Actions and activities
  - Environment and setting
  - Colors and lighting
  - Composition and perspective
  - Text or signage detection
  - Technical details
  - Context and implications
  - Sequential pattern analysis
- **Multiple Format Support**: JPG, JPEG, PNG, GIF, BMP, WEBP
- **Persistent Tracking**: Remembers processed images to avoid duplicates
- **Detailed Output**: Saves analysis in both human-readable text and JSON formats
- **Flexible Modes**: Run continuously or process once and exit

## Installation

1. Clone or download this project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

Or set it as an environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

### Basic Usage (Continuous Monitoring)

```bash
python agent.py --watch ./images --output ./analysis
```

This will:
- Monitor the `./images` directory for new images
- Analyze each new image using GPT-4 Vision
- Save detailed analysis to `./analysis` directory
- Continue running until stopped with Ctrl+C

### Single Run Mode

Process all existing images once and exit:

```bash
python agent.py --watch ./images --output ./analysis --once
```

### Advanced Options

```bash
python agent.py \
  --watch ./screenshots \
  --output ./reports \
  --interval 10 \
  --model gpt-4o \
  --api-key YOUR_API_KEY
```

### Command Line Arguments

- `--watch`: Directory to watch for new images (default: `./input_images`)
- `--output`: Directory to save analysis results (default: `./analysis_output`)
- `--interval`: Check interval in seconds (default: `5`)
- `--model`: OpenAI model to use (default: `gpt-4o`)
- `--once`: Process existing images once and exit (default: continuous monitoring)
- `--api-key`: OpenAI API key (or use OPENAI_API_KEY environment variable)

## Output Format

For each analyzed image, the agent creates two files:

### 1. Text Report (`*_analysis.txt`)
```
Image Analysis Report
================================================================================

Image: screenshot_001.png
Analyzed: 2024-01-15T10:30:45.123456
Model: gpt-4o

================================================================================

DETAILED ANALYSIS:

[Extensive description of the image...]

================================================================================
Tokens used: 1234
```

### 2. JSON Report (`*_analysis.json`)
```json
{
  "success": true,
  "image_path": "/path/to/image.png",
  "image_name": "image.png",
  "timestamp": "2024-01-15T10:30:45.123456",
  "analysis": "Detailed analysis text...",
  "model": "gpt-4o",
  "tokens_used": 1234
}
```

## Use Cases

- **Screen Recording Analysis**: Analyze screenshots from automated testing or screen recording tools
- **Security Monitoring**: Analyze images from security cameras
- **Quality Assurance**: Monitor and document visual changes in applications
- **Documentation**: Auto-generate descriptions for image archives
- **Accessibility**: Create detailed descriptions for visually impaired users
- **Research**: Analyze experimental results captured in images
- **Social Media Monitoring**: Analyze images from social media feeds

## Example Workflow

1. Another program saves screenshots to `./screenshots/`
2. The agent continuously monitors this directory
3. When a new image appears, the agent:
   - Detects the new file
   - Analyzes it with AI vision
   - Generates extensive description
   - Saves the analysis
   - Marks the image as processed
4. The process repeats for each new image

## Configuration

You can configure the agent using:

1. **Command line arguments** (highest priority)
2. **Environment variables** (`.env` file)
3. **Default values** (built-in)

## Requirements

- Python 3.8+
- OpenAI API key with access to vision models (GPT-4 Vision)
- Sufficient API credits for image analysis

## Cost Considerations

- GPT-4 Vision API calls cost tokens based on image size and detail level
- The agent uses "high" detail mode for comprehensive analysis
- Monitor your OpenAI usage dashboard to track costs
- Consider using `--once` mode for batch processing to control costs

## Troubleshooting

**Agent not detecting images:**
- Ensure the watch directory exists and is accessible
- Check file permissions
- Verify image formats are supported

**API errors:**
- Verify your OpenAI API key is valid
- Check your API quota and billing status
- Ensure you have access to vision models

**Out of memory:**
- Process images in smaller batches using `--once` mode
- Reduce the check interval to process images more slowly

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
