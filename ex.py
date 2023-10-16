class Node():

  def __init__(self, data) -> None:
    self.data = data
    self.left = self.right = None
    self.height = 1

  def __str__(self) -> str:
    return str(self.data)


class AVLTree():

  def __init__(self) -> None:
    self.root = None

  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self.root = self._insert(data, self.root)

  def _insert(self, data, root):
    if data < root.data:
      if root.left is None:
        root.left = Node(data)
      else:
        root.left = self._insert(data, root.left)
    else:
      if root.right is None:
        root.right = Node(data)
      else:
        root.right = self._insert(data, root.right)

    root.height = 1 + max(self._get_height(root.left),
                          self._get_height(root.right))
    return self._balance(data, root)

  def _get_height(self, root):
    if root is None:
      return 0
    return root.height

  def _balance_factor(self, root):
    if root is None:
      return 0
    return self._get_height(root.left) - self._get_height(root.right)

  def _balance(self, data, root):
    balance_factor = self._balance_factor(root)

    if balance_factor > 1:
      if data < root.left.data:
        return self._rotate_right(root)
      else:
        root.left = self._rotate_left(root.left)
        return self._rotate_right(root)
    elif balance_factor < -1:
      if data > root.right.data:
        return self._rotate_left(root)
      else:
        root.right = self._rotate_right(root.right)
        return self._rotate_left(root)
    return root

  def _rotate_left(self, root):
    new_node = root.right
    root.right = new_node.left
    new_node.left = root

    root.height = 1 + max(self._get_height(root.left),
      self._get_height(root.right))

    new_node.height = 1 + max(self._get_height(new_node.left),
      self._get_height(new_node.right))

    return new_node
  def _rotate_right(self, root):
    new_node = root.left
    root.left = new_node.right
    new_node.right = root

    root.height = 1 + max(self._get_height(root.left),
      self._get_height(root.right))

    new_node.height = 1 + max(self._get_height(new_node.left),
      self._get_height(new_node.right))
    return new_node
  def printTree(self, root, Level=0):
    if root is not None:
        self.printTree(root.right , Level + 1)
        print("    "*Level , root.data)
        self.printTree(root.left , Level + 1)

T = AVLTree()
inp = input("Enter Input : ").split()
for i in inp :
  T.insert(int(i))

T.printTree(T.root)