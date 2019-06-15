title: Fun With Ed(1)
date: 2019-06-15
slug: fun-with-ed
category: linux
summary: The most user-hostile editor ever created


The ed text editor was one of the first key elements of the Unix operating system.  It has been described as one of the most user-hostile text editors ever created.  It operates in two distinct modes: command and input.  Here are some fun examples you can use to impress onlookers at your next dinner party!

## Open a file 
```
ed tennyson.txt
226
```

## Print all lines 
```
,p
Cannon to right of them,
Cannon to left of them,
Cannon in front of them
Volley'd and thunder'd;
Storm'd at with shot and shell,
Boldly they rode and well,
Into the jaws of Death,
Into the mouth of Hell
Rode the six hundred.
```

## Print first line
```
1p
Cannon to right of them,
```

## Print last line
```
$p
Rode the six hundred.
```

## Edit last line
```
$p
Rode the six hundred.
s/six/nine/p
Rode the nine hundred.
```

## Escaping edit mode
To escape out of edit mode you simply need to have a single line with `.`
```
Rode the nine hundred.
.
```

## Append to a line
```
$a
Here is a new line
```

## Write buffer to file (save)
```
w <filename>
```

## Quit Ed(1)
```
q
```

As you can see there are lots of fun ways to edit a file with ed(1).  I just touched on the basics here.  There is an entire new world of editing possible when you include the use of regex.  Ed(1) is lightweight also!  Clocking in at about 117k, it's much smaller than vim or emacs.  For the scoop on all of its features see the man or info pages.


