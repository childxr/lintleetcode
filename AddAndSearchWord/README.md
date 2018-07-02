## Add and Search Word - Data structure design

### Description

Design a data structure that supports the following two operations: `addWord(word) and search(word)`

search(word) can search a **literal word** or a **regular expression** string containing only letters a-z or `.`.

A `.` means it can represent any one letter.

You may assume that all words are consist of `lowercase letters a-z`.

### Example

addWord("bad")

addWord("dad")

addWord("mad")

search("pad")  // return false

search("bad")  // return true

search(".ad")  // return true

search("b..")  // return true
