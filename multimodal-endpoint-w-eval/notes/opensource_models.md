

[Open in
app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F84fd4b45d0cf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---two_column_layout_nav----------------------------------)

[Sign
up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-llamaindex-84fd4b45d0cf&source=post_page---
two_column_layout_nav-----------------------global_nav-----------)

[Sign
in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-llamaindex-84fd4b45d0cf&source=post_page---
two_column_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---two_column_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=---two_column_layout_nav-----------------------
new_post_topnav-----------)

[](https://medium.com/search?source=---two_column_layout_nav----------------------------------)

[Sign
up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-llamaindex-84fd4b45d0cf&source=post_page---
two_column_layout_nav-----------------------global_nav-----------)

[Sign
in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-llamaindex-84fd4b45d0cf&source=post_page---
two_column_layout_nav-----------------------global_nav-----------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

# 10+ Ways to Run Open-Source Models with LlamaIndex

## LlamaIndex’s open-source model integration with Hugging Face, vLLM, Ollama,
Llama.cpp, liteLLM, Replicate, Gradient, and more

[![Wenqi
Glantz](https://miro.medium.com/v2/resize:fill:88:88/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page
-----84fd4b45d0cf--------------------------------)[![Level Up
Coding](https://miro.medium.com/v2/resize:fill:48:48/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page
-----84fd4b45d0cf--------------------------------)

[Wenqi Glantz](https://medium.com/@wenqiglantz?source=post_page-----
84fd4b45d0cf--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-
ce7cd5b8b74a----84fd4b45d0cf---------------------post_header-----------)

Published in

[Level Up Coding

](https://levelup.gitconnected.com/?source=post_page-----
84fd4b45d0cf--------------------------------)

·

18 min read

·

5 days ago

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F84fd4b45d0cf&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=-----84fd4b45d0cf
---------------------clap_footer-----------)

\--

2

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F84fd4b45d0cf&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&source=-----84fd4b45d0cf---------------------
bookmark_footer-----------)

Share

Image by DALL-E 3

The CTO of Hugging Face, [Julien
Chaumond](https://www.linkedin.com/in/julienchaumond/), [posted on
LinkedIn](https://www.linkedin.com/posts/julienchaumond_actually-lets-make-
bolder-predictions-for-
activity-7135999136788619264-RuKJ?utm_source=share&utm_medium=member_desktop)
two weeks ago and predicted that “Most open source models next year will be
better than OpenAI’s”.

Screenshot from LinkedIn

Astounding progress by the open-source community indeed! And the momentum is
simply unstoppable. With many quality open-source LLMs and embedding models
emerging every week, and their performance nearing that of those proprietary
models, it’s a no-brainer to roll up our sleeves and experiment with them to
see how well they perform for our specific use cases.

It is amazing to see the large number of integrations LlamaIndex has
established with a plethora of open-source model platforms and providers, and
the integration list keeps growing. In this article, let’s explore how we can
run open-source models, both LLMs and embedding models, with the out-of-the-
box support from LlamaIndex.

# RAG Pipeline: It’s a Wonderful Life

We will use the following two models for our RAG pipeline, which loads data
from the Wikipedia page of the classic movie [_It’s a Wonderful
Life_](https://en.wikipedia.org/wiki/It%27s_a_Wonderful_Life) __ (one of my
all-time favorites), and answers questions related to the movie. We will
explore the different ways we can utilize these two models in building our RAG
pipeline.

  * LLM: `zephyr-7b-beta`. A 7B parameter GPT-like model fine-tuned on a mix of publicly available, synthetic datasets. It’s a fine-tuned version of [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1). This will be used as our main LLM. However, some integration methods we explore in the sections below don’t support this LLM, we show the sample code snippet with a different LLM supported by that particular integration method.
  * Embedding model: `UAE-Large-V1`. Universal AnglE Embedding (UAE), ranked number 1 on the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) at the time of this writing.

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F84fd4b45d0cf&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=-----84fd4b45d0cf
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F84fd4b45d0cf&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=-----84fd4b45d0cf
---------------------clap_footer-----------)

\--

2

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F84fd4b45d0cf&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&source=--------------------------bookmark_footer-----------)

[![Wenqi
Glantz](https://miro.medium.com/v2/resize:fill:144:144/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page
-----84fd4b45d0cf--------------------------------)[![Level Up
Coding](https://miro.medium.com/v2/resize:fill:64:64/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page
-----84fd4b45d0cf--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-
ce7cd5b8b74a----84fd4b45d0cf---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F8a4fae108f4e&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&newsletterV3=ce7cd5b8b74a&newsletterV3Id=8a4fae108f4e&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=-----84fd4b45d0cf
---------------------subscribe_user-----------)

[

## Written by Wenqi Glantz

](https://medium.com/@wenqiglantz?source=post_page-----
84fd4b45d0cf--------------------------------)

[6.8K Followers](https://medium.com/@wenqiglantz/followers?source=post_page
-----84fd4b45d0cf--------------------------------)

·Writer for

[Level Up Coding

](https://levelup.gitconnected.com/?source=post_page-----
84fd4b45d0cf--------------------------------)

Mom, wife, software architect with a passion for technology and crafting
quality products [linkedin.com/in/wenqi-
glantz-b5448a5a/](http://linkedin.com/in/wenqi-glantz-b5448a5a/)
[twitter.com/wenqi_glantz](http://twitter.com/wenqi_glantz)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-
ce7cd5b8b74a----84fd4b45d0cf---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F8a4fae108f4e&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F10-ways-
to-run-open-source-models-with-
llamaindex-84fd4b45d0cf&newsletterV3=ce7cd5b8b74a&newsletterV3Id=8a4fae108f4e&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=-----84fd4b45d0cf
---------------------subscribe_user-----------)

[Help

](https://help.medium.com/hc/en-us?source=post_page-----
84fd4b45d0cf--------------------------------)

[Status

](https://medium.statuspage.io/?source=post_page-----
84fd4b45d0cf--------------------------------)

[About

](https://medium.com/about?autoplay=1&source=post_page-----
84fd4b45d0cf--------------------------------)

[Careers

](https://medium.com/jobs-at-medium/work-at-
medium-959d1a85284e?source=post_page-----
84fd4b45d0cf--------------------------------)

[Blog

](https://blog.medium.com/?source=post_page-----
84fd4b45d0cf--------------------------------)

[Privacy

](https://policy.medium.com/medium-privacy-
policy-f03bf92035c9?source=post_page-----
84fd4b45d0cf--------------------------------)

[Terms

](https://policy.medium.com/medium-terms-of-
service-9db0094a1e0f?source=post_page-----
84fd4b45d0cf--------------------------------)

[Text to speech

](https://speechify.com/medium?source=post_page-----
84fd4b45d0cf--------------------------------)

[Teams

](https://medium.com/business?source=post_page-----
84fd4b45d0cf--------------------------------)

