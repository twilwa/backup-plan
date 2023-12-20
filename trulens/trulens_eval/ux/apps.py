# Code in support of the Apps.py page.

from typing import Any, Optional

import pydantic

from trulens_eval.app import App
from trulens_eval.utils.serial import JSON


class ChatRecord(pydantic.BaseModel):

    class Config:
        arbitrary_types_allowed = True

    # Human input
    human: Optional[str] = None

    # Computer response
    computer: Optional[str] = None

    # Jsonified record. Available only after the app is run on human input and
    # produced a computer output.
    record_json: Optional[JSON] = None

    # The final app state for continuing the session.
    app: App

    # The state of the app as was when this record was produced.
    app_json: JSON
