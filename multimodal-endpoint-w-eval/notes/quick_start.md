---
description: 'Quick start CLI, Config, Docker'
docsearch:docusaurus_tag: 'docs-default-current'
docsearch:language: en
docsearch:version: current
docusaurus_locale: en
docusaurus_tag: 'docs-default-current'
docusaurus_version: current
generator: Docusaurus v2.4.1
lang: en
title: 'Quick Start \| liteLLM'
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

    -   [Quick Start](/docs/proxy/quick_start){.menu__link
        .menu__link--active}
    -   [Proxy Config.yaml](/docs/proxy/configs){.menu__link}
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
-   [Quick Start]{.breadcrumbs__link itemprop="name"}

::: {.tocCollapsible_ETCw .theme-doc-toc-mobile .tocMobile_ITEo}
On this page
:::

::: {.theme-doc-markdown .markdown}
Quick Start
===========

Quick start CLI, Config, Docker

LiteLLM Server manages:

-   **Unified Interface**: Calling 100+ LLMs
    [Huggingface/Bedrock/TogetherAI/etc.](#other-supported-models) in
    the OpenAI `ChatCompletions` & `Completions` format
-   **Load Balancing**: between [Multiple
    Models](#multiple-models---quick-start) + [Deployments of the same
    model](#multiple-instances-of-1-model) - LiteLLM proxy can handle
    1.5k+ requests/second during load tests.
-   **Cost tracking**: Authentication & Spend Tracking [Virtual
    Keys](#managing-auth---virtual-keys)

[**See LiteLLM Proxy
code**](https://github.com/BerriAI/litellm/tree/main/litellm/proxy)

View all the supported args for the Proxy CLI
[here](https://docs.litellm.ai/docs/simple_proxy#proxy-cli-arguments)

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ pip install litellm[proxy]
```

::: {.buttonGroup__atx}
:::
:::
:::

If this fails try running

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ pip install 'litellm[proxy]'
```

::: {.buttonGroup__atx}
:::
:::
:::

Quick Start - LiteLLM Proxy CLI[​](#quick-start---litellm-proxy-cli "Direct link to Quick Start - LiteLLM Proxy CLI"){.hash-link} {#quick-start---litellm-proxy-cli .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------------------------------------------------------------

Run the following command to start the litellm proxy

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model huggingface/bigcode/starcoder

#INFO: Proxy running on http://0.0.0.0:8000
```

::: {.buttonGroup__atx}
:::
:::
:::

### Test[​](#test "Direct link to Test"){.hash-link} {#test .anchor .anchorWithStickyNavbar_LWe7}

In a new shell, run, this will make an `openai.chat.completions`
request. Ensure you\'re using openai v1.0.0+

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
litellm --test
```

::: {.buttonGroup__atx}
:::
:::
:::

This will now automatically route any requests for gpt-3.5-turbo to
bigcode starcoder, hosted on huggingface inference endpoints.

### Using LiteLLM Proxy - Curl Request, OpenAI Package, Langchain, Langchain JS[​](#using-litellm-proxy---curl-request-openai-package-langchain-langchain-js "Direct link to Using LiteLLM Proxy - Curl Request, OpenAI Package, Langchain, Langchain JS"){.hash-link} {#using-litellm-proxy---curl-request-openai-package-langchain-langchain-js .anchor .anchorWithStickyNavbar_LWe7}

::: {.tabs-container .tabList__CuJ}
-   Curl Request
-   OpenAI v1.0.0+
-   Langchain
-   Langchain Embeddings

::: {.margin-top--md}
::: {.tabItem_Ymn6 role="tabpanel"}
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
      ]
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

# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="gpt-3.5-turbo", messages = [
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

chat = ChatOpenAI(
    openai_api_base="http://0.0.0.0:8000", # set openai_api_base to the LiteLLM Proxy
    model = "gpt-3.5-turbo",
    temperature=0.1
)

messages = [
    SystemMessage(
        content="You are a helpful assistant that im using to make a test request to."
    ),
    HumanMessage(
        content="test from litellm. tell me why it's amazing in 1 sentence"
    ),
]
response = chat(messages)

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
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="sagemaker-embeddings", openai_api_base="http://0.0.0.0:8000", openai_api_key="temp-key")


text = "This is a test document."

query_result = embeddings.embed_query(text)

print(f"SAGEMAKER EMBEDDINGS")
print(query_result[:5])

embeddings = OpenAIEmbeddings(model="bedrock-embeddings", openai_api_base="http://0.0.0.0:8000", openai_api_key="temp-key")

text = "This is a test document."

query_result = embeddings.embed_query(text)

print(f"BEDROCK EMBEDDINGS")
print(query_result[:5])

embeddings = OpenAIEmbeddings(model="bedrock-titan-embeddings", openai_api_base="http://0.0.0.0:8000", openai_api_key="temp-key")

text = "This is a test document."

query_result = embeddings.embed_query(text)

print(f"TITAN EMBEDDINGS")
print(query_result[:5])
```

::: {.buttonGroup__atx}
:::
:::
:::
:::
:::
:::

### Supported LLMs[​](#supported-llms "Direct link to Supported LLMs"){.hash-link} {#supported-llms .anchor .anchorWithStickyNavbar_LWe7}

All LiteLLM supported LLMs are supported on the Proxy. Seel all
[supported llms](https://docs.litellm.ai/docs/providers)

::: {.tabs-container .tabList__CuJ}
-   AWS Bedrock
-   Azure OpenAI
-   OpenAI
-   OpenAI Compatible Endpoint
-   Huggingface (TGI) Deployed
-   Huggingface (TGI) Local
-   AWS Sagemaker
-   Anthropic
-   VLLM
-   TogetherAI
-   Replicate
-   Petals
-   Palm
-   AI21
-   Cohere

::: {.margin-top--md}
::: {.tabItem_Ymn6 role="tabpanel"}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export AWS_ACCESS_KEY_ID=
$ export AWS_REGION_NAME=
$ export AWS_SECRET_ACCESS_KEY=
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model bedrock/anthropic.claude-v2
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export AZURE_API_KEY=my-api-key
$ export AZURE_API_BASE=my-api-base
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-text .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model azure/my-deployment-name
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export OPENAI_API_KEY=my-api-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model gpt-3.5-turbo
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export OPENAI_API_KEY=my-api-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model openai/<your model name> --api_base <your-api-base> # e.g. http://0.0.0.0:3000
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export HUGGINGFACE_API_KEY=my-api-key #[OPTIONAL]
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model huggingface/<your model name> --api_base <your-api-base> # e.g. http://0.0.0.0:3000
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model huggingface/<your model name> --api_base http://0.0.0.0:8001
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
export AWS_ACCESS_KEY_ID=
export AWS_REGION_NAME=
export AWS_SECRET_ACCESS_KEY=
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model sagemaker/jumpstart-dft-meta-textgeneration-llama-2-7b
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export ANTHROPIC_API_KEY=my-api-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model claude-instant-1
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
Assuming you\'re running vllm locally

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model vllm/facebook/opt-125m
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export TOGETHERAI_API_KEY=my-api-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model together_ai/lmsys/vicuna-13b-v1.5-16k
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export REPLICATE_API_KEY=my-api-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm \
  --model replicate/meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model petals/meta-llama/Llama-2-70b-chat-hf
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export PALM_API_KEY=my-palm-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model palm/chat-bison
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export AI21_API_KEY=my-api-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model j2-light
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ export COHERE_API_KEY=my-api-key
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ litellm --model command-nightly
```

::: {.buttonGroup__atx}
:::
:::
:::
:::
:::
:::

Quick Start - LiteLLM Proxy + Config.yaml[​](#quick-start---litellm-proxy--configyaml "Direct link to Quick Start - LiteLLM Proxy + Config.yaml"){.hash-link} {#quick-start---litellm-proxy--configyaml .anchor .anchorWithStickyNavbar_LWe7}
-------------------------------------------------------------------------------------------------------------------------------------------------------------

The config allows you to create a model list and set `api_base`,
`max_tokens` (all litellm params). See more details about the config
[here](https://docs.litellm.ai/docs/proxy/configs)

### Create a Config for LiteLLM Proxy[​](#create-a-config-for-litellm-proxy "Direct link to Create a Config for LiteLLM Proxy"){.hash-link} {#create-a-config-for-litellm-proxy .anchor .anchorWithStickyNavbar_LWe7}

Example config

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
model_list: 
  - model_name: gpt-3.5-turbo # user-facing model alias
    litellm_params: # all params accepted by litellm.completion() - https://docs.litellm.ai/docs/completion/input
      model: azure/<your-deployment-name>
      api_base: <your-azure-api-endpoint>
      api_key: <your-azure-api-key>
  - model_name: gpt-3.5-turbo
    litellm_params:
      model: azure/gpt-turbo-small-ca
      api_base: https://my-endpoint-canada-berri992.openai.azure.com/
      api_key: <your-azure-api-key>
  - model_name: vllm-model
    litellm_params:
      model: openai/<your-model-name>
      api_base: <your-api-base> # e.g. http://0.0.0.0:3000
```

::: {.buttonGroup__atx}
:::
:::
:::

### Run proxy with config[​](#run-proxy-with-config "Direct link to Run proxy with config"){.hash-link} {#run-proxy-with-config .anchor .anchorWithStickyNavbar_LWe7}

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
litellm --config your_config.yaml
```

::: {.buttonGroup__atx}
:::
:::
:::

[**More Info**](/docs/proxy/configs)

Server Endpoints[​](#server-endpoints "Direct link to Server Endpoints"){.hash-link} {#server-endpoints .anchor .anchorWithStickyNavbar_LWe7}
------------------------------------------------------------------------------------

::: {.theme-admonition .theme-admonition-note .alert .alert--secondary .admonition_LlT9}
::: {.admonitionHeading_tbUL}
note
:::

::: {.admonitionContent_S0QG}
You can see Swagger Docs for the server on root <http://0.0.0.0:8000>
:::
:::

-   POST `/chat/completions` - chat completions endpoint to call 100+
    LLMs
-   POST `/completions` - completions endpoint
-   POST `/embeddings` - embedding endpoint for Azure, OpenAI,
    Huggingface endpoints
-   GET `/models` - available models on server
-   POST `/key/generate` - generate a key to access the proxy

Gunicorn + Proxy[​](#gunicorn--proxy "Direct link to Gunicorn + Proxy"){.hash-link} {#gunicorn--proxy .anchor .anchorWithStickyNavbar_LWe7}
-----------------------------------------------------------------------------------

Command:

::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
cmd = f"gunicorn litellm.proxy.proxy_server:app --workers {num_workers} --worker-class uvicorn.workers.UvicornWorker --bind {host}:{port}"
```

::: {.buttonGroup__atx}
:::
:::
:::

[**Code**](https://github.com/BerriAI/litellm/blob/077f6b1298101079b72396bdf04f8ca0cf737720/litellm/tests/test_proxy_gunicorn.py#L4)

Quick Start Docker Image: Github Container Registry[​](#quick-start-docker-image-github-container-registry "Direct link to Quick Start Docker Image: Github Container Registry"){.hash-link} {#quick-start-docker-image-github-container-registry .anchor .anchorWithStickyNavbar_LWe7}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Pull the litellm ghcr docker image[​](#pull-the-litellm-ghcr-docker-image "Direct link to Pull the litellm ghcr docker image"){.hash-link} {#pull-the-litellm-ghcr-docker-image .anchor .anchorWithStickyNavbar_LWe7}

See the latest available ghcr docker image here:
<https://github.com/berriai/litellm/pkgs/container/litellm>

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
docker pull ghcr.io/berriai/litellm:main-v1.10.1
```

::: {.buttonGroup__atx}
:::
:::
:::

### Run the Docker Image[​](#run-the-docker-image "Direct link to Run the Docker Image"){.hash-link} {#run-the-docker-image .anchor .anchorWithStickyNavbar_LWe7}

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
docker run ghcr.io/berriai/litellm:main-v1.10.0
```

::: {.buttonGroup__atx}
:::
:::
:::

#### Run the Docker Image with LiteLLM CLI args[​](#run-the-docker-image-with-litellm-cli-args "Direct link to Run the Docker Image with LiteLLM CLI args"){.hash-link} {#run-the-docker-image-with-litellm-cli-args .anchor .anchorWithStickyNavbar_LWe7}

See all supported CLI args
[here](https://docs.litellm.ai/docs/proxy/cli):

Here\'s how you can run the docker image and pass your config to
`litellm`

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
docker run ghcr.io/berriai/litellm:main-v1.10.0 --config your_config.yaml
```

::: {.buttonGroup__atx}
:::
:::
:::

Here\'s how you can run the docker image and start litellm on port 8002
with `num_workers=8`

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
docker run ghcr.io/berriai/litellm:main-v1.10.0 --port 8002 --num_workers 8
```

::: {.buttonGroup__atx}
:::
:::
:::

#### Run the Docker Image using docker compose[​](#run-the-docker-image-using-docker-compose "Direct link to Run the Docker Image using docker compose"){.hash-link} {#run-the-docker-image-using-docker-compose .anchor .anchorWithStickyNavbar_LWe7}

**Step 1**

-   (Recommended) Use the example file `docker-compose.example.yml`
    given in the project root. e.g.
    <https://github.com/BerriAI/litellm/blob/main/docker-compose.example.yml>

-   Rename the file `docker-compose.example.yml` to
    `docker-compose.yml`.

Here\'s an example `docker-compose.yml` file

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
version: "3.9"
services:
  litellm:
    image: ghcr.io/berriai/litellm:main
    ports:
      - "8000:8000" # Map the container port to the host, change the host port if necessary
    volumes:
      - ./litellm-config.yaml:/app/config.yaml # Mount the local configuration file
    # You can change the port or number of workers as per your requirements or pass any new supported CLI augument. Make sure the port passed here matches with the container port defined above in `ports` value
    command: [ "--config", "/app/config.yaml", "--port", "8000", "--num_workers", "8" ]

# ...rest of your docker-compose config if any
```

::: {.buttonGroup__atx}
:::
:::
:::

**Step 2**

Create a `litellm-config.yaml` file with your LiteLLM config relative to
your `docker-compose.yml` file.

Check the config doc [here](https://docs.litellm.ai/docs/proxy/configs)

**Step 3**

Run the command `docker-compose up` or `docker compose up` as per your
docker installation.

> Use `-d` flag to run the container in detached mode (background) e.g.
> `docker compose up -d`

Your LiteLLM container should be running now on the defined port e.g.
`8000`.

Using with OpenAI compatible projects[​](#using-with-openai-compatible-projects "Direct link to Using with OpenAI compatible projects"){.hash-link} {#using-with-openai-compatible-projects .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------------------------------------------------------------------------------

Set `base_url` to the LiteLLM Proxy server

::: {.tabs-container .tabList__CuJ}
-   OpenAI v1.0.0+
-   LibreChat
-   ContinueDev
-   Aider
-   AutoGen
-   guidance

::: {.margin-top--md}
::: {.tabItem_Ymn6 role="tabpanel"}
::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
import openai
client = openai.OpenAI(
    api_key="anything",
    base_url="http://0.0.0.0:8000"
)

# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="gpt-3.5-turbo", messages = [
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
#### Start the LiteLLM proxy[​](#start-the-litellm-proxy "Direct link to Start the LiteLLM proxy"){.hash-link} {#start-the-litellm-proxy .anchor .anchorWithStickyNavbar_LWe7}

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
litellm --model gpt-3.5-turbo

#INFO: Proxy running on http://0.0.0.0:8000
```

::: {.buttonGroup__atx}
:::
:::
:::

#### 1. Clone the repo[​](#1-clone-the-repo "Direct link to 1. Clone the repo"){.hash-link} {#1-clone-the-repo .anchor .anchorWithStickyNavbar_LWe7}

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
git clone https://github.com/danny-avila/LibreChat.git
```

::: {.buttonGroup__atx}
:::
:::
:::

#### 2. Modify Librechat\'s `docker-compose.yml`[​](#2-modify-librechats-docker-composeyml "Direct link to 2-modify-librechats-docker-composeyml"){.hash-link} {#2-modify-librechats-docker-composeyml .anchor .anchorWithStickyNavbar_LWe7}

LiteLLM Proxy is running on port `8000`, set `8000` as the proxy below

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
OPENAI_REVERSE_PROXY=http://host.docker.internal:8000/v1/chat/completions
```

::: {.buttonGroup__atx}
:::
:::
:::

#### 3. Save fake OpenAI key in Librechat\'s `.env`[​](#3-save-fake-openai-key-in-librechats-env "Direct link to 3-save-fake-openai-key-in-librechats-env"){.hash-link} {#3-save-fake-openai-key-in-librechats-env .anchor .anchorWithStickyNavbar_LWe7}

Copy Librechat\'s `.env.example` to `.env` and overwrite the default
OPENAI\_API\_KEY (by default it requires the user to pass a key).

::: {.language-env .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-env .codeBlock_bY9V .thin-scrollbar tabindex="0"}
OPENAI_API_KEY=sk-1234
```

::: {.buttonGroup__atx}
:::
:::
:::

#### 4. Run LibreChat:[​](#4-run-librechat "Direct link to 4. Run LibreChat:"){.hash-link} {#4-run-librechat .anchor .anchorWithStickyNavbar_LWe7}

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
docker compose up
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
Continue-Dev brings ChatGPT to VSCode. See how to [install it
here](https://continue.dev/docs/quickstart).

In the [config.py](https://continue.dev/docs/reference/Models/openai)
set this as your default model.

::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
  default=OpenAI(
      api_key="IGNORED",
      model="fake-model-name",
      context_length=2048, # customize if needed for your model
      api_base="http://localhost:8000" # your proxy server url
  ),
```

::: {.buttonGroup__atx}
:::
:::
:::

Credits
[\@vividfog](https://github.com/jmorganca/ollama/issues/305#issuecomment-1751848077)
for this tutorial.
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
$ pip install aider 

$ aider --openai-api-base http://0.0.0.0:8000 --openai-api-key fake-key
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
pip install pyautogen
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
from autogen import AssistantAgent, UserProxyAgent, oai
config_list=[
    {
        "model": "my-fake-model",
        "api_base": "http://localhost:8000",  #litellm compatible endpoint
        "api_type": "open_ai",
        "api_key": "NULL", # just a placeholder
    }
]

response = oai.Completion.create(config_list=config_list, prompt="Hi")
print(response) # works fine

llm_config={
    "config_list": config_list,
}

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy")
user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change YTD.", config_list=config_list)
```

::: {.buttonGroup__atx}
:::
:::
:::

Credits
[\@victordibia](https://github.com/microsoft/autogen/issues/45#issuecomment-1749921972)
for this tutorial.
:::

::: {.tabItem_Ymn6 role="tabpanel" hidden=""}
A guidance language for controlling large language models.
https://github.com/guidance-ai/guidance

**NOTE:** Guidance sends additional params like `stop_sequences` which
can cause some models to fail if they don\'t support it.

**Fix**: Start your proxy using the `--drop_params` flag

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
litellm --model ollama/codellama --temperature 0.3 --max_tokens 2048 --drop_params
```

::: {.buttonGroup__atx}
:::
:::
:::

::: {.language-python .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-python .codeBlock_bY9V .thin-scrollbar tabindex="0"}
import guidance

# set api_base to your proxy
# set api_key to anything
gpt4 = guidance.llms.OpenAI("gpt-4", api_base="http://0.0.0.0:8000", api_key="anything")

experts = guidance('''
{{#system~}}
You are a helpful and terse assistant.
{{~/system}}

{{#user~}}
I want a response to the following question:
{{query}}
Name 3 world-class experts (past or present) who would be great at answering this?
Don't answer the question yet.
{{~/user}}

{{#assistant~}}
{{gen 'expert_names' temperature=0 max_tokens=300}}
{{~/assistant}}
''', llm=gpt4)

result = experts(query='How can I be more productive?')
print(result)
```

::: {.buttonGroup__atx}
:::
:::
:::
:::
:::
:::

Debugging Proxy[​](#debugging-proxy "Direct link to Debugging Proxy"){.hash-link} {#debugging-proxy .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------------

Run the proxy with `--debug` to easily view debug logs

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
litellm --model gpt-3.5-turbo --debug
```

::: {.buttonGroup__atx}
:::
:::
:::

When making requests you should see the POST request sent by LiteLLM to
the LLM on the Terminal output

::: {.language-shell .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-shell .codeBlock_bY9V .thin-scrollbar tabindex="0"}
POST Request Sent from LiteLLM:
curl -X POST \
https://api.openai.com/v1/chat/completions \
-H 'content-type: application/json' -H 'Authorization: Bearer sk-qnWGUIW9****************************************' \
-d '{"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "this is a test request, write a short poem"}]}'
```

::: {.buttonGroup__atx}
:::
:::
:::
:::

[](/docs/simple_proxy){.pagination-nav__link
.pagination-nav__link--prev}

::: {.pagination-nav__sublabel}
Previous
:::

::: {.pagination-nav__label}
💥 OpenAI Proxy Server
:::

[](/docs/proxy/configs){.pagination-nav__link
.pagination-nav__link--next}

::: {.pagination-nav__sublabel}
Next
:::

::: {.pagination-nav__label}
Proxy Config.yaml
:::
:::
:::

::: {.col .col--3}
::: {.tableOfContents_bqdL .thin-scrollbar .theme-doc-toc-desktop}
-   [Quick Start - LiteLLM Proxy
    CLI](#quick-start---litellm-proxy-cli){.table-of-contents__link
    .toc-highlight}
    -   [Test](#test){.table-of-contents__link .toc-highlight}
    -   [Using LiteLLM Proxy - Curl Request, OpenAI Package, Langchain,
        Langchain
        JS](#using-litellm-proxy---curl-request-openai-package-langchain-langchain-js){.table-of-contents__link
        .toc-highlight}
    -   [Supported LLMs](#supported-llms){.table-of-contents__link
        .toc-highlight}
-   [Quick Start - LiteLLM Proxy +
    Config.yaml](#quick-start---litellm-proxy--configyaml){.table-of-contents__link
    .toc-highlight}
    -   [Create a Config for LiteLLM
        Proxy](#create-a-config-for-litellm-proxy){.table-of-contents__link
        .toc-highlight}
    -   [Run proxy with
        config](#run-proxy-with-config){.table-of-contents__link
        .toc-highlight}
-   [Server Endpoints](#server-endpoints){.table-of-contents__link
    .toc-highlight}
-   [Gunicorn + Proxy](#gunicorn--proxy){.table-of-contents__link
    .toc-highlight}
-   [Quick Start Docker Image: Github Container
    Registry](#quick-start-docker-image-github-container-registry){.table-of-contents__link
    .toc-highlight}
    -   [Pull the litellm ghcr docker
        image](#pull-the-litellm-ghcr-docker-image){.table-of-contents__link
        .toc-highlight}
    -   [Run the Docker
        Image](#run-the-docker-image){.table-of-contents__link
        .toc-highlight}
-   [Using with OpenAI compatible
    projects](#using-with-openai-compatible-projects){.table-of-contents__link
    .toc-highlight}
-   [Debugging Proxy](#debugging-proxy){.table-of-contents__link
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
