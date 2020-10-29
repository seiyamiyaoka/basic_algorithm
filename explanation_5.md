# Autocomplete with Tries

## About data structure and algorithm

I am using a tree structure.
Also, the node of the tree is held by hashmap.

## About Order complexity
- TrieNode
  - insert(self, char)
    - $O(1)$
  - suffixes(self, suffix='', is_stop=False) // 間違っているので直すが理由がわかっていない
    - $O(n ^ n)$.This is because the suffixes method is executed recursively for the number of keys.
- Trie
  - insert(self, word) and find(self, prefix)
    - $O(n * m)$. First of all, loop the prefix character. this is `n`.The worst case is when character is included in the children of node every time. It takes a time complexity of $O(m)$ to make sure that the dict contains a particular key. this is `m`. Therefore $O(n * m)$.

## About Space complexity
- TrieNode
  - __init__(self)
    - $O(1)$. This is to hold empty dictionaries and bool values.
  - insert(self, char)
    - $O(1)$. This is because one node is set for one key.
  - suffixes(self, suffix='', is_stop=False)
    - $O(n ^ n)$. This is because the suffixes method is executed recursively for the number of keys.
- Trie
  - __init__(self)
    - $O(1)$
  - insert(self, word)
    - $O(n * m)$
      - This is because space is used to check the hash table for the number of characters.
  - find(self, prefix)
    - $O(n * m)$
      - This is because space is used to check the hash table for the number of characters.

## About implementation

It uses the Trie data structure.

When getting suffixes, if it is a word but has children, recursive processing is newly executed.
