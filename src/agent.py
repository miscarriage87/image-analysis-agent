import os
import time
import json
import base64
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import openai
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ImageAnalysisAgent:
    def __init__(
        self,
        watch_directory: str,
        output_directory: str,
        api_key: Optional[str] = None,
        model: str = "gpt-4o",
        check_interval: int = 5,
        supported_formats: List[str] = None
    ):
        self.watch_directory = Path(watch_directory)
        self.output_directory = Path(output_directory)
        self.model = model
        self.check_interval = check_interval
        self.processed_images = set()
        self.supported_formats = supported_formats or ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
        
        self.watch_directory.mkdir(parents=True, exist_ok=True)
        self.output_directory.mkdir(parents=True, exist_ok=True)
        
        self.client = openai.OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        
        self.processed_log = self.output_directory / 'processed_images.json'
        self._load_processed_images()

    def _load_processed_images(self):
        if self.processed_log.exists():
            with open(self.processed_log, 'r') as f:
                data = json.load(f)
                self.processed_images = set(data.get('processed', []))

    def _save_processed_images(self):
        with open(self.processed_log, 'w') as f:
            json.dump({'processed': list(self.processed_images)}, f, indent=2)

    def encode_image(self, image_path: Path) -> str:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_image(self, image_path: Path) -> Dict:
        print(f"Analyzing image: {image_path.name}")
        
        base64_image = self.encode_image(image_path)
        file_extension = image_path.suffix.lower()
        
        mime_types = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.webp': 'image/webp'
        }
        mime_type = mime_types.get(file_extension, 'image/jpeg')
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert image analyst. Provide extensive, detailed descriptions of images.
                        
Your analysis should include:
1. Overall scene description - what is happening in the image
2. Main subjects and objects - detailed description of people, animals, or objects
3. Actions and activities - what actions are being performed
4. Environment and setting - location, time of day, weather conditions
5. Colors and lighting - dominant colors, lighting conditions, mood
6. Composition and perspective - camera angle, framing, focal points
7. Text or signage - any visible text, labels, or signs
8. Technical details - image quality, resolution observations
9. Context and implications - what this image might represent or document
10. Sequential analysis - if this appears to be part of a series, note patterns or changes

Be thorough and specific. Provide actionable insights about what has been done or what is happening."""
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Analyze this image in extensive detail. Describe everything you observe and provide comprehensive instructions or explanations about what has been done or what is happening."
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{mime_type};base64,{base64_image}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=2000,
                temperature=0.7
            )
            
            analysis = response.choices[0].message.content
            
            return {
                'success': True,
                'image_path': str(image_path),
                'image_name': image_path.name,
                'timestamp': datetime.now().isoformat(),
                'analysis': analysis,
                'model': self.model,
                'tokens_used': response.usage.total_tokens
            }
            
        except Exception as e:
            print(f"Error analyzing image {image_path.name}: {str(e)}")
            return {
                'success': False,
                'image_path': str(image_path),
                'image_name': image_path.name,
                'timestamp': datetime.now().isoformat(),
                'error': str(e)
            }

    def save_analysis(self, result: Dict):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_name = Path(result['image_name']).stem
        
        output_file = self.output_directory / f"{image_name}_{timestamp}_analysis.txt"
        json_file = self.output_directory / f"{image_name}_{timestamp}_analysis.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Image Analysis Report\n")
            f.write(f"{'=' * 80}\n\n")
            f.write(f"Image: {result['image_name']}\n")
            f.write(f"Analyzed: {result['timestamp']}\n")
            f.write(f"Model: {result['model']}\n")
            f.write(f"\n{'=' * 80}\n\n")
            
            if result['success']:
                f.write("DETAILED ANALYSIS:\n\n")
                f.write(result['analysis'])
                f.write(f"\n\n{'=' * 80}\n")
                f.write(f"Tokens used: {result.get('tokens_used', 'N/A')}\n")
            else:
                f.write(f"ERROR: {result['error']}\n")
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"Analysis saved to: {output_file}")

    def scan_for_new_images(self) -> List[Path]:
        new_images = []
        
        for file_path in self.watch_directory.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in self.supported_formats:
                if str(file_path) not in self.processed_images:
                    new_images.append(file_path)
        
        return sorted(new_images, key=lambda x: x.stat().st_mtime)

    def process_image(self, image_path: Path):
        result = self.analyze_image(image_path)
        self.save_analysis(result)
        
        self.processed_images.add(str(image_path))
        self._save_processed_images()

    def run_continuous(self):
        print(f"Image Analysis Agent Started")
        print(f"Watching directory: {self.watch_directory}")
        print(f"Output directory: {self.output_directory}")
        print(f"Supported formats: {', '.join(self.supported_formats)}")
        print(f"Check interval: {self.check_interval} seconds")
        print(f"Model: {self.model}")
        print(f"\nMonitoring for new images... Press Ctrl+C to stop.\n")
        
        try:
            while True:
                new_images = self.scan_for_new_images()
                
                if new_images:
                    print(f"\nFound {len(new_images)} new image(s) to process")
                    for image_path in new_images:
                        self.process_image(image_path)
                
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            print("\n\nAgent stopped by user")
            print(f"Total images processed: {len(self.processed_images)}")

    def run_once(self):
        print(f"Image Analysis Agent - Single Run Mode")
        print(f"Scanning directory: {self.watch_directory}\n")
        
        new_images = self.scan_for_new_images()
        
        if not new_images:
            print("No new images found to process")
            return
        
        print(f"Found {len(new_images)} image(s) to process\n")
        
        for image_path in new_images:
            self.process_image(image_path)
        
        print(f"\nProcessing complete. Analyzed {len(new_images)} image(s)")
