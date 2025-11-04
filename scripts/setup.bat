@echo off

echo Setting up Image Analysis Agent...

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo WARNING: Please edit .env and add your OpenAI API key!
    echo.
)

echo Creating default directories...
if not exist "input_images" mkdir input_images
if not exist "analysis_output" mkdir analysis_output

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Edit .env and add your OPENAI_API_KEY
echo 2. Place images in the 'input_images' directory
echo 3. Run: python agent.py
echo.
echo For help: python agent.py --help

pause
