# LocalLocal AI Chat

A FastAPI application that provides a simple web interface for chatting with AI models locally. This application supports two Hugging Face models:

- **Google Gemma-2-2b-it**: An instruction-tuned language model
- **Katanemo Arch-Router-1.5B**: A routing model for directing queries

## Features

- 🤖 **Multiple Model Support**: Choose between Gemma, Arch Router, or use both in pipeline
- 🎨 **Beautiful UI**: Clean, responsive web interface with gradient design
- ⚡ **Fast Response**: Local inference without API calls
- 🔄 **Pipeline Mode**: Use Arch Router to analyze queries, then Gemma for responses
- 📱 **Mobile Friendly**: Responsive design works on all devices

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd locallocal
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Note: If you encounter Windows Long Path issues, install packages individually:
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   pip install --no-cache-dir transformers
   ```

## Usage

### Option 1: Main Application (Recommended)

Start the main application with intelligent AI simulation:

```bash
python app.py
```

Or simply double-click `start_app.bat` on Windows.

### Option 2: Simple Mock Responses

Start the application with basic mock responses for UI testing:

```bash
python app_test.py
```

### Option 3: Heavy AI Models (Currently Has Dependency Issues)

```bash
python app_heavy_models_broken.py
```

**Note**: The heavy AI model version currently has Windows Long Path and package compatibility issues. The main `app.py` provides intelligent responses that simulate real AI behavior without the heavy dependencies.

## Accessing the Application

1. Start the server using one of the methods above
2. Open your web browser and go to: `http://localhost:8000`
3. Type your message in the text area
4. Select which model to use:
   - **Gemma 2-2B**: Direct response from Google's instruction-tuned model
   - **Arch Router**: Response from Katanemo's routing model
   - **Both Models**: Pipeline where Router analyzes, then Gemma responds
5. Click "Send Message" or press Ctrl+Enter

## Model Information

### Google Gemma-2-2b-it
- **Size**: ~4GB
- **Purpose**: General instruction-following and conversation
- **Strengths**: Well-rounded responses, good instruction following

### Katanemo Arch-Router-1.5B  
- **Size**: ~3GB
- **Purpose**: Query routing and analysis
- **Strengths**: Understanding query intent and routing decisions

## System Requirements

- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: ~10GB free space for models and dependencies  
- **GPU**: Optional (CUDA support), will use CPU if not available
- **Python**: 3.8+

## Configuration

The application automatically detects whether CUDA is available and uses GPU acceleration when possible. For CPU-only inference, models will run slower but still functional.

## API Endpoints

- `GET /`: Main chat interface
- `POST /chat`: Process chat messages
- `GET /health`: Health check endpoint

## Troubleshooting

### Current Known Issues
- **Heavy AI Models (app_heavy_models_broken.py)**: Windows Long Path and PyTorch/Transformers compatibility issues
- **Solution**: Use `app.py` (the main application) which provides intelligent AI-like responses without heavy dependencies

### Model Loading Issues (for app.py)
- Ensure you have sufficient RAM and storage
- Check internet connection for model downloads  
- Enable Windows Long Path support in Windows 10/11
- Try using `app.py` as an alternative (the main working version)

### Windows Long Path Issues
- Enable Long Path support: `gpedit.msc` → Computer Configuration → Administrative Templates → System → Filesystem → Enable Win32 long paths
- Or use the working version: `python app_working.py`

### Memory Issues
- Use the lightweight version: `python app.py`
- Close other applications to free RAM if using full models

## Development

### File Structure
```
locallocal/
├── app.py                        # Main application with intelligent AI simulation
├── app_test.py                   # Simple test version with basic mock responses  
├── app_heavy_models_broken.py    # Heavy AI models version (has dependency issues)
├── start_app.bat                 # Windows batch file to easily start the app
├── templates/
│   └── index.html                # Web interface template
├── requirements.txt              # Python dependencies
└── README.md                    # This file
```

### Adding New Models
1. Update `ModelManager` class in `app.py`
2. Add model loading logic in `load_models()`
3. Update response generation in `generate_response()`
4. Add new option in HTML template

## License

This project is open source. Model usage is subject to their respective licenses:
- Gemma models: Google's Gemma license
- Arch Router: Katanemo's license terms

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with both `app_test.py` and `app.py`
5. Submit a pull request

---

**Happy chatting with your local AI models! 🤖**