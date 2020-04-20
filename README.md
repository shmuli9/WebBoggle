#WebBoggle

####The aim of this application is to solve the board game Boggle(TM)
My solution recursively searches the entire board, but significant speed optimisiations were achived by pruning search branches with the use of a prepared dictionary, built with a linked-list type data structure (not quite a linked list as the data structure looks like `WTNode{data: str, isWord: boolean, children ={"A" : nodeA, "B": nodeB, ...}}`)
Typical Board search speed on my laptop (CPU: i7-8550u, SSD, RAM: 16GB) is in the region of 2-7ms

###Acknowlegments:
  - Segments of my code were forked from or modified based on, code written by Daniel Samet
  - The web app, including HTML, and backend code, is almost entirely the work of Daniel Samet (thanks!)

