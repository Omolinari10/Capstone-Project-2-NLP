# Capstone-Project-2-NLP Translation Model
------------------------------------------

Project files:
-------------
* Capstone Project 2 - Milestone Report 1.pdf (Report explaining what was done till this point: 2020/12/13)
* Capstone Project 2 - Milestone Report 1.pptx (Slides explaining what was done till this point: 2020/12/13)
* requirements.txt (Python packages as of 2020/12/13)
* CAPSTONE PROJECT 2 - NLP - 1) Environment and Data Set Up.ipynb
* CAPSTONE PROJECT 2 - NLP - 2) Processing the data.ipynb
* CAPSTONE PROJECT 2 - NLP - 3) Modeling.ipynb
* nlp_helper_functions (directory)
  * my_tokenize.py
  * my_pad.py
  * my_preprocess.py
  
 Data files:
 ----------
 * europarl-v7.fr-en.en (European Parliament English sentences from transcripts)
 * europarl-v7.fr-en.fr (European Parliament French sentences from transcripts)

What it's about:
---------------
This is my second Capstone Project on SpringBoard.com. For this project I chose to build a Natural Language Processing Model (NLP) using an Embedded Recurrent Neural Networks(RNN) Model to be able to automatically translate English sentences into French sentences.


The machine set-up:
------------------
I signed up for an account on the Google Cloud Platform to get more processing power than my own machine could afford. Google Cloud Platform comes with a $300 credit upon first account opening. This is enough for folks to get their feet wet learning how to build instances on the cloud and be able to use Virtual Machines with more processing power than they can normally afford on their own. I spawned an instance with a Debian Linux OS with a good CPU and an added NVIDIA K80 GPU. I created a Google bucket where I uploaded my project's input files.


The language used:
-----------------
I used Python 3 for this project.


The Input files:
---------------
They input files can be found at this URL: http://www.statmt.org/europarl/ and this download "parallel corpus French-English, 194 MB, 04/1996-11/2011"
That download provides you with fr-en.tgz which when uncompressed results in two files: europarl-v7.fr-en.en and europarl-v7.fr-en.fr


The Python code files:
---------------------
The main code is divided into three Jupyter Notebooks: 
* 1) CAPSTONE PROJECT 2 - NLP - 1) Environment and Data Set Up.ipynb
* 2) CAPSTONE PROJECT 2 - NLP - 2) Processing the data.ipynb
* 3) CAPSTONE PROJECT 2 - NLP - 3) Modeling.ipynb
 
There are 3 .py files that are used within the 2) and 3) Jupyter Notebooks. They are found in the nlp_helper_functions directory. They are: my_tokenize.py, my_pad.py, and my_preprocess.py. As named, the first tokenizes lists of sentences, the second pads them and the third calls the first two to prepare the data for modeling.

The requirements.txt file has the packages (and their versions) that were necessary to build this model.


How to run the project:
----------------------
This project was run on a Conda environment containing the packages and their versions from the requirements file. All three .ipynb files and the nlp_helper_functions directory that contains the .py files need to be in the same directory.

CAPSTONE PROJECT 2 - NLP - 1) Environment and Data Set Up.ipynb will be run first, followed by CAPSTONE PROJECT 2 - NLP - 2) Processing the data.ipynb, and finally CAPSTONE PROJECT 2 - NLP - 3) Modeling.ipynb

Documents:
---------
* Capstone Project 2 - Milestone Report 1.pdf (Report explaining what was done till this point: 2020/12/13)
* Capstone Project 2 - Milestone Report 1.pptx (Slides explaining what was done till this point: 2020/12/13)
* requirements.txt (as of 2020/12/13)
