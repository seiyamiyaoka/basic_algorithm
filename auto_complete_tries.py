class TrieNode:
  def __init__(self):
    self.is_word = False
    self.children = {}

  def insert(self, char):
    self.children[char] = TrieNode()

  def suffixes(self, suffix='', is_stop=False):
    is_duplicate = False

    keys = self.children.keys()
    if len(keys) == 0 or is_stop is True:
      return suffix
    else:
      paths = []
      result_a = ""

      for key in keys:
        result = self.children[key].suffixes(key)

        if self.is_word and is_duplicate is False:
          result_a = self.suffixes(suffix, True)

        if result_a and is_duplicate is False:
          is_duplicate = True
          paths.append(result_a)
        for element in result:
          paths.append(suffix + element)
      return paths

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root

    for char in word:
      if char not in node.children:
        node.insert(char)
      node = node.children[char]
    node.is_word = True

  def find(self, prefix):
    node = self.root

    for char in prefix:
      if char in node.children:
        node = node.children[char]
      else:
        return None
    return node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
result = MyTrie.find('a')
print(result.suffixes())

# Trieデータ構造作成
# 特定のnodeを検出
# childrenのkeyを次々と取得してkeyがなくなるまでループ
# keyが無くなったら最後の文字を返す
# 再帰的に実行しているので呼び出し元に文字列を返して以前のsuffixの足していきそれを探索済みpathに追加する
# 