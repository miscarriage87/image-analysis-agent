import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from agent import ImageAnalysisAgent


def example_continuous_monitoring():
    print("Example 1: Continuous Monitoring")
    print("-" * 50)
    
    agent = ImageAnalysisAgent(
        watch_directory="./input_images",
        output_directory="./analysis_output",
        check_interval=5,
        model="gpt-4o"
    )
    
    agent.run_continuous()


def example_single_run():
    print("Example 2: Single Run (Process Once)")
    print("-" * 50)
    
    agent = ImageAnalysisAgent(
        watch_directory="./input_images",
        output_directory="./analysis_output",
        model="gpt-4o"
    )
    
    agent.run_once()


def example_custom_configuration():
    print("Example 3: Custom Configuration")
    print("-" * 50)
    
    agent = ImageAnalysisAgent(
        watch_directory="./screenshots",
        output_directory="./detailed_reports",
        check_interval=10,
        model="gpt-4o",
        supported_formats=['.png', '.jpg', '.jpeg']
    )
    
    agent.run_continuous()


def example_programmatic_usage():
    print("Example 4: Programmatic Usage")
    print("-" * 50)
    
    agent = ImageAnalysisAgent(
        watch_directory="./test_images",
        output_directory="./test_output",
        model="gpt-4o"
    )
    
    new_images = agent.scan_for_new_images()
    
    print(f"Found {len(new_images)} new images")
    
    for image_path in new_images:
        print(f"\nProcessing: {image_path.name}")
        result = agent.analyze_image(image_path)
        
        if result['success']:
            print(f"Analysis preview: {result['analysis'][:200]}...")
            agent.save_analysis(result)
            agent.processed_images.add(str(image_path))
        else:
            print(f"Error: {result['error']}")
    
    agent._save_processed_images()
    print("\nProcessing complete!")


if __name__ == '__main__':
    examples = {
        '1': ('Continuous Monitoring', example_continuous_monitoring),
        '2': ('Single Run', example_single_run),
        '3': ('Custom Configuration', example_custom_configuration),
        '4': ('Programmatic Usage', example_programmatic_usage)
    }
    
    print("\nImage Analysis Agent - Examples")
    print("=" * 50)
    print("\nAvailable examples:")
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")
    print()
    
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        choice = input("Select an example (1-4): ").strip()
    
    if choice in examples:
        name, func = examples[choice]
        print(f"\nRunning: {name}\n")
        func()
    else:
        print("Invalid choice. Please select 1-4.")
