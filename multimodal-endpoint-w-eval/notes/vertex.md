Skip to main content

[ **🚅 LiteLLM**](/)[Docs](/docs/)

[GitHub](https://github.com/BerriAI/litellm)[Discord](https://discord.com/invite/wuPM9dRgDw)

I'm Confused

  * [LiteLLM - Getting Started](/docs/)
  * [Completion()](/docs/completion)

  * [Embedding() & Moderation()](/docs/embedding/supported_embedding)

  * [Supported Models & Providers](/docs/providers)

    * [OpenAI](/docs/providers/openai)
    * [OpenAI-Compatible Endpoints](/docs/providers/openai_compatible)
    * [Azure OpenAI](/docs/providers/azure)
    * [Huggingface](/docs/providers/huggingface)
    * [Ollama](/docs/providers/ollama)
    * [VertexAI - Google [Gemini]](/docs/providers/vertex)
    * [PaLM API - Google](/docs/providers/palm)
    * [Mistral AI API](/docs/providers/mistral)
    * [Anthropic](/docs/providers/anthropic)
    * [AWS Sagemaker](/docs/providers/aws_sagemaker)
    * [AWS Bedrock](/docs/providers/bedrock)
    * [Anyscale](/docs/providers/anyscale)
    * [Perplexity AI (pplx-api)](/docs/providers/perplexity)
    * [VLLM](/docs/providers/vllm)
    * [DeepInfra](/docs/providers/deepinfra)
    * [AI21](/docs/providers/ai21)
    * [NLP Cloud](/docs/providers/nlp_cloud)
    * [Replicate](/docs/providers/replicate)
    * [Cohere](/docs/providers/cohere)
    * [Together AI](/docs/providers/togetherai)
    * [Aleph Alpha](/docs/providers/aleph_alpha)
    * [Baseten](/docs/providers/baseten)
    * [OpenRouter](/docs/providers/openrouter)
    * [Custom API Server (OpenAI Format)](/docs/providers/custom_openai_proxy)
    * [Petals](/docs/providers/petals)
  * [💥 OpenAI Proxy Server](/docs/simple_proxy)

  * [Router - Load Balancing, Fallbacks](/docs/routing)
  * [Rules](/docs/rules)
  * [Setting API Keys, Base, Version](/docs/set_keys)
  * [Budget Manager](/docs/budget_manager)
  * [Secret Manager](/docs/secret)
  * [Completion Token Usage & Cost](/docs/completion/token_usage)
  * [Tutorials](/docs/tutorials/azure_openai)

  * [Logging & Observability](/docs/debugging/local_debugging)

  * [Caching](/docs/caching)

  * [LangChain, LlamaIndex Integration](/docs/langchain/)

  * [Extras](/docs/extras/contributing)

  * [Migration Guide - LiteLLM v1.0.0+](/docs/migration)
  * [Support & Talk with founders](/docs/troubleshoot)

  * [](/)
  * [Supported Models & Providers](/docs/providers)
  * VertexAI - Google [Gemini]

On this page

# VertexAI - Google [Gemini]

[![Open In Colab](https://colab.research.google.com/assets/colab-
badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/liteLLM_VertextAI_Example.ipynb)

## Pre-requisites​

  * `pip install google-cloud-aiplatform`
  * Authentication: 
    * run `gcloud auth application-default login` See [Google Cloud Docs](https://cloud.google.com/docs/authentication/external/set-up-adc)
    * Alternatively you can set `application_default_credentials.json`

## Sample Usage​

    
    
    import litellm  
    litellm.vertex_project = "hardy-device-38811" # Your Project ID  
    litellm.vertex_location = "us-central1"  # proj location  
      
    response = completion(model="gemini-pro", messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}])  
    

## Set Vertex Project & Vertex Location​

All calls using Vertex AI require the following parameters:

  * Your Project ID

    
    
    import os, litellm   
      
    # set via env var  
    os.environ["VERTEXAI_PROJECT"] = "hardy-device-38811" # Your Project ID`  
      
    ### OR ###  
      
    # set directly on module   
    litellm.vertex_project = "hardy-device-38811" # Your Project ID`  
    

  * Your Project Location

    
    
    import os, litellm   
      
    # set via env var  
    os.environ["VERTEXAI_LOCATION"] = "us-central1 # Your Location  
      
    ### OR ###  
      
    # set directly on module   
    litellm.vertex_location = "us-central1 # Your Location  
    

## Gemini Pro​

Model Name| Function Call  
---|---  
gemini-pro| `completion('gemini-pro', messages)`  
  
## Gemini Pro Vision​

Model Name| Function Call  
---|---  
gemini-pro-vision| `completion('gemini-pro-vision', messages)`  
  
#### Using Gemini Pro Vision​

Call `gemini-pro-vision` in the same input/output format as OpenAI
[`gpt-4-vision`](https://docs.litellm.ai/docs/providers/openai#openai-vision-
models)

LiteLLM Supports the following image types passed in `url`

  * Images with Cloud Storage URIs - gs://cloud-samples-data/generative-ai/image/boats.jpeg
  * Images with direct links - <https://storage.googleapis.com/github-repo/img/gemini/intro/landmark3.jpg>
  * Videos with Cloud Storage URIs - <https://storage.googleapis.com/github-repo/img/gemini/multimodality_usecases_overview/pixel8.mp4>

**Example Request**

    
    
     import litellm  
      
    response = litellm.completion(  
      model = "vertex_ai/gemini-pro-vision",  
      messages=[  
          {  
              "role": "user",  
              "content": [  
                              {  
                                  "type": "text",  
                                  "text": "Whats in this image?"  
                              },  
                              {  
                                  "type": "image_url",  
                                  "image_url": {  
                                  "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"  
                                  }  
                              }  
                          ]  
          }  
      ],  
    )  
    print(response)  
    

## Chat Models​

Model Name| Function Call  
---|---  
chat-bison-32k| `completion('chat-bison-32k', messages)`  
chat-bison| `completion('chat-bison', messages)`  
chat-bison@001| `completion('chat-bison@001', messages)`  
  
## Code Chat Models​

Model Name| Function Call  
---|---  
codechat-bison| `completion('codechat-bison', messages)`  
codechat-bison-32k| `completion('codechat-bison-32k', messages)`  
codechat-bison@001| `completion('codechat-bison@001', messages)`  
  
## Text Models​

Model Name| Function Call  
---|---  
text-bison| `completion('text-bison', messages)`  
text-bison@001| `completion('text-bison@001', messages)`  
  
## Code Text Models​

Model Name| Function Call  
---|---  
code-bison| `completion('code-bison', messages)`  
code-bison@001| `completion('code-bison@001', messages)`  
code-gecko@001| `completion('code-gecko@001', messages)`  
code-gecko@latest| `completion('code-gecko@latest', messages)`  
  
[PreviousOllama](/docs/providers/ollama)[NextPaLM API -
Google](/docs/providers/palm)

  * Pre-requisites
  * Sample Usage
  * Set Vertex Project & Vertex Location
  * Gemini Pro
  * Gemini Pro Vision
  * Chat Models
  * Code Chat Models
  * Text Models
  * Code Text Models

Docs

  * [Tutorial](/docs/index)

Community

  * [Discord](https://discord.com/invite/wuPM9dRgDw)
  * [Twitter](https://twitter.com/LiteLLM)

More

  * [GitHub](https://github.com/BerriAI/litellm/)

Copyright © 2023 liteLLM

