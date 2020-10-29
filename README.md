# WebBoggle

#### The aim of this application is to solve the board game Boggle(TM)

My solution recursively searches the entire board, but significant speed optimisiations were achieved by pruning search 
branches with the use of a prepared dictionary, built with a linked-list type data structure (not quite a linked list as
the data structure looks like `WTNode{data: str, isWord: boolean, children ={"A" : nodeA, "B": nodeB, ...}}`)

WordTree generation, from a word list of 279,496 words, takes around 2s. Note, this is done once per application run, 
not once per Board. 

Typical Board search speed on my laptop (CPU: i7-8550u, SSD, RAM: 16GB) is in the region of **1-7ms**.
Over 10,000 randomly generated boards, the average speed was 1.67ms, max 7.999ms, min 0.0ms(ie, too small for python to count)

On my recently purchased laptop (CPU: R7-4800u, Nvme SSD, RAM: 16GB) 10,000 randomly generated boards take around 1.45ms 
(max: 6.000ms, min: 0.0ms)

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