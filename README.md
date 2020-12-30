# Machine Learning project

## Student info
- **Name**: Bontinck Lennert
- **StudentID**: 568702
- **Affiliation**: VUB - Master Computer Science: AI

## Main files
- [Intermediate report](Intermediate_Report_ML_Project_Bontinck_Lennert_568702_VUB.pdf)
- [Final report - Coming](Final_Report_ML_Project_Bontinck_Lennert_568702_VUB.pdf)

## Installing required libraries and files
The required libraries can be installed by executing the following command from the root of this directory.
> pip install -r requirements.txt

Some of the required files are left out to limit the size of this GitHub repository. This includes:
- "feautures"  folder inside the provided code folder AND  the developed code folder.
- "images" folder inside the code folder, inside this folder are the test and train folder as provided by the Kaggle competition. 


## Feedback:

Don’t put in too much fluff and repeat stuff. I know you mean well, but it sometimes hinders readability of your document. Also, 25p is simply way too much for the intermediate (and even final) report.

> - The final report tried to get rid of this "fluff". The page count is still high but taking into account large figures and separation pages for parts it's better.

Why do you leave out features? Or what do you mean by ‘feature amounts’?

> - This was a bad usage of the term feature amounts. The amount of clusters is what was actually meant. This has been changed everywhere (hopefully).

A bit more text on figures (it’s great that you include them though)

> - Revision of the figures and better captions and in text discussion.

Include all scores, also Kaggle scores.

> - For many of the tested settings I didn't upload a test to Kaggle. I've now tried to include some more of the Kaggle scores.

Numbers in your CM!

> - TODO

Try to put your figures in the text for readability.

> - Figures have now been added in text with only the ones that are supplementary added to the extra figures list.

Preprocessing is a crucial part of the model, you mention the opposite.

> - This comment in the report was meant that the focus for this assignment (for me) will mostly be on understanding and testing different models, not doing image manipulations in preprocessing. 

SURF is left out by intention, if you want to use it, you can follow some tips in the first part of the vbow notebook.

> - I don't seem to have the license nor am I able to get it, this is why i didn't use SURF nor did I experiment with changing the images since a license for SIFT was also not present and I used the SIFT descriptor since it performed the best.

Your comment on the class_weight parameter is great, it shows that you ask the right questions. I won’t give away the actual answer to it, though, since it is important for your progress/report. Your next comment is related to it: I also can’t answer it directly, but I like that you think about these things, so good job already.

> - TODO -> betere manier van test split


**General feedback:**

Excellent start. I see a lot of good things, but also some (small) errors, which is normal of course.

Model analysis! 

Also, even though this does not affect your grades, I am genuinely surprised your Kaggle score is not better based on your clear efforts.
