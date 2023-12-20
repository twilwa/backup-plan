# backup-plan
well this looked like fun

'Datatonic' contains evaluation files and information from the original repo.
'Notebooks' contain notebooks related to multimodal Weaviate and Neo4j RAG pipelines; these might be interesting candidates for trulens evals.
'trulens' contains the contents of the 'trulens-eval' folder found at https://github.com/truera/trulens/tree/main/trulens_eval.
in the 'trulens/examples' folder, notebooks found under 'quickstart' should run entirely as-is, '/expositional' may require updates to the dependencies outlined at the top of the file.
'expositionial' also contains an 'end2end_apps' folder, which you might use as a starting point for a full-stack application that incorporates TruLens.
'completed-eval-data' contains two folders, 'outputs' and 'notebooks', which your work should be deposited to upon completion. See 'CONTRIBUTING:' for more details.

Documentation for Google Gemini can be found [here](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini?_ga=2.179001954.-799536016.1700120910&_gac=1.26697039.1702492576.Cj0KCQiAyeWrBhDDARIsAGP1mWRBfEyPIju5t-GUBCU4kfiqJq_YQAYEbuQE9qwfgi82tBqdYiiorp4aAuD0EALw_wcB). A requirement for the submission is to incorporate Google Gemini as part of a Trulens evaluation.

If applicable for your usecase, choose an example notebook from 'quickstart', then modify the imports to run the eval against Gemini. Follow the instructions in the notebook to extract the evaluation data, then deposit the data into 'completed-eval-data' as outlined once completed.

CONTRIBUTING:
Additional notebooks which are incomplete and require modifications, can be deposited into the 'notebooks' folder under the appropriate vendor name via pull request. Any completed evaluation data should be deposited into the 'completed-eval-data/outputs' folder for review. The name of the corresponding notebook (which, upon completion, should be deposited into the 'completed-eval-data/notebooks' folder) should be identical to the name of the notebook with the suffix '-data'.

Before beginning notebook modification, create an issue in the repo for visibility.

Please create an issue if any part of these instructions are unclear, or if you need assistance clearing a blocker to complete your eval.

GG everybody!