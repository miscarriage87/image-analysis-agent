#!/bin/bash

echo "Setting up Image Analysis Agent..."

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo ""
    echo "⚠️  Please edit .env and add your OpenAI API key!"
    echo ""
fi

echo "Creating default directories..."
mkdir -p input_images
mkdir -p analysis_output

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your OPENAI_API_KEY"
echo "2. Place images in the 'input_images' directory"
echo "3. Run: python agent.py"
echo ""
echo "For help: python agent.py --help"
