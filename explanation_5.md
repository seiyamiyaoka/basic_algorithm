# Autocomplete with Tries

## About data structure and algorithm

I am using a tree structure.
Also, the node of the tree is held by hashmap.

## About Order complexity
$O(n ^ 2)$

The amount of calculation is $O(n^2)$ because there is a double loop of the for statement in the suffixes method.

## About Space complexity
- TrieNode
  - __init__(self)
    - $O(1)$. This is to hold empty dictionaries and bool values.
  - insert(self, char)
    - $O(1)$. This is because one node is set for one key.
  - suffixes(self, suffix='', is_stop=False)
    - $O(n ^ 2)$. This is because a new array is retained each time recursive processing is performed.
- Trie
  - __init__(self)
    - $O(1)$
  - insert(self, word)
    - $O(1)$
      - This function is looping, but the node variable is reused so no new space is needed.
  - find(self, prefix)
    - $O(1)$

## About implementation

It uses the Trie data structure.

When getting suffixes, if it is a word but has children, recursive processing is newly executed.
