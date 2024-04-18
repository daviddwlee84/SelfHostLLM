import streamlit as st
import ollama
import pandas as pd

st.set_page_config("Ollama Demo")
st.title("Ollama Demo")

host_url = st.text_input("Ollama URL", "http://localhost:11434")

"""
Here are some example models that can be downloaded:

| Model              | Parameters | Size  | Download            |
| ------------------ | ---------- | ----- | ------------------- |
| Llama 2            | 7B         | 3.8GB | `llama2`            |
| Mistral            | 7B         | 4.1GB | `mistral`           |
| Dolphin Phi        | 2.7B       | 1.6GB | `dolphin-phi`       |
| Phi-2              | 2.7B       | 1.7GB | `phi`               |
| Neural Chat        | 7B         | 4.1GB | `neural-chat`       |
| Starling           | 7B         | 4.1GB | `starling-lm`       |
| Code Llama         | 7B         | 3.8GB | `codellama`         |
| Llama 2 Uncensored | 7B         | 3.8GB | `llama2-uncensored` |
| Llama 2 13B        | 13B        | 7.3GB | `llama2:13b`        |
| Llama 2 70B        | 70B        | 39GB  | `llama2:70b`        |
| Orca Mini          | 3B         | 1.9GB | `orca-mini`         |
| LLaVA              | 7B         | 4.5GB | `llava`             |
| Gemma              | 2B         | 1.4GB | `gemma:2b`          |
| Gemma              | 7B         | 4.8GB | `gemma:7b`          |
| Solar              | 10.7B      | 6.1GB | `solar`             |
"""

model_list = {
    "llama2": "Llama 2",
    "llama2-uncensored": "Llama 2 Uncensored",
    "llama2:13b": "Llama 2 13B",
    "llama2:70b": "Llama 2 70B",
    "codellama": "Code Llama",
    "mistral": "Mistral",
    "dolphin-phi": "Dolphin Phi",
    "phi": "Phi-2",
    "neural-chat": "Neural Chat",
    "starling-lm": "Starling",
    "orca-mini": "Orca Mini",
    "llava": "LLaVA",
    "gemma:2b": "Gemma",
    "gemma:7b": "Gemma",
    "solar": "Solar",
}

model_name = st.selectbox(
    "Model", options=model_list.keys(), format_func=lambda x: model_list[x]
)


models = st.empty()
models_df = pd.DataFrame(ollama.list()["models"])
models.dataframe(models_df)

avail_models = set(models_df["name"].str.split(":").str[0])

if model_name is None:
    st.warning(
        f"Please select a model first. Current available models are {avail_models}."
    )
    st.stop()

if model_name not in avail_models:
    # progress = ollama.pull(model_name, stream=True)
    # for p in progress:
    #     print(p)
    #     # print(f"{p['completed'] / p['total'] = }")
    with st.spinner(f"Pulling model {model_name}..."):
        ollama.pull(model_name)
    # Update available model list after downloading
    models.dataframe(pd.DataFrame(ollama.list()["models"]))

with st.expander("Model Detail"):
    st.json(ollama.show(model_name))

client = ollama.Client(host=host_url)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat(
            model=model_name,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        # Response json
        # {
        #     "model": "llama2",
        #     "created_at": "2024-04-18T06:12:25.939568316Z",
        #     "message": {
        #         "role": "assistant",
        #         "content": '{"name": "John", "age": 30, " occupation": "Software Engineer"}',  # json mode
        #         "content": "Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?",  # normal mode
        #     },
        #     "done": True,
        #     "total_duration": 3657335949,
        #     "load_duration": 2350525,
        #     "prompt_eval_duration": 143723000,
        #     "eval_count": 23,
        #     "eval_duration": 3376456000,
        # }
        response = st.write_stream((item["message"]["content"] for item in stream))
    st.session_state.messages.append({"role": "assistant", "content": response})
