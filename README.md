# General Overview of Data Mining

## LaTeX Advice

You may wish to use [Overleaf](http://www.overleaf.com) to type up LaTeX, which has most of the packages that would be needed. Otherwise, for Macs, you can download [MacTeX](https://www.tug.org/mactex/).

## Homework Template Files

This templated repository has the following files

* `assignment1_template.tex` - You can edit this for your assignment. If you do, make sure you rename it to `assignment1.tex` so that TA's know which file to compile and grade.
* assignment1_questions.pdf - These are the questions for the assignment.

## Submission Guidelines

At the end of this assignment, your submission will point to a repository, where the following files will be reviewed and subsequently graded:

* A "Dockerfile" specifying what packages that you've used
* `assignment1.tex` file with your homework writeup
* `assignment1.pdf` file of the compiled version of your `*.tex` file
* `assignment1.py` file of your working code

None of the other files in that repository will be reviewed. You can however, have a directory structure for supporting files. For example, the following repository structure could help keep your top level directory clean.

```
./
Dockerfile
assignment1.tex
assignment1.pdf
assignment1.py
./images
  graph_for_question-1.jpg
  results_for_question-2.jpg
./tex
  question_2_proof.tex
./code
  helper_functions.py
```

Do _NOT_ include data into your Git repository.
