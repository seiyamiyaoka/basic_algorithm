# HTTPRouter using a Trie

## About data structure and algorithm

I am using a tree structure.
Also, the node of the tree is held by hashmap.

## About Order complexity

- RouteTrie
  - insert(insert(self, path_routes, handler))
    - $O(n)$. This is because it loops to the end of path.
- Router
  - lookup(self, path)
    - $O(n)$. The path of the received string is converted to an array and looped.

## About Space complexity
- RouteTrie
  - __init__(self, path, handler)
    - $O(1)$.
  - insert(self, path_routes, handler)
    - $O(n)$. Since the path_routes argument is an array, it requires a space complexity of $O(n)$.
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
    - $O(n)$.
      - This is because we use the paths variable, which is a string converted to an array.
## About implementation

It uses the Trie data structure.

When creating various errors by creating an error node, it can be managed in a hierarchical structure.

This means that you can create an error handling node just as you would create a web server node.