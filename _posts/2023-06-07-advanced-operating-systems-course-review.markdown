---
title: "CMU 15-712 Advanced Operating Systems and Distributed Systems Course Review"
layout: post
tags: [courses, systems]
cover: santorini_church.avif
cover_preview: santorini_church.avif
caption: Three Bells of Fira, Thera, Greece
class: post-template
author: fanpu
toc:
  sidebar: left
giscus_comments: true
# published: false
description: >
---

This semester (Spring 2023), I took [15-712 Advanced Operating Systems and
Distributed Systems](https://www.cs.cmu.edu/~15712/) under professor [Phil
Gibbons](http://www.cs.cmu.edu/~gibbons/) and his TA and also PhD advisee [Val
Choung](http://nicebowlofsoup.com/). This was the first time I took
a class under Phil (he usually teaches either this class or [15-745 Optimizing
Compilers for Modern
Architectures](http://www.cs.cmu.edu/afs/cs/academic/class/15745-s19/www/)),
and interestingly enough this was the third time Val was my TA, the 
previous two times being 15-330 Introduction to Computer Security
in Fall 2019 and [15-410 Operating System Design and Implementation](https://www.cs.cmu.edu/~410/)
in Spring 2020.

# Overall Impression
This class exceeded my expectations significantly.
I found it especially meaningful and apt since this was my last systems class before I
graduate, and the topics and discussions from class helped to unify all the
systems concepts that I had learnt from previous classes into a nice package
informed by common underlying principles: from distributed systems, to
networking, databases, filesystems, operating systems, and even machine learning
systems. 

# Why I Took The Class
I had to take a systems class this semester to fulfill my graduation
requirements for the MSCS program. I initially did include this class in my
shortlist of systems classes to take, but then thought it was just going to be a
paper reading class (not that I had been in one of such classes before, but it
just did not sound very interesting and felt like something I could do by myself
asynchronously after I graduate) and therefore was quite hesitant to take it.

As such, during registration week I settled on [15-618 Parallel Computer Architecture and
Programming](https://www.cs.cmu.edu/~418/),
since it included topics on GPU programming that aligned with my current
interests in machine learning. However, I did not feel like the class was
sufficiently challenging for me after the first lecture, as it was a bit too
slow-paced and simple for my liking as I already had exposure to most of the
topics from other system classes that I had taken. I decided to switch
to 15-712, and I knew immediately that it was the right class for me after the
first lecture. 

In a sense, this class was a hidden gem and I was really glad that I ended up
taking it.

# The First Lecture
The first lecture went through 2 "Wisdom Papers", which no one was expected
to have read yet as it was the first class. You can refer
to the [slides here](https://www.cs.cmu.edu/~15712/lectures/01-intro.pdf) if you are curious.

The first paper, [Mythical Man-Month: Essays on Software
Engineering](https://www.cs.cmu.edu/~15712/papers/mythicalmanmonth00fred.pdf)
is a book by Turing-award winner Fred Brooks. It is about many of his observations
and principles on software engineering based on his own vast experiences. What
really brought it home to me was that a couple of them were also things that I
had some suspicions about previously, but never really thought it was universally
applicable, and thought they were simply artifacts of the way I approached things.

For instance, one of the principles is "Plan to Throw One Away", meaning that
one should first build a worthwhile system in a short amount of time, and then
re-build a better second version with the benefit of hindsight. This is because
one would end up having to re-build the system anyway after being confronted
with change and feedback, and also due to the following observation on program
maintenance:

> "Program maintenance is an entropy-increasing
> process, and even its most skillful execution only
> delays the subsidence of the system into unfixable
> obsolescence"

This had many parallels with my own experiences. For instance, my group ended up
having 4 major re-writes of our kernel during 15-410, and I also did a complete
re-write of my CloudFS filesystem for my 18-746 project. Similarly, many of my
internship projects were also re-writes and improvements on design of existing
systems that had accumulated too much technical debt. It does seem
a lot more reasonable to plan for this eventual change to begin with.

The paper also contained a lot of other great advice, such as the
importance of conceptual integrity to separate architecture
from implementation, structuring a team in a "surgical" fashion to drive software
development where the best programmer leads the most critical development
work like a surgeon and directs others on the other aspects, and of
course the famous Brook's law:

> “Adding manpower to a late
> software project makes it later”

The second paper, [You and Your
Research](https://www.cs.cmu.edu/~15712/papers/hamming86.pdf) by Richard Hamming
(of Hamming code fame)




## Class Structure
There are three main components to the class. 

1.  Before each lecture, the class is assigned a paper to read, and a paper summary to be submitted.
    In the paper summary, you'll write about the 3 most important things in the paper, 1 most
    glaring deficiency of the paper (even highly celebrated papers have faults!), and a conclusion
    on how you will use lessons from this paper to inform you on how you will build systems in the future.
    It took me on average 2-4 hours to read each paper and around 15 minutes for the summary.

    The lectures for this class are front-loaded, meaning that during the first
    two-thirds of the semester, you will meet 3 times a week for 80 minutes each,
    while there will be no lectures at all during the final third of the semester,
    and so "on average" throughout the semester you will meet twice a week. This is so that
    students have enough knowledge and content to begin working on their course
    projects early on in the semester.

2.  A semester-long course project with a significant systems component in
    groups of three. This will begin in earnest after a third of the semester,
    and all the project groups met with Phil and the TA Val once every two weeks.
    The deliverables include a project proposal, an interim report, a final
    presentation, and a final report.

3.  Two midterm exams, which are taken during class time.

The first half of the class took us on a whirlwind tour through many [SIGOPS Hall
of Fame papers](https://www.sigops.org/awards/hof/), which the award description
states was "instituted in 2005 to recognize the most influential Operating
Systems papers that were published at least ten years in the past".
Reading through the papers helped to consolidate a lot of the
knowledge that I learned in previous systems classes, and it was cool to see
how decades ago many of these ideas that were once unappreciated or heavily
criticized now form the bedrock of many of the systems that we use today.


As a seminar-based class, one of the most surprising things for me was how fun
and valuable the class discussions were.  It was especially enlightening to
hear the comments of Ph.D. students who are working in systems and other fields
in computer science, who often had very different critiques and opinions of
the papers than what I had come up with, which often led me to wonder how they
got their perspectives and what their background is like. 
This was particularly true when someone mentioned glaring deficiencies and
problems with the paper that I had completely not even thought of.

However, one thing that made me sad was that attendance in class
started to fall after the halfway point of the semester. This
included quite a few of the students who used to give very insightful
and interesting responses, and so the diversity of perspectives of the
discussions as a whole suffered.
While attendance is not graded or required, actively participating in the
discussions and being engaged in lecture is one of the most valuable
takeaways from this class, and positively impacts not just you but also
your classmates, and so I would strongly encourage anyone interested in the
class to attend all the lectures that you can.

Another aspect of the class that I really appreciated was how Phil taught us a
lot of the spirit and tribal knowledge of doing CS research. These were often
presented as off-hand remarks while presenting the context or background of a
paper, and provided insight into the zeitgeist of the time, the motivations
and challenges that the paper authors faced, and what the authors went on to
do in the future based on the impact (or lack of impact at that time)
of their work.

As someone who has not done a long-term research project with a faculty member
but am thinking about possibly doing a Ph.D. in the future, all of these were
valuable wisdom as they are not things that you can pick up easily yourself
from reading past papers or books. In fact, it almost felt as if I had my own
Ph.D. advisor at times, who sprinkled trinkles of advice each class.

I also really appreciated the personal attention that Phil and Val gave to us
by meeting with us every other week for our course projects. 
This is especially so if you consider that many advisors already have trouble
meeting their own Ph.D. students for an hour a week, whereas in this case the
course staff dedicated half an hour every two weeks for every single group in
the class (there were around 10), which was true dedication.
I will admit that I did not live up to my end of the bargain by spending
as much time on the project as I would have wanted to (compared to when I took 15-410).
This is due to a combination of high workloads from other classes, the fact 
that we faced a few unexpected issues when working on the project that forced us
to return to the drawing boards several times, and how it was hard to get
everyone's schedules aligned to work on things as my project partners were also
very busy with their own research.

Our course project was on automatic optimal scheduling of data in dynamic neural
networks over heterogeneous GPUs for inference tasks in a pipeline-parallelism
fashion. This means that when a model is too large to fit on a single GPU
but instead has to be distributed across multiple GPUs, we aim to solve the problem
of finding the optimal way to perform this split in the presence of dynamism
in the network. In our case we focused on input dynamism, meaning that the
sizes of the inputs can vary, which can result in different execution times in different
segments of the network. We built a system called `DynPartition`, 
a reinforcement-learning based scheduler that uses Deep-Q Learning to learn
the optimal way of performing this split.

We had some positive results but with some caveats 
thought it was a great experience working with PhD students and other smarter
people and to have learnt from them. It was also really cool to see the
breadth and depth of projects presented during the final presentation. I
cannot recommend this course enough to anyone who has the sufficient
pre-requisites, which will allow them to truly appreciate the content in the
class.

# Who Is Suitable For The Class
When I took the class, all the students were either Masters or Ph.D. students.
However, strong undergraduates with sufficient systems background would
also do well in the class.

# Acknowledgements
I would like to express my gratitude to [Albert
Gao](https://adbforlife.github.io/) who took the class together with me for
helping to proofread this article. Shoutout to [Abigale
Kim](https://abigalekim.github.io/) as well for taking the class together with
Albert and I, where we formed a lively discussion group every class and made
many memories.

I would also like to thank my project groupmates [Vivswan
Shah](https://vivswan.github.io/) and [Yudong
Liu](https://www.linkedin.com/in/yudong-liu-510929205/), both of whom have far
more research experience than me and allowed me to learn many things from
working with them.