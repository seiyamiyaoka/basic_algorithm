class RouteTrie:
  # 本当のトップのnode
  def __init__(self, path, handler):
    # ルートpathのnode
    self.root_node = RouteTrieNode(path, handler)

  def insert(self, path_routes, handler):
    # 再帰的に追加して最も深いノードのハンドラーを追加する
    node = self.root_node
    end_path = path_routes[-1]
    for path in path_routes:
      if path and path not in node.children:
        if path == end_path:
          node.insert(path, handler)
        else:
          node.insert(path)
        node = node.children[path]

class RouteTrieNode:
  # 一つ一つのnode
  def __init__(self, path, handler):
    self.path = path
    self.handler = handler
    self.children = {}

  def insert(self, path, handler=""):
    self.children[path] = RouteTrieNode(path, handler)
    # nodeの追加

class Router:
  def __init__(self, root_handler, error_handler):
    self.root = RouteTrie("/", root_handler)
    self.error = RouteTrie("/error", error_handler)

  def add_handler(self, path, handler):
    root = self.root
    if root:
      root.insert(path.split("/"), handler)

  def lookup(self, path):
    node = self.root.root_node
    error = self.error.root_node
    paths = path.split("/")
    last_path = paths[-1]

    if path == "":
      return error.handler

    if last_path == '':
      paths = paths[:-1]
      last_path = paths[-1]

    for s_path in paths:
      if s_path != '' and s_path != '/' and s_path:
        if s_path in node.children:
          node = node.children[s_path]

    if node.path and node.path == last_path and node.handler:
      return node.handler
    else:
      return error.handler



router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/blogs", "blogs handler")

print(router.lookup(""))
# not found handler
print(router.lookup("/"))
# not found handler
print(router.lookup("/home"))
# not found handler
print(router.lookup("/home/about"))
# about handler
print(router.lookup("/home/about/"))
# about handler
print(router.lookup("/home/about/me"))
# not found handler