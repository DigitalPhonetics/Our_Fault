# Sumary of data in this folder

## Miscommunication Annotations (miscom_summary.csv)
This is a summary document of the number of miscommunication events and the number of turns of miscommunication for each user who also filled out a survey.
The document is a csv using `;` as the delimator

For information on anonymous users, please see the full miscommunication table (`miscommunication_table.csv`).

**Columns:**
* user: the code the user received on submission of survey (consistant with all other files)
* num_events: the number of discrete miscommunication events in each user's communication with the system
* total_turns: the total number of turns each user was in which were part of a miscommunication event 
* classification_by_event: 0 -> no miscommunication events; 1 -> few miscommunication events (1-2) (below average to average); 2 -> many miscommunication events (3+)(greater than average)
* classification_by_turns: 0 -> no turns of miscommunication; 1 -> few turns of miscommunication (1-11) (below average to average); 2 -> many turns of miscommunication (12+)(greater than average)
* strategies: An encoding for which strategies were employed in each users communication with the system which resolved the miscommunication. Per event only the strategy which resulted in the end of the miscommunication is recorded (although the user or system may have employed other methods during a miscommunication event which were not sucessful). This means per event, only a single strategy was recorded, however if the user had multiple miscommunication events, there may be multiple strategies. Below is the mapping between numbers which appear in the column and the corresponding strategy they represent:
  * 'Correct System': **0** _(user corrects a false assumption or misunderstanding on the system's side)_
  * 'System asks question': **1** _(system either asks the user a new question or repeats one it has previously asked)_
  * 'System next module': **2**, _(miscommunication is resolved when the system misunderstands the user and moves on to the next module, ending previous discussion)_
  * 'System provides info': **3** _(system provides either new information or repeats information it has previously provided)_
  * 'Tries Something new': **4** _(user tries a new dialog action)_
  * 'agrees with system': **5** _(user gives up arguing and agrees with the system/just tries to get through dialog as quickly as possible)_
  * 'asks for clarification': **6** _(user asks system for clarification)_
  * 'dialog ends': **7** _(dialog ends before any resolution was reached)_
  * 'rephrases': **8** _(user rephrases their input)_
  * 'restarts': **9** _(user restarts either the current module or refreshes the page and restarts the entire game)_
  * 'solves module without help': **10** _(user solves the module by trial and error without help from the system)_
  * 'unnoticed': **11** _(a misunderstanding is simply not noticed)_

## ContentAnalysis
* The conent analysis documents are excel documents counting the number of times a code appeared in the user survery responses, these are broken into two files for clarity (what the user thougth was easy/hard for the dialog partner and the mental models they formed about the dialog partner) 
* Annoations for both of these files were performed by two annotators not familiar with the experimental design or aims of the study

## Miscommunication_annotations.xlsx
* Provides a more detailed/ human friendly representation of the data in `miscom_summary.csv`

## MTurkTrustStudy_finalResultsWithDialogAnalysis.xslx
* Provides a summary of survery results and miscommunication annotations in one combined document

## user_acts.txt
* Provides an automatically generated user act annotation for each user utterance (the same one used by the system during the interaction)
* Data is structured so the user id appears first and then the user acts for each user turn in the dialog

## sys_acts.txt
* Provides an automatically generated system act annotation for each system utterance (generated after the experiment, so may have some errors)
* Data is structured so the user id appears first and then the system acts for each system turn in the dialog
