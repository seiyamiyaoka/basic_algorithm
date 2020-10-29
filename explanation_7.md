# HTTPRouter using a Trie

## About data structure and algorithm

I am using a tree structure.
Also, the node of the tree is held by hashmap.

## About Order complexity

- RouteTrie
  - insert(insert(self, path_routes, handler))
    - $O(n * m)$. This is because it loops to the end of path. this is `n`. It takes a time complexity of $O(m)$ to make sure that the dict contains a particular key. this is `m`. Therefore $O(n * m)$
- Router
  - lookup(self, path)
    - $O(n * m)$. Iterating the list requires `n` time complexity. It also requires $O(m)$ time complexity of m to see if children contain a particular path. This is because I'm using dict. Therefore $O(n * m)$.

## About Space complexity
- RouteTrie
  - __init__(self, path, handler)
    - $O(1)$.
  - insert(self, path_routes, handler)
    - $O(n * m)$. This is because space is used to check the hash table for the number of path_routes.
- RouteTrieNode
  - __init__(self, path, handler)
    - $O(n)$.
      - This is because hashmap is used for self.children.
  - insert(self, path, handler="")
    - $O(1)$
- Router
  - __init__(self, root_handler, error_handler)
    - $O(1)$.
  - add_handler(self, path, handler)
    - $O(1)$.
  - lookup(self, path)
    - $O(n * m)$.
      - This is because space is used to check the hash table for the number of paths.

## About implementation

It uses the Trie data structure.

When creating various errors by creating an error node, it can be managed in a hierarchical structure.

This means that you can create an error handling node just as you would create a web server node.