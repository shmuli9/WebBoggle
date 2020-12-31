# WebBoggle

#### The aim of this application is to solve the board game Boggle(TM)

My solution recursively searches the entire board, but significant speed optimisations were achieved by pruning search 
branches with the use of a prepared dictionary, built with a linked-list type data structure (not quite a linked list as
the data structure looks like `WTNode{data: str, isWord: boolean, children ={"A" : nodeA, "B": nodeB, ...}}`). 

Not only are the words returned, but also coordinates (as though the Boggle board is represented in a 2D array, ie 1,0 
for 1st letter on the 2nd row). This is so that a graphical representation can be made of the words on the board. 
The data structure is a dictionary `{ "WORD": ["1,0", "0,1", "0,2", "1,3"] ...}`.

WordTree generation, from a word list of 279,496 words, takes around 2s. Note, this is done once per application run, 
not once per Board search. 

Typical Board search speed on my laptop (CPU: i7-8550u, SSD, RAM: 16GB) is in the region of **1-7ms**.
Over 10,000 randomly generated boards, the average speed was 1.67ms, max 7.999ms, min 0.0ms (ie, too small for python to count)

On my recently purchased laptop (CPU: R7-4800u, Nvme SSD, RAM: 16GB) 10,000 randomly generated boards take around 1.45ms 
(max: 6.000ms, min: 0.0ms)

### Optimisations

I implemented several optimisations in my code. I aim to list and explain them all here.

1.  Once a word is found, the final node in the word has its isWord property is set to False. This operation results in 
"voided words", which are tracked so that they can be reset for every new board search
    
    **Why?** This optimisation is done to prevent words being "found" again and producing duplicates. This optimisation 
    does away with the need for the duplicates_analysis function (found in solver.py)

2.  Once a word is found I try to determine if the node should be voided (this is different to the isWord property) by 
looking at all children of the the final node in the word, and if there are no children or all children are themselves 
void, then this node is voided as well. This operation results in "voided nodes", which are tracked so that they can be 
reset for every new board search

    **Why?** This optimisation is done to eliminate nodes that aren't words and don't lead to words from later searches 
    on the same board, potentially saving time going down this path
    
3.  Similar to optimisation #2, when leaving a node, I check if the node has no children or all it's children are 
themselves void, in which case this node is voided. Similarly to #2, voided nodes are tracked so that they can be reset 
for every new board search

    **Why?** This optimisation is done to eliminate nodes that aren't words and don't lead to words from later searches 
    on the same board potentially saving time going down this path
    
    
Optimisation #2 and #3 dont show a notable speed improvement on a regular 4x4 boggle board, but I think that this code 
is optimal and perhaps could be of use in larger NxN boards

### Run
On Windows: 
```
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
.\reset_db.cmd
flask run
```

On Linux:
```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
source reset_db.cmd
python app.py
```

### Acknowledgments:

  - Segments of my code were forked from or modified based on, code written by [Daniel Samet](https://github.com/CouchMaster789)
  - The web app, including HTML, and backend code, is almost entirely the work of [Daniel Samet](https://github.com/CouchMaster789) (thanks!)
  - Thanks Dr Arman Khouzani for the Linux install scripts! (I was using an IDE, and overlooked this 😯)