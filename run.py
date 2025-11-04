import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from agent import ImageAnalysisAgent


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='AI Agent for continuous image analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py --watch ./images --output ./analysis
  python run.py --watch ./screenshots --output ./reports --interval 10
  python run.py --watch ./images --output ./analysis --once
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
        help='OpenAI model to use (default: gpt-4o)'
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
    
    args = parser.parse_args()
    
    agent = ImageAnalysisAgent(
        watch_directory=args.watch,
        output_directory=args.output,
        api_key=args.api_key,
        model=args.model,
        check_interval=args.interval
    )
    
    if args.once:
        agent.run_once()
    else:
        agent.run_continuous()


if __name__ == '__main__':
    main()
