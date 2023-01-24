T5HTML
======

Converts a text file into HTML. 

The text must be formatted according to the rules of a Trivial Text Tree To
Trivial HTML (T5HTML).


## Disclaimers

This **Read.Me** is a link to doc/Read.us!
For **licensing** look for meta/license.


## Example

```t5html
## t5html
DOCTYPE := <!DOCTYPE html>
METADESC := meta name=description
METAPROP := meta content_
JSBASE := js

!! DOCTYPE
html
    head
        METADESC content=example for t5html
    body

## vi: set et ai ts=3 sw=3 ft=t5html :
```


## t5html-Syntax

    - Line oriented: single line processing, except for explicit line
      continuations `..`
    - Word oriented: elements are separated by spaces, e.g. keep attribute-names
      and attribute-values together, e.g.: `href=images/icon.png`
    - Indentation **must** be **3** and **don't use tabs**. Every indentation
      represents an hierarchical step-down. An indentation makes the previous
      line the parent of the new line. The reason for 3 is not arbitrary and is
      basically the result of the line-continuation symbol: `..`!


## For Developers

Start with `Read.4dev` in the `doc` directory.


[//]: # vi: set et ts=4 sw=4 ai ft=markdown tw=80 cc=+0 spl=en:
