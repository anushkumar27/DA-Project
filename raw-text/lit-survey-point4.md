Introduction to context of problem:
===================================

For a course, there may exist dependencies (often represented as prerequisites)
that give us an idea of the skills and knowledge required to perform in a satisfactory
manner in the particular course. Thus, it stands to reason that using these
dependencies, there must be a way to predict a student's performance in the course
(of course prior to having attempted the course) using the dependencies and an
data of how well the student has performed in the dependencies of the course. For
example, a course on algorithms depends on a solid foundation in discrete mathematics
and logic, data structures, etc. If it is ascertained that the student has strong
skills in the dependencies, then their chances of performing well in said course
increases. Thus, it also stands to reason that the student need not spend as much
time studying that subject to be able to perform well. In this manner, we can
generate the most optimal study schedule for a student to be able to perform well
academically.

While it may be the case that the above process seems simple enough for a person
to do themselves, often times, in a classroom setting, it is difficult for a single
teacher to accurately judge every single one their students' aptitude and determine
the appropriate course of action to improve their performance. In addition, this
process would require that the teacher get to know each student's aptitude and
skills before they can advise the student on fruitful application of their time
and efforts. Thus, there would be considerable benefit to having a system by which
we can advice a student on the necessary actions that need to be taken to ensure
that their performance is satisfactory, prior to have any data on their current
performance in the course. Such advice would come through the form of a 'study schedule'
that instructs the student of the time needed to be spent in order to achieve
academic success.

Our problem is to gain an understanding of a student's aptitude and
proficiency in various courses through various data sources like test scores,
project grades, etc. and determining the dependencies between a course and its
prerequisites use the information to generate the study schedule. The first step
would be to determine the appropriate metric to measure the level of dependencies
between the course and prerequisites, followed by determining the model needed
to solve the problem with the dependency measure and student's previous performance
on the prerequisites. Time permitting, we may also be able to increase the granularity
the of the dependency analysis from course level to course unit/chapter levels,
and to use the data to more accurately determine the student's study schedule.
