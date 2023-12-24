---
description: 'Set model list, apibase, apikey, temperature & proxy
  server settings (master-key) on the config.yaml.'
docsearch:docusaurus_tag: 'docs-default-current'
docsearch:language: en
docsearch:version: current
docusaurus_locale: en
docusaurus_tag: 'docs-default-current'
docusaurus_version: current
generator: Docusaurus v2.4.1
lang: en
title: 'Proxy Config.yaml \| liteLLM'
twitter:card: summary\_large\_image
twitter:image: 'https://litellm.vercel.app/img/docusaurus-social-card.png'
viewport: 'width=device-width,initial-scale=1'
---

::: {#__docusaurus}
::: {role="region" aria-label="Skip to main content"}
[Skip to main
content](#__docusaurus_skipToContent_fallback){.skipToContent_fXgn}
:::

::: {.navbar__inner}
::: {.navbar__items}
[**🚅 LiteLLM**](/){.navbar__brand}[Docs](/docs/){.navbar__item
.navbar__link .navbar__link--active}
:::

::: {.navbar__items .navbar__items--right}
GitHub

Discord

::: {.navbar__item}
[I\'m Confused](#){.navbar__link}
:::

::: {.toggle_vylO .colorModeToggle_DEke}
:::

::: {.searchBox_ZlJk}
::: {.navbar__search}
[]{.search-icon aria-label="expand searchbar" role="button"
tabindex="0"}
:::
:::
:::
:::

::: {.navbar-sidebar__backdrop role="presentation"}
:::

::: {#__docusaurus_skipToContent_fallback .main-wrapper .mainWrapper_z2l0 .docsWrapper_BCFX}
::: {.docPage__5DB}
::: {.sidebarViewport_Xe31}
::: {.sidebar_njMd}
-   [LiteLLM - Getting Started](/docs/){.menu__link}

-   ::: {.menu__list-item-collapsible}
    [Completion()](/docs/completion){.menu__link .menu__link--sublist}
    :::

-   ::: {.menu__list-item-collapsible}
    [Embedding() &
    Moderation()](/docs/embedding/supported_embedding){.menu__link
    .menu__link--sublist .menu__link--sublist-caret}
    :::

-   ::: {.menu__list-item-collapsible}
    [Supported Models & Providers](/docs/providers){.menu__link
    .menu__link--sublist}
    :::

-   ::: {.menu__list-item-collapsible}
    [💥 OpenAI Proxy Server](/docs/simple_proxy){.menu__link
    .menu__link--sublist .menu__link--active}
    :::

    -   [Quick Start](/docs/proxy/quick_start){.menu__link}
    -   [Proxy Config.yaml](/docs/proxy/configs){.menu__link
        .menu__link--active}
    -   [Embeddings - /embeddings](/docs/proxy/embedding){.menu__link}
    -   [Load Balancing - Multiple Instances of 1
        model](/docs/proxy/load_balancing){.menu__link}
    -   [Key Management](/docs/proxy/virtual_keys){.menu__link}
    -   [Model Management](/docs/proxy/model_management){.menu__link}
    -   [Fallbacks, Retries, Timeouts,
        Cooldowns](/docs/proxy/reliability){.menu__link}
    -   [Health Checks](/docs/proxy/health){.menu__link}
    -   [Modify Incoming Data](/docs/proxy/call_hooks){.menu__link}
    -   [Caching](/docs/proxy/caching){.menu__link}
    -   [Logging - Custom Callbacks, OpenTelemetry, Langfuse,
        Sentry](/docs/proxy/logging){.menu__link}
    -   [CLI Arguments](/docs/proxy/cli){.menu__link}
    -   [🐳 Docker, Deploying LiteLLM
        Proxy](/docs/proxy/deploy){.menu__link}

-   [Router - Load Balancing, Fallbacks](/docs/routing){.menu__link}

-   [Rules](/docs/rules){.menu__link}

-   [Setting API Keys, Base, Version](/docs/set_keys){.menu__link}

-   [Budget Manager](/docs/budget_manager){.menu__link}

-   [Secret Manager](/docs/secret){.menu__link}

-   [Completion Token Usage &
    Cost](/docs/completion/token_usage){.menu__link}

-   ::: {.menu__list-item-collapsible}
    [Tutorials](/docs/tutorials/azure_openai){.menu__link
    .menu__link--sublist .menu__link--sublist-caret}
    :::

-   ::: {.menu__list-item-collapsible}
    [Logging &
    Observability](/docs/debugging/local_debugging){.menu__link
    .menu__link--sublist .menu__link--sublist-caret}
    :::

-   ::: {.menu__list-item-collapsible}
    [Caching](/docs/caching){.menu__link .menu__link--sublist}
    :::

-   ::: {.menu__list-item-collapsible}
    [LangChain, LlamaIndex Integration](/docs/langchain/){.menu__link
    .menu__link--sublist .menu__link--sublist-caret}
    :::

-   ::: {.menu__list-item-collapsible}
    [Extras](/docs/extras/contributing){.menu__link .menu__link--sublist
    .menu__link--sublist-caret}
    :::

-   [Migration Guide - LiteLLM v1.0.0+](/docs/migration){.menu__link}

-   [Support & Talk with founders](/docs/troubleshoot){.menu__link}
:::
:::

::: {.docMainContainer_gTbr role="main"}
::: {.container .padding-top--md .padding-bottom--lg}
::: {.row}
::: {.col .docItemCol_VOVn}
::: {.docItemContainer_Djhp}
-   
-   [[💥 OpenAI Proxy
    Server]{itemprop="name"}](/docs/simple_proxy){.breadcrumbs__link}
-   [Proxy Config.yaml]{.breadcrumbs__link itemprop="name"}

::: {.tocCollapsible_ETCw .theme-doc-toc-mobile .tocMobile_ITEo}
On this page
:::

::: {.theme-doc-markdown .markdown}
Proxy Config.yaml
=================

Set model list, `api_base`, `api_key`, `temperature` & proxy server
settings (`master-key`) on the config.yaml.

  Param Name                Description
  ------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `model_list`              List of supported models on the server, with model-specific configs
  `router_settings`         litellm Router settings, example `routing_strategy="least-busy"` [**see all**](https://github.com/BerriAI/litellm/blob/6ef0e8485e0e720c0efa6f3075ce8119f2f62eea/litellm/router.py#L64)
  `litellm_settings`        litellm Module settings, example `litellm.drop_params=True`, `litellm.set_verbose=True`, `litellm.api_base`, `litellm.cache` [**see all**](https://github.com/BerriAI/litellm/blob/main/litellm/__init__.py)
  `general_settings`        Server settings, example setting `master_key: sk-my_special_key`
  `environment_variables`   Environment Variables example, `REDIS_HOST`, `REDIS_PORT`

**Complete List:** Check the Swagger UI docs on
`<your-proxy-url>/#/config.yaml` (e.g.
<http://0.0.0.0:8000/#/config.yaml>), for everything you can pass in the
config.yaml.

Quick Start[​](#quick-start "Direct link to Quick Start"){.hash-link} {#quick-start .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------

Set a model alias for your deployments.

In the `config.yaml` the model\_name parameter is the user-facing name
to use for your deployment.

In the config below requests with:

-   `model=vllm-models` will route to `openai/facebook/opt-125m`.
-   `model=gpt-3.5-turbo` will load balance between
    `azure/gpt-turbo-small-eu` and `azure/gpt-turbo-small-ca`

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
model_list:
  - model_name: gpt-3.5-turbo # user-facing model alias
    litellm_params: # all params accepted by litellm.completion() - https://docs.litellm.ai/docs/completion/input
      model: azure/gpt-turbo-small-eu
      api_base: https://my-endpoint-europe-berri-992.openai.azure.com/
      api_key: "os.environ/AZURE_API_KEY_EU" # does os.getenv("AZURE_API_KEY_EU")
      rpm: 6      # Rate limit for this deployment: in requests per minute (rpm)
  - model_name: bedrock-claude-v1 
    litellm_params:
      model: bedrock/anthropic.claude-instant-v1
  - model_name: gpt-3.5-turbo
    litellm_params:
      model: azure/gpt-turbo-small-ca
      api_base: https://my-endpoint-canada-berri992.openai.azure.com/
      api_key: "os.environ/AZURE_API_KEY_CA"
      rpm: 6
  - model_name: vllm-models
    litellm_params:
      model: openai/facebook/opt-125m # the `openai/` prefix tells litellm it's openai compatible
      api_base: http://0.0.0.0:8000
      rpm: 1440
    model_info: 
      version: 2

litellm_settings: # module level litellm settings - https://github.com/BerriAI/litellm/blob/main/litellm/__init__.py
  drop_params: True
  set_verbose: True

general_settings: 
  master_key: sk-1234 # [OPTIONAL] Only use this if you to require all calls to contain this key (Authorization: Bearer sk-1234)
```

::: {.buttonGroup__atx}
:::
:::
:::

#### Step 2: Start Proxy with config[​](#step-2-start-proxy-with-config "Direct link to Step 2: Start Proxy with config"){.hash-link} {#step-2-start-proxy-with-config .anchor .anchorWithStickyNavbar_LWe7}

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --config /path/to/config.yaml
```

::: {.buttonGroup__atx}
:::
:::
:::

### Using Proxy - Curl Request, OpenAI Package, Langchain, Langchain JS[​](#using-proxy---curl-request-openai-package-langchain-langchain-js "Direct link to Using Proxy - Curl Request, OpenAI Package, Langchain, Langchain JS"){.hash-link} {#using-proxy---curl-request-openai-package-langchain-langchain-js .anchor .anchorWithStickyNavbar_LWe7}

Calling a model group

::: {.tabs-container .tabList__CuJ}
-   Curl Request
-   Curl Request: Bedrock
-   OpenAI v1.0.0+
-   Langchain Python

::: {.margin-top--md}
::: {.tabItem_Ymn6 role="tabpanel"}
Sends request to model where `model_name=gpt-3.5-turbo` on config.yaml.

If multiple with `model_name=gpt-3.5-turbo` does [Load
Balancing](https://docs.litellm.ai/docs/proxy/load_balancing)

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
curl --location 'http://0.0.0.0:8000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ],
    }
'
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
Sends this request to model where `model_name=bedrock-claude-v1` on
config.yaml

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
curl --location 'http://0.0.0.0:8000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "bedrock-claude-v1",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ],
    }
'
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
import openai
client = openai.OpenAI(
    api_key="anything",
    base_url="http://0.0.0.0:8000"
)

# Sends request to model where `model_name=gpt-3.5-turbo` on config.yaml. 
response = client.chat.completions.create(model="gpt-3.5-turbo", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])

print(response)

# Sends this request to model where `model_name=bedrock-claude-v1` on config.yaml
response = client.chat.completions.create(model="bedrock-claude-v1", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])

print(response)
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(
        content="You are a helpful assistant that im using to make a test request to."
    ),
    HumanMessage(
        content="test from litellm. tell me why it's amazing in 1 sentence"
    ),
]

# Sends request to model where `model_name=gpt-3.5-turbo` on config.yaml. 
chat = ChatOpenAI(
    openai_api_base="http://0.0.0.0:8000",  # set openai base to the proxy
    model = "gpt-3.5-turbo",                
    temperature=0.1
)

response = chat(messages)
print(response)

# Sends request to model where `model_name=bedrock-claude-v1` on config.yaml. 
claude_chat = ChatOpenAI(
    openai_api_base="http://0.0.0.0:8000", # set openai base to the proxy
    model = "bedrock-claude-v1",                   
    temperature=0.1
)

response = claude_chat(messages)
print(response)
```

::: {.buttonGroup__atx}
:::
:::
:::
:::
:::
:::

Save Model-specific params (API Base, API Keys, Temperature, Headers etc.)[​](#save-model-specific-params-api-base-api-keys-temperature-headers-etc "Direct link to Save Model-specific params (API Base, API Keys, Temperature, Headers etc.)"){.hash-link} {#save-model-specific-params-api-base-api-keys-temperature-headers-etc .anchor .anchorWithStickyNavbar_LWe7}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use the config to save model-specific information like
api\_base, api\_key, temperature, max\_tokens, etc.

[**All input
params**](https://docs.litellm.ai/docs/completion/input#input-params-1)

**Step 1**: Create a `config.yaml` file

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
model_list:
  - model_name: gpt-4-team1
    litellm_params: # params for litellm.completion() - https://docs.litellm.ai/docs/completion/input#input---request-body
      model: azure/chatgpt-v-2
      api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
      api_version: "2023-05-15"
      azure_ad_token: eyJ0eXAiOiJ
  - model_name: gpt-4-team2
    litellm_params:
      model: azure/gpt-4
      api_key: sk-123
      api_base: https://openai-gpt-4-test-v-2.openai.azure.com/
  - model_name: mistral-7b
    litellm_params:
      model: ollama/mistral
      api_base: your_ollama_api_base
      headers: {
        "HTTP-Referer": "litellm.ai",  
        "X-Title": "LiteLLM Server"
      }
```

::: {.buttonGroup__atx}
:::
:::
:::

**Step 2**: Start server with config

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --config /path/to/config.yaml
```

::: {.buttonGroup__atx}
:::
:::
:::

Load API Keys[​](#load-api-keys "Direct link to Load API Keys"){.hash-link} {#load-api-keys .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------

### Load API Keys from Environment[​](#load-api-keys-from-environment "Direct link to Load API Keys from Environment"){.hash-link} {#load-api-keys-from-environment .anchor .anchorWithStickyNavbar_LWe7}

If you have secrets saved in your environment, and don\'t want to expose
them in the config.yaml, here\'s how to load model-specific keys from
the environment.

::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
os.environ["AZURE_NORTH_AMERICA_API_KEY"] = "your-azure-api-key"
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
model_list:
  - model_name: gpt-4-team1
    litellm_params: # params for litellm.completion() - https://docs.litellm.ai/docs/completion/input#input---request-body
      model: azure/chatgpt-v-2
      api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
      api_version: "2023-05-15"
      api_key: os.environ/AZURE_NORTH_AMERICA_API_KEY
```

::: {.buttonGroup__atx}
:::
:::
:::

[**See
Code**](https://github.com/BerriAI/litellm/blob/c12d6c3fe80e1b5e704d9846b246c059defadce7/litellm/utils.py#L2366)

s/o to [\@David
Manouchehri](https://www.linkedin.com/in/davidmanouchehri/) for helping
with this.

### Load API Keys from Azure Vault[​](#load-api-keys-from-azure-vault "Direct link to Load API Keys from Azure Vault"){.hash-link} {#load-api-keys-from-azure-vault .anchor .anchorWithStickyNavbar_LWe7}

1.  Install Proxy dependencies

::: {.language-bash .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-bash .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ pip install litellm[proxy] litellm[extra_proxy]
```

::: {.buttonGroup__atx}
:::
:::
:::

2.  Save Azure details in your environment

::: {.language-bash .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-bash .codeBlock_bY9V .thin-scrollbar tabindex="0"}
export["AZURE_CLIENT_ID"]="your-azure-app-client-id"
export["AZURE_CLIENT_SECRET"]="your-azure-app-client-secret"
export["AZURE_TENANT_ID"]="your-azure-tenant-id"
export["AZURE_KEY_VAULT_URI"]="your-azure-key-vault-uri"
```

::: {.buttonGroup__atx}
:::
:::
:::

3.  Add to proxy config.yaml

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
model_list: 
    - model_name: "my-azure-models" # model alias 
        litellm_params:
            model: "azure/<your-deployment-name>"
            api_key: "os.environ/AZURE-API-KEY" # reads from key vault - get_secret("AZURE_API_KEY")
            api_base: "os.environ/AZURE-API-BASE" # reads from key vault - get_secret("AZURE_API_BASE")

general_settings:
  use_azure_key_vault: True
```

::: {.buttonGroup__atx}
:::
:::
:::

You can now test this by starting your proxy:

::: {.language-bash .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-bash .codeBlock_bY9V .thin-scrollbar tabindex="0"}
litellm --config /path/to/config.yaml
```

::: {.buttonGroup__atx}
:::
:::
:::

### Set Custom Prompt Templates[​](#set-custom-prompt-templates "Direct link to Set Custom Prompt Templates"){.hash-link} {#set-custom-prompt-templates .anchor .anchorWithStickyNavbar_LWe7}

LiteLLM by default checks if a model has a [prompt template and applies
it](/docs/completion/prompt_formatting) (e.g. if a huggingface model has
a saved chat template in it\'s tokenizer\_config.json). However, you can
also set a custom prompt template on your proxy in the `config.yaml`:

**Step 1**: Save your prompt template in a `config.yaml`

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
# Model-specific parameters
model_list:
  - model_name: mistral-7b # model alias
    litellm_params: # actual params for litellm.completion()
      model: "huggingface/mistralai/Mistral-7B-Instruct-v0.1" 
      api_base: "<your-api-base>"
      api_key: "<your-api-key>" # [OPTIONAL] for hf inference endpoints
      initial_prompt_value: "\n"
      roles: {"system":{"pre_message":"<|im_start|>system\n", "post_message":"<|im_end|>"}, "assistant":{"pre_message":"<|im_start|>assistant\n","post_message":"<|im_end|>"}, "user":{"pre_message":"<|im_start|>user\n","post_message":"<|im_end|>"}}
      final_prompt_value: "\n"
      bos_token: "<s>"
      eos_token: "</s>"
      max_tokens: 4096
```

::: {.buttonGroup__atx}
:::
:::
:::

**Step 2**: Start server with config

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --config /path/to/config.yaml
```

::: {.buttonGroup__atx}
:::
:::
:::

Router Settings[​](#router-settings "Direct link to Router Settings"){.hash-link} {#router-settings .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------------

Use this to configure things like routing strategy.

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
router_settings:
  routing_strategy: "least-busy"

model_list: # will route requests to the least busy ollama model
  - model_name: ollama-models
    litellm_params: 
      model: "ollama/mistral"
      api_base: "http://127.0.0.1:8001"
  - model_name: ollama-models
    litellm_params: 
      model: "ollama/codellama"
      api_base: "http://127.0.0.1:8002"
  - model_name: ollama-models
    litellm_params: 
      model: "ollama/llama2"
      api_base: "http://127.0.0.1:8003"
```

::: {.buttonGroup__atx}
:::
:::
:::

Max Parallel Requests[​](#max-parallel-requests "Direct link to Max Parallel Requests"){.hash-link} {#max-parallel-requests .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------------------------------

To rate limit a user based on the number of parallel requests, e.g.: if
user\'s parallel requests \> x, send a 429 error if user\'s parallel
requests \<= x, let them use the API freely.

set the max parallel request limit on the config.yaml (note: this
expects the user to be passing in an api key).

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
general_settings:
  max_parallel_requests: 100 # max parallel requests for a user = 100
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

[](/docs/proxy/quick_start){.pagination-nav__link
.pagination-nav__link--prev}

::: {.pagination-nav__sublabel}
Previous
:::

::: {.pagination-nav__label}
Quick Start
:::

[](/docs/proxy/embedding){.pagination-nav__link
.pagination-nav__link--next}

::: {.pagination-nav__sublabel}
Next
:::

::: {.pagination-nav__label}
Embeddings - /embeddings
:::
:::
:::

::: {.col .col--3}
::: {.tableOfContents_bqdL .thin-scrollbar .theme-doc-toc-desktop}
-   [Quick Start](#quick-start){.table-of-contents__link .toc-highlight}
    -   [Using Proxy - Curl Request, OpenAI Package, Langchain,
        Langchain
        JS](#using-proxy---curl-request-openai-package-langchain-langchain-js){.table-of-contents__link
        .toc-highlight}
-   [Save Model-specific params (API Base, API Keys, Temperature,
    Headers
    etc.)](#save-model-specific-params-api-base-api-keys-temperature-headers-etc){.table-of-contents__link
    .toc-highlight}
-   [Load API Keys](#load-api-keys){.table-of-contents__link
    .toc-highlight}
    -   [Load API Keys from
        Environment](#load-api-keys-from-environment){.table-of-contents__link
        .toc-highlight}
    -   [Load API Keys from Azure
        Vault](#load-api-keys-from-azure-vault){.table-of-contents__link
        .toc-highlight}
    -   [Set Custom Prompt
        Templates](#set-custom-prompt-templates){.table-of-contents__link
        .toc-highlight}
-   [Router Settings](#router-settings){.table-of-contents__link
    .toc-highlight}
-   [Max Parallel
    Requests](#max-parallel-requests){.table-of-contents__link
    .toc-highlight}
:::
:::
:::
:::
:::
:::
:::

::: {.container .container-fluid}
::: {.row .footer__links}
::: {.col .footer__col}
::: {.footer__title}
Docs
:::

-   [Tutorial](/docs/index){.footer__link-item}
:::

::: {.col .footer__col}
::: {.footer__title}
Community
:::

-   Discord
-   Twitter
:::

::: {.col .footer__col}
::: {.footer__title}
More
:::

-   GitHub
:::
:::

::: {.footer__bottom .text--center}
::: {.footer__copyright}
Copyright © 2023 liteLLM
:::
:::
:::
:::
