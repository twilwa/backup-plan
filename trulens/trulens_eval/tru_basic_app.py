"""
# Basic input output instrumentation and monitoring.
"""

from inspect import BoundArguments
from inspect import signature
from inspect import Signature
import logging
from pprint import PrettyPrinter
from typing import Callable, ClassVar, Optional

from pydantic import Field

from trulens_eval.app import App
from trulens_eval.instruments import Instrument
from trulens_eval.utils.pyschema import Class
from trulens_eval.utils.pyschema import FunctionOrMethod

logger = logging.getLogger(__name__)

pp = PrettyPrinter()


class TruBasicCallableInstrument(Instrument):

    class Default:
        CLASSES = lambda: {TruWrapperApp}

        # Instrument only methods with these names and of these classes.
        METHODS = {"_call": lambda o: isinstance(o, TruWrapperApp)}

    def __init__(self, *args, **kwargs):
        super().__init__(
            include_classes=TruBasicCallableInstrument.Default.CLASSES(),
            include_methods=TruBasicCallableInstrument.Default.METHODS,
            *args,
            **kwargs
        )


class TruWrapperApp(object):
    # This will be wrapped by instrumentation. Because TruWrapperApp may wrap
    # different types of callables, we cannot patch the signature to anything
    # consistent. Because of this, the dashboard/record for this call will have
    # *args, **kwargs instead of what the app actually uses. We also need to
    # adjust the main_input lookup to get the correct signature. See note there.
    def _call(self, *args, **kwargs):
        return self._call_fn(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self._call(*args, **kwargs)

    def __init__(self, call_fn: Callable):
        self._call_fn = call_fn


class TruBasicApp(App):
    """Instantiates a Basic app that makes little assumptions. Assumes input text and output text.
        
        **Usage:**

        ```
        def custom_application(prompt: str) -> str:
            return "a response"
        
        from trulens_eval import TruBasicApp
        # f_lang_match, f_qa_relevance, f_qs_relevance are feedback functions
        tru_recorder = TruBasicApp(custom_application, 
            app_id="Custom Application v1",
            feedbacks=[f_lang_match, f_qa_relevance, f_qs_relevance])

        # Basic app works by turning your callable into an app
        # This app is accessbile with the `app` attribute in the recorder
        with tru_recorder as recording:
            tru_recorder.app(question)

        tru_record = recording.records[0]
        
        ```
        See [Feedback Functions](https://www.trulens.org/trulens_eval/api/feedback/) for instantiating feedback functions.

        Args:
            text_to_text (Callable): A text to text callable.
    """

    class Config:
        arbitrary_types_allowed = True

    app: TruWrapperApp

    root_callable: ClassVar[FunctionOrMethod] = Field(
        default_factory=lambda: FunctionOrMethod.
        of_callable(TruWrapperApp._call)
    )

    def __init__(
        self,
        text_to_text: Optional[Callable] = None,
        app: Optional[TruWrapperApp] = None,
        **kwargs
    ):
        """
        Wrap a callable for monitoring.

        Arguments:
        - text_to_text: A function with signature string to string.
        - More args in App
        - More args in AppDefinition
        - More args in WithClassInfo
        """

        if text_to_text is not None:
            app = TruWrapperApp(text_to_text)
        else:
            assert app is not None, "Need to provide either `app: TruWrapperApp` or a `text_to_text: Callable`."

        kwargs['app'] = app
        kwargs['root_class'] = Class.of_object(app)
        kwargs['instrument'] = TruBasicCallableInstrument(app=self)

        super().__init__(**kwargs)

    def main_call(self, human: str) -> str:
        # If available, a single text to a single text invocation of this app.

        return self.app._call(human)

    async def main_acall(self, human: str) -> str:
        # If available, a single text to a single text invocation of this app.
        raise NotImplementedError()

    def main_input(
        self, func: Callable, sig: Signature, bindings: BoundArguments
    ) -> str:

        if func == getattr(TruWrapperApp._call, Instrument.INSTRUMENT):
            # If func is the wrapper app _call, replace the signature and
            # bindings based on the actual containing callable instead of
            # self.app._call . This needs to be done since the a TruWrapperApp
            # may be wrapping apps with different signatures on their callables
            # so TruWrapperApp._call cannot have a consistent signature
            # statically. Note also we are looking up the Instrument.INSTRUMENT
            # attribute here since the method is instrumented and overridden by
            # another wrapper in the process with the original accessible at
            # this attribute.

            sig = signature(self.app._call_fn)
            # Skipping self as TruWrapperApp._call takes in self, but
            # self.app._call_fn does not.
            bindings = sig.bind(*bindings.args[1:], **bindings.kwargs)

        return super().main_input(func, sig, bindings)

    def call_with_record(self, *args, **kwargs):
        """
        Run the callable with the given arguments. Note that the wrapped
        callable is expected to take in a single string.

        Returns:
            dict: record metadata
        """
        # NOTE: Actually text_to_text can take in more args.

        self._with_dep_message(method="call", is_async=False, with_record=True)

        return self.with_record(self.app._call, *args, **kwargs)


TruBasicApp.model_rebuild()
