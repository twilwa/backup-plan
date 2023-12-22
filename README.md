# backup-plan
'Notebooks' contain notebooks related to multimodal Weaviate and Neo4j RAG pipelines; these might be interesting candidates for trulens evals.

'trulens' contains the contents of the 'trulens-eval' folder found at https://github.com/truera/trulens/tree/main/trulens_eval.

in the 'trulens/examples' folder, notebooks found under 'quickstart' should run entirely as-is, '/expositional' may require updates to the dependencies outlined at the top of the file.

'expositionial' also contains an 'end2end_apps' folder, which you might use as a starting point for a full-stack application that incorporates TruLens.

'completed-eval-data' contains two folders, 'outputs' and 'notebooks', which your work should be deposited to upon completion. See 'CONTRIBUTING:' for more details.

Documentation for Google Gemini can be found [here](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini?_ga=2.179001954.-799536016.1700120910&_gac=1.26697039.1702492576.Cj0KCQiAyeWrBhDDARIsAGP1mWRBfEyPIju5t-GUBCU4kfiqJq_YQAYEbuQE9qwfgi82tBqdYiiorp4aAuD0EALw_wcB). A requirement for the submission is to incorporate Google Gemini as part of a Trulens evaluation.

---
WORKFLOW:

If applicable for your usecase, choose an example notebook from 'quickstart', then modify the imports to run the eval against Gemini. Follow the instructions in the notebook to extract the evaluation data, then deposit the data into 'completed-eval-data' as outlined once completed. Completion of this process hits all code-related requirements your for submission to lablab's gemini/trulens hackathon. For more complex use-cases, modify the appropriate template notebook or create your own following the guidelines outlined above.

CONTRIBUTING:

Additional notebooks which are incomplete and require modifications (i.e. ones you found somewhere that would be cool to run evals on), can be deposited into the 'notebooks' folder under the appropriate vendor name via pull request. Any completed evaluation data should be deposited into the 'completed-eval-data/outputs' folder for review (example outputs or interesting runs are welcome as a showcase!). The name of the corresponding notebook (which, after being successfully modified & confirmed to run as-is, should be deposited into the 'completed-eval-data/notebooks' folder) should be identical to the name of the notebook with the suffix '-data'.

Before beginning notebook modification, create an issue in the repo for visibility, or fork this repo and do the same for your team. If you use this repository as a template, be sure to set your upstream to your submission repository rather than this one!

GG everybody!

FURTHER READING:
I'll include 'why did nobody tell me how to do this earlier' materials into the notebooks/tutorials section. Feel free to contribute there as well!

