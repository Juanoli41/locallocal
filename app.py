from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import logging
import random
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LocalLocal AI Chat", description="Chat with AI models locally")

# Setup templates
templates = Jinja2Templates(directory="templates")

class MockModelManager:
    """Mock model manager that simulates AI responses without heavy dependencies"""
    
    def __init__(self):
        self.device = "cpu"
        self.models_loaded = True
        logger.info("Mock AI models initialized successfully!")
        
    def generate_gemma_response(self, user_input: str) -> str:
        """Generate intelligent responses that actually answer questions"""
        time.sleep(1)  # Simulate processing time
        
        query = user_input.lower().strip()
        
        # Greetings
        if any(word in query for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
            return "Hello! I'm Gemma, an AI assistant. I'm here to help answer your questions, provide explanations, assist with coding, creative writing, and much more. What would you like to know?"
        
        # Geography and Facts
        elif 'states' in query and ('united states' in query or 'usa' in query or 'america' in query):
            return "The United States has 50 states. This has been the case since Hawaii became the 50th state in 1959. The states range from Alaska (the largest) to Rhode Island (the smallest by area), and each state has its own government while being part of the federal system."
        
        elif 'capital' in query and ('usa' in query or 'united states' in query or 'america' in query):
            return "The capital of the United States is Washington, D.C. (District of Columbia). It was established as the nation's capital in 1790 and is located between Maryland and Virginia along the Potomac River."
        
        elif 'population' in query and ('world' in query or 'earth' in query):
            return "The world population is approximately 8 billion people as of 2024. This number grows by roughly 70-80 million people per year, though the growth rate has been slowing in recent decades."
        
        # Science and Math
        elif 'speed of light' in query:
            return "The speed of light in a vacuum is approximately 299,792,458 meters per second (or about 186,282 miles per second). This is one of the fundamental constants of physics and represents the maximum speed at which information can travel in the universe."
        
        elif any(word in query for word in ['2+2', '2 + 2', 'two plus two']):
            return "2 + 2 equals 4. This is a basic arithmetic operation where we're adding two identical positive integers."
        
        elif 'photosynthesis' in query:
            return "Photosynthesis is the process by which plants and some bacteria convert light energy (usually from the sun) into chemical energy stored in glucose. The basic equation is: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂. This process is crucial for life on Earth as it produces oxygen and forms the base of most food chains."
        
        # Technology and Programming
        elif 'python' in query and any(word in query for word in ['programming', 'language', 'code']):
            return "Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum and first released in 1991, Python is widely used for web development, data science, artificial intelligence, automation, and many other applications. Its philosophy emphasizes code readability and simplicity."
        
        elif 'javascript' in query:
            return "JavaScript is a dynamic, high-level programming language primarily used for web development. It enables interactive web pages and is an essential part of web applications alongside HTML and CSS. JavaScript can also be used for server-side development (Node.js), mobile apps, and desktop applications."
        
        elif 'html' in query:
            return "HTML (HyperText Markup Language) is the standard markup language for creating web pages. It uses tags to structure content, define elements like headings, paragraphs, links, and images. HTML provides the basic building blocks of web pages, which are then styled with CSS and made interactive with JavaScript."
        
        # History
        elif 'world war' in query and ('2' in query or 'two' in query or 'ii' in query):
            return "World War II lasted from 1939 to 1945 and was the deadliest conflict in human history. It involved most of the world's nations and resulted in 70-85 million deaths. The war ended with the surrender of Germany in May 1945 and Japan in September 1945, following the atomic bombings of Hiroshima and Nagasaki."
        
        elif 'moon landing' in query:
            return "The first human moon landing occurred on July 20, 1969, during NASA's Apollo 11 mission. Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon, while Michael Collins orbited above in the command module. Armstrong's famous words were: 'That's one small step for man, one giant leap for mankind.'"
        
        # Health and Biology
        elif 'dna' in query:
            return "DNA (Deoxyribonucleic Acid) is the hereditary material in most living organisms. It contains the genetic instructions for the development, functioning, and reproduction of all known living things. DNA is structured as a double helix and is composed of four nucleotide bases: Adenine (A), Thymine (T), Guanine (G), and Cytosine (C)."
        
        # Weather (general info)
        elif any(word in query for word in ['weather', 'temperature', 'rain', 'snow']):
            return "I don't have access to real-time weather data, but I can explain weather concepts! Weather is the atmospheric conditions at a specific place and time, including temperature, humidity, precipitation, wind, and atmospheric pressure. For current weather information, I'd recommend checking a weather service like weather.com or your local meteorological service."
        
        # Time and Date
        elif 'what time' in query or 'current time' in query:
            return "I don't have access to real-time information, so I can't tell you the current time. However, you can check the time on your device's clock, or search 'current time' in your web browser to get the accurate local time."
        
        # Creative requests
        elif any(word in query for word in ['joke', 'funny', 'humor']):
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the programmer quit his job? Because he didn't get arrays! (a raise)",
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What's the best thing about Switzerland? I don't know, but the flag is a big plus."
            ]
            return f"Here's a joke for you: {random.choice(jokes)}"
        
        elif 'story' in query or 'tale' in query:
            return "Once upon a time, in a digital realm filled with endless possibilities, there lived an AI assistant who loved helping people learn and explore new ideas. Every question was an adventure, and every answer was a step toward greater understanding. What kind of story would you like me to help create or tell you about?"
        
        # General help
        elif any(word in query for word in ['help', 'assist', 'what can you do']):
            return """I can help you with many things! Here are some examples:
• Answer factual questions (geography, science, history, math)
• Explain concepts and provide definitions
• Help with programming and technology questions
• Provide creative content like jokes and stories
• Give explanations about various topics
• Assist with learning and understanding new subjects

What would you like to know about?"""
        
        # Default intelligent response
        else:
            return f"""I understand you're asking about '{user_input}'. While I aim to be helpful, I might not have specific information about this particular topic in my current knowledge base. 

Could you provide a bit more context or rephrase your question? I'm knowledgeable about topics like:
- Science and mathematics
- Geography and history  
- Technology and programming
- General knowledge and facts

I'm here to help with explanations, definitions, and answering questions within my capabilities!"""
    
    def generate_router_response(self, user_input: str) -> str:
        """Generate intelligent routing analysis"""
        time.sleep(0.5)  # Simulate processing time
        
        query = user_input.lower().strip()
        
        # Technical/Programming queries
        if any(word in query for word in ['code', 'programming', 'python', 'javascript', 'html', 'css', 'algorithm']):
            return f"ROUTING ANALYSIS: Query classified as TECHNICAL_PROGRAMMING\nConfidence: 94%\nReasoning: Contains programming-related keywords\nRecommended Handler: Code Assistant with syntax highlighting and debugging capabilities\nExpected Response Type: Technical explanation with examples"
        
        # Scientific/Mathematical queries  
        elif any(word in query for word in ['math', 'calculate', 'equation', 'formula', 'science', 'physics', 'chemistry', 'biology']):
            return f"ROUTING ANALYSIS: Query classified as SCIENTIFIC_MATHEMATICAL\nConfidence: 91%\nReasoning: Detected scientific or mathematical concepts\nRecommended Handler: STEM Knowledge Base with calculation support\nExpected Response Type: Factual explanation with formulas/data"
        
        # Geography/Facts queries
        elif any(word in query for word in ['states', 'country', 'capital', 'population', 'geography', 'history']):
            return f"ROUTING ANALYSIS: Query classified as FACTUAL_KNOWLEDGE\nConfidence: 89%\nReasoning: Requesting specific factual information\nRecommended Handler: Encyclopedia/Facts Database\nExpected Response Type: Precise factual answer with context"
        
        # Creative requests
        elif any(word in query for word in ['joke', 'story', 'creative', 'write', 'poem', 'funny']):
            return f"ROUTING ANALYSIS: Query classified as CREATIVE_CONTENT\nConfidence: 86%\nReasoning: Request for creative or entertainment content\nRecommended Handler: Creative Writing Engine\nExpected Response Type: Original creative content"
        
        # Real-time data requests
        elif any(word in query for word in ['weather', 'time', 'current', 'now', 'today', 'temperature']):
            return f"ROUTING ANALYSIS: Query classified as REALTIME_DATA_REQUEST\nConfidence: 93%\nReasoning: Requires current/live information\nRecommended Handler: External API Service (Weather/Time)\nExpected Response Type: Current data with disclaimer about API access"
        
        # Greeting/Social
        elif any(word in query for word in ['hello', 'hi', 'hey', 'good morning', 'how are you']):
            return f"ROUTING ANALYSIS: Query classified as SOCIAL_GREETING\nConfidence: 95%\nReasoning: Standard conversational greeting detected\nRecommended Handler: Conversational AI with personality\nExpected Response Type: Friendly greeting with capability overview"
        
        # Help/Meta queries
        elif any(word in query for word in ['help', 'what can you do', 'assist', 'support']):
            return f"ROUTING ANALYSIS: Query classified as META_ASSISTANCE\nConfidence: 92%\nReasoning: User requesting information about AI capabilities\nRecommended Handler: Help System with feature documentation\nExpected Response Type: Comprehensive capability list with examples"
        
        # Default classification
        else:
            return f"ROUTING ANALYSIS: Query classified as GENERAL_INQUIRY\nConfidence: 76%\nReasoning: Broad topic that doesn't match specific categories\nRecommended Handler: General Knowledge Assistant\nExpected Response Type: Contextual response with request for clarification if needed"

# Initialize model manager
model_manager = MockModelManager()

# Startup logging is handled in the main block

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: Request, user_input: str = Form(...), model_choice: str = Form(...)):
    """Handle chat requests"""
    if not user_input.strip():
        response = "Please enter a message."
    else:
        try:
            logger.info(f"Processing request with model: {model_choice}")
            
            if model_choice == "gemma":
                response = model_manager.generate_gemma_response(user_input)
            elif model_choice == "router":
                response = model_manager.generate_router_response(user_input)
            elif model_choice == "both":
                # First get routing decision
                router_response = model_manager.generate_router_response(user_input)
                # Then use gemma for final response with routing context
                gemma_input = f"Based on this routing analysis, please provide a helpful response to the user's original question: '{user_input}'"
                gemma_response = model_manager.generate_gemma_response(user_input)
                response = f"🤖 Router Analysis:\n{router_response}\n\n💬 Gemma Response:\n{gemma_response}"
            else:
                response = "Invalid model choice."
                
            logger.info(f"Generated response for: {user_input[:50]}...")
            
        except Exception as e:
            logger.error(f"Error in chat endpoint: {e}")
            response = f"Sorry, there was an error processing your request: {str(e)}"
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "user_input": user_input,
        "response": response,
        "model_choice": model_choice
    })

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy", 
        "models_loaded": model_manager.models_loaded,
        "device": model_manager.device,
        "mode": "mock_ai_simulation"
    }

@app.get("/api/models")
async def get_models():
    """API endpoint to get available models"""
    return {
        "models": [
            {
                "id": "gemma",
                "name": "Gemma 2-2B",
                "description": "Google's instruction-tuned model (Simulated)",
                "status": "ready"
            },
            {
                "id": "router", 
                "name": "Arch Router 1.5B",
                "description": "Katanemo's routing model (Simulated)",
                "status": "ready"
            },
            {
                "id": "both",
                "name": "Pipeline Mode",
                "description": "Router + Gemma pipeline (Simulated)",
                "status": "ready"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting LocalLocal AI Chat server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)