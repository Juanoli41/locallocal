#!/usr/bin/env python3
"""
Server startup script for LocalLocal AI Chat
This script starts the FastAPI server for the web UI
"""

import uvicorn
import logging
from app import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting LocalLocal AI Chat Server...")
    logger.info("The application will be available at: http://localhost:8000")
    logger.info("Press Ctrl+C to stop the server")
    
    # Start the server
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="info"
    )