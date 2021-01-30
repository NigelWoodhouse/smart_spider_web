# Smart Spider Web
Utilizing genetic algorithms to show how a simple system is increasing in complexity to satisfy its function in the form of a spider web. Inspired by Richard Dawkins 1991 Christmas Lecture.

https://www.youtube.com/watch?v=QdtYRJqNe9I

Spiderwebs are a fantastic evolutionary adaptation. The wellbeing of the spider and reproductive success directly ties to the quality of its web -> that would be the more insects that a spider web could catch, the better fed the spider is, and the more likely the spider would be able to reproduce and pass its genetic information on to the next generation.

A spider web is an excellent way of exploring this form of genetic algorithms. The web's efficiency or fitness can be evaluated by the number of insects caught (more insects caught improves fitness) and the amount of web used (more web used decreases fitness).

To operate, either choose the Spiderweb_Artificial_Selection.py or Spiderweb_Natural_Selction.py. Download all of the .py files.

On the screen, nine spider webs are presented. The top left web is the parent web; the other eight are daughter webs. The red dots represent insects that may pass through the web. If they touch the black lines of the web, they are caught.

The Natural Selection automatically evaluates the fitness of each of the nine webs and uses the best web's properties to create a new generation. The cell will dip gray, showing which web has the best fitness.

The Artificial Selection allows the user to select which web they think is best via aesthetic means.

Overall, the program shows how something simple can increase in complexity to satisfy its niche better as would have been expected in the natural world. Regardless of the web's original configuration, all solutions will approach a circular shape with many internal webbings, exactly what we see in nature. 

![Alt text](/documentation/spiderwebs_gen1.PNG?raw=true "1st Generation")
 
 
![Alt text](/documentation/spiderwebs_gen25.PNG?raw=true "25th Generation")
 
 
![Alt text](/documentation/spiderwebs_gen80.PNG?raw=true "80th Generation")
