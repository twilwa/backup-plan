---
description: Add new models + Get model info without restarting proxy.
docsearch:docusaurus_tag: 'docs-default-current'
docsearch:language: en
docsearch:version: current
docusaurus_locale: en
docusaurus_tag: 'docs-default-current'
docusaurus_version: current
generator: Docusaurus v2.4.1
lang: en
title: 'Model Management \| liteLLM'
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
    -   [Proxy Config.yaml](/docs/proxy/configs){.menu__link}
    -   [Embeddings - /embeddings](/docs/proxy/embedding){.menu__link}
    -   [Load Balancing - Multiple Instances of 1
        model](/docs/proxy/load_balancing){.menu__link}
    -   [Key Management](/docs/proxy/virtual_keys){.menu__link}
    -   [Model Management](/docs/proxy/model_management){.menu__link
        .menu__link--active}
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
-   [Model Management]{.breadcrumbs__link itemprop="name"}

::: {.tocCollapsible_ETCw .theme-doc-toc-mobile .tocMobile_ITEo}
On this page
:::

::: {.theme-doc-markdown .markdown}
Model Management
================

Add new models + Get model info without restarting proxy.

In Config.yaml[​](#in-configyaml "Direct link to In Config.yaml"){.hash-link} {#in-configyaml .anchor .anchorWithStickyNavbar_LWe7}
-----------------------------------------------------------------------------

::: {.language-yaml .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-yaml .codeBlock_bY9V .thin-scrollbar tabindex="0"}
model_list:
  - model_name: text-davinci-003
    litellm_params: 
      model: "text-completion-openai/text-davinci-003"
    model_info: 
      metadata: "here's additional metadata on the model" # returned via GET /model/info
```

::: {.buttonGroup__atx}
:::
:::
:::

Get Model Information[​](#get-model-information "Direct link to Get Model Information"){.hash-link} {#get-model-information .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------------------------------

Retrieve detailed information about each model listed in the `/models`
endpoint, including descriptions from the `config.yaml` file, and
additional model info (e.g. max tokens, cost per input token, etc.)
pulled the model\_info you set and the litellm model cost map. Sensitive
details like API keys are excluded for security purposes.

::: {values="[object Object]"}
::: {value="curl"}
::: {.language-bash .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-bash .codeBlock_bY9V .thin-scrollbar tabindex="0"}
curl -X GET "http://0.0.0.0:8000/model/info" \
     -H "accept: application/json" \
```

::: {.buttonGroup__atx}
:::
:::
:::
:::
:::

Add a New Model[​](#add-a-new-model "Direct link to Add a New Model"){.hash-link} {#add-a-new-model .anchor .anchorWithStickyNavbar_LWe7}
---------------------------------------------------------------------------------

Add a new model to the list in the `config.yaml` by providing the model
parameters. This allows you to update the model list without restarting
the proxy.

::: {values="[object Object]"}
::: {value="curl"}
::: {.language-bash .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-bash .codeBlock_bY9V .thin-scrollbar tabindex="0"}
curl -X POST "http://0.0.0.0:8000/model/new" \
     -H "accept: application/json" \
     -H "Content-Type: application/json" \
     -d '{ "model_name": "azure-gpt-turbo", "litellm_params": {"model": "azure/gpt-3.5-turbo", "api_key": "os.environ/AZURE_API_KEY", "api_base": "my-azure-api-base"} }'
```

::: {.buttonGroup__atx}
:::
:::
:::
:::
:::

### Model Parameters Structure[​](#model-parameters-structure "Direct link to Model Parameters Structure"){.hash-link} {#model-parameters-structure .anchor .anchorWithStickyNavbar_LWe7}

When adding a new model, your JSON payload should conform to the
following structure:

-   `model_name`: The name of the new model (required).
-   `litellm_params`: A dictionary containing parameters specific to the
    Litellm setup (required).
-   `model_info`: An optional dictionary to provide additional
    information about the model.

Here\'s an example of how to structure your `ModelParams`:

::: {.language-json .codeBlockContainer_Ckt0 .theme-code-block style="--prism-color:#393A34;--prism-background-color:#f6f8fa"}
::: {.codeBlockContent_biex}
``` {.prism-code .language-json .codeBlock_bY9V .thin-scrollbar tabindex="0"}
{
  "model_name": "my_awesome_model",
  "litellm_params": {
    "some_parameter": "some_value",
    "another_parameter": "another_value"
  },
  "model_info": {
    "author": "Your Name",
    "version": "1.0",
    "description": "A brief description of the model."
  }
}
```

::: {.buttonGroup__atx}
:::
:::
:::

------------------------------------------------------------------------

Keep in mind that as both endpoints are in \[BETA\], you may need to
visit the associated GitHub issues linked in the API descriptions to
check for updates or provide feedback:

-   Get Model Information: [Issue
    \#933](https://github.com/BerriAI/litellm/issues/933)
-   Add a New Model: [Issue
    \#964](https://github.com/BerriAI/litellm/issues/964)

Feedback on the beta endpoints is valuable and helps improve the API for
all users.
:::

[](/docs/proxy/virtual_keys){.pagination-nav__link
.pagination-nav__link--prev}

::: {.pagination-nav__sublabel}
Previous
:::

::: {.pagination-nav__label}
Key Management
:::

[](/docs/proxy/reliability){.pagination-nav__link
.pagination-nav__link--next}

::: {.pagination-nav__sublabel}
Next
:::

::: {.pagination-nav__label}
Fallbacks, Retries, Timeouts, Cooldowns
:::
:::
:::

::: {.col .col--3}
::: {.tableOfContents_bqdL .thin-scrollbar .theme-doc-toc-desktop}
-   [In Config.yaml](#in-configyaml){.table-of-contents__link
    .toc-highlight}
-   [Get Model
    Information](#get-model-information){.table-of-contents__link
    .toc-highlight}
-   [Add a New Model](#add-a-new-model){.table-of-contents__link
    .toc-highlight}
    -   [Model Parameters
        Structure](#model-parameters-structure){.table-of-contents__link
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
