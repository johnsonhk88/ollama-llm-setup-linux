docker run -d --name ollama -p 11434:11434 -v ollama_storage:/root/.ollama \
  ollama/ollama:latest