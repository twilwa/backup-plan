LiteLLM APIs¶
Below is how you can instantiate LiteLLM as a provider. LiteLLM supports 100+ models from OpenAI, Cohere, Anthropic, HuggingFace, Meta and more. You can find more information about models available here.

All feedback functions listed in the base LLMProvider class can be run with LiteLLM.

Bases: LLMProvider

Out of the box feedback functions calling LiteLLM API.

Source code in trulens_eval/trulens_eval/feedback/provider/litellm.py
__init__(*args, endpoint=None, model_engine='gpt-3.5-turbo', **kwargs) ¶
Create an LiteLLM Provider with out of the box feedback functions.

Usage:


from trulens_eval.feedback.provider.litellm import LiteLLM
litellm_provider = LiteLLM()
Parameters:

Name	Type	Description	Default
model_engine	str	The LiteLLM completion model.Defaults to gpt-3.5-turbo	'gpt-3.5-turbo'
endpoint	Endpoint	Internal Usage for DB serialization	None
