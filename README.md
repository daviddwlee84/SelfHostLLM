# Self-Host LLM

Learning to self-host LLM on local or cloud

- [Reddit - LocalLlama](https://www.reddit.com/r/LocalLLaMA/)

## Getting Started

1. Install Ollama: `curl -fsSL https://ollama.com/install.sh | sh` (Windows: [Download Ollama on Windows](https://ollama.com/download/windows))
2. Install Python dependencies: `pip install -r requirements.txt`
3. Start Streamlit UI: `streamlit run ./Overview.py`

## LLM Operations and Support Tools

> List support by LangChain: [LLMs | 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/llms/#features-natively-supported)

### Ollama (recommend)

> Easier to run

- [Ollama](https://ollama.com/)
  - [OpenAI compatibility · Ollama Blog](https://ollama.com/blog/openai-compatibility)
  - [Windows preview · Ollama Blog](https://ollama.com/blog/windows-preview)
    - [Download Ollama on Windows](https://ollama.com/download/windows)
  - [Ollama and LangChain: Run LLMs locally | by Abonia Sojasingarayar | Feb, 2024 | Medium](https://medium.com/@abonia/ollama-and-langchain-run-llms-locally-900931914a46)
- GitHub
  - [ollama/ollama: Get up and running with Llama 2, Mistral, Gemma, and other large language models.](https://github.com/ollama/ollama)
  - [ollama/ollama-python: Ollama Python library](https://github.com/ollama/ollama-python)
- LangChain
  - [Ollama | 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/llms/ollama/)
  - [ChatOllama | 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/chat/ollama/)
    - [OllamaFunctions | 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/chat/ollama_functions/)

```bash
curl -fsSL https://ollama.com/install.sh | sh
# You should have ollama.service running

ollama run llama2
ollama run llama2-uncensored
```

> Copy existing Ollama to another system
> 
> `/usr/local/bin/ollama`
> 
> ```ini
> # /etc/systemd/system/ollama.service
> 
> [Unit]
> Description=Ollama Service
> After=network-online.target
> 
> [Service]
> ExecStart=/usr/local/bin/ollama serve
> User=ollama
> Group=ollama
> Restart=always
> RestartSec=3
> Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"
> 
> [Install]
> WantedBy=default.target
> ```
> 
> ```bash
> sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama
> sudo usermod -a -G render ollama
> sudo usermod -a -G video ollama
> sudo usermod -a -G ollama $(whoami)
> 
> sudo systemctl daemon-reload
> sudo systemctl enable ollama
> sudo systemctl restart ollama
> sudo systemctl status ollama
> ```

### llama.cpp

> Launch earlier

- [ggerganov/llama.cpp: LLM inference in C/C++](https://github.com/ggerganov/llama.cpp)
- [Llama.cpp | 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/llms/llamacpp/)
- [abetlen/llama-cpp-python: Python bindings for llama.cpp](https://github.com/abetlen/llama-cpp-python)

### alpaca.cpp (not maintaining)

- [antimatter15/alpaca.cpp: Locally run an Instruction-Tuned Chat-Style LLM](https://github.com/antimatter15/alpaca.cpp)

## Other

### Free API

- [aurora-develop/aurora](https://github.com/aurora-develop/aurora)
- [xqdoo00o/ChatGPT-to-API: Scalable unofficial ChatGPT API for production.](https://github.com/xqdoo00o/ChatGPT-to-API)
  - [acheong08/ChatGPT-to-API: Scalable unofficial ChatGPT API for production.](https://github.com/acheong08/ChatGPT-to-API) (archived)
- [xtekky/gpt4free: The official gpt4free repository | various collection of powerful language models](https://github.com/xtekky/gpt4free)

### CLI Tools

- [taketwo/llm-ollama: LLM plugin providing access to local Ollama models using HTTP API](https://github.com/taketwo/llm-ollama)
- [LLM: A CLI utility and Python library for interacting with Large Language Models](https://llm.datasette.io/en/stable/)
