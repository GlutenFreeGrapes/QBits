# yet-another-qb-reader
This program of mine will join the ever-growing list of quizbowl question readers out there. I decided to try and combine tossup readers like Protobowl and QuizBug and bonus readers like pkbot to create an all-in-one solo studying program for reading questions. 

More specifically, I plan to use the QuizDB database in order to access questions, then use simple Python GUI functions in order to have the program display the words one at a time. I plan on giving the tossups the same functionality as in protobowl and likewise with bonuses and pkbot, except for the fact that pkbot has a helpful function where even if the program may not initially detect your answer as being correct you can still say that you did in fact get it right, so I plan on giving the tossups this functionality alongside typo correction/spellcheck. 
## How to use
when the program is run, you will be prompted with a screen asking for inputs on what categories you want, difficulties, etc. Use the dropdown menus to select your options. There are also options for changing the time interval between words and whether you want tossups only, bonuses only, or tossups and bonuses. 

When you hit the "Go" button, the windo should momentarily close out only for another to open. The screen should read "Press [Next/Skip] to start". Press the Next/Skip button, and the reading should start. As of now I have not bound keys to the buttons, so no hitting [space] to buzz or [enter] to submit your answer. 

When you hit [Go], at the bottom of the screen there should be several buttons(all should be disabled except the [Next/Skip] button), a space to type answers in, and a large slider. The slider allows you to live-adjust the speed at which the program reads you the questions. 

### Tossups
When you start the reading, the program will read the question one word at a time. The [Next/Skip] button stays enabled in case you want to skip questions. The [Buzz] button will be enabled so that you can buzz in, and when you do, it disables itself and the [Next/Skip] button, and enables the text entry box, and a timer for 8 seconds. When you have finished typing, hit the [Enter] button(in the GUI, not on your keyboard) and the program should either display the question and the correct answer or prompt you with a message asking whether your provided answer was correct. Once this happens, you should see that your number of tossups you've heard, number of tossup points, points per 20 tossups heard, and your powers/10s/negs ratio will have updated. When you have run out of tossups, everything will be disabled, but you will see your stats. 
### Bonuses

### Tossups and Bonuses
This option basically has the same functionality as tossups and bonuses, just combined. I've made it such that even if you may have gotten a tossup wrong you will still be read a bonus after it, because I have the program simply alternate between tossups and bonuses. 
