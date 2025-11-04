import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from agent import ImageAnalysisAgent


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='AI Agent for continuous image analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Using OpenAI:
  python run.py --watch ./images --output ./analysis
  python run.py --watch ./screenshots --output ./reports --interval 10

  # Using Ollama (local LLM):
  python run.py --model ollama/llava --watch ./images --output ./analysis
  python run.py --model ollama/llama3.2-vision --watch ./images --output ./analysis --once

Note: For Ollama, make sure Ollama is installed and running:
  - Install: https://ollama.ai
  - Pull a vision model: ollama pull llava
  - Start Ollama service (usually runs automatically)
        """
    )
    
    parser.add_argument(
        '--watch',
        type=str,
        default='./input_images',
        help='Directory to watch for new images (default: ./input_images)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='./analysis_output',
        help='Directory to save analysis results (default: ./analysis_output)'
    )
    
    parser.add_argument(
        '--interval',
        type=int,
        default=5,
        help='Check interval in seconds (default: 5)'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='gpt-4o',
        help='Model to use: OpenAI (e.g., gpt-4o) or Ollama (e.g., ollama/llava, ollama/llama3.2-vision) (default: gpt-4o)'
    )

    parser.add_argument(
        '--once',
        action='store_true',
        help='Process existing images once and exit (default: continuous monitoring)'
    )

    parser.add_argument(
        '--api-key',
        type=str,
        help='OpenAI API key (or set OPENAI_API_KEY environment variable)'
    )

    parser.add_argument(
        '--ollama-url',
        type=str,
        default='http://localhost:11434',
        help='Ollama base URL (default: http://localhost:11434)'
    )

    args = parser.parse_args()

    agent = ImageAnalysisAgent(
        watch_directory=args.watch,
        output_directory=args.output,
        api_key=args.api_key,
        model=args.model,
        check_interval=args.interval,
        ollama_base_url=args.ollama_url
    )

    if args.once:
        agent.run_once()
    else:
        agent.run_continuous()


if __name__ == '__main__':
    main()
