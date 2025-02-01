class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end_of_word

# Load dictionary words into Trie
trie = Trie()
word_list = ["apple", "banana", "grape", "orange", "pear","noor","ammar","ali","manahil"]
for word in word_list:
    trie.insert(word)

# Spell checking
def check_spelling(word):
    return trie.search(word)
print("WELCOME TO MY SPELL CHECKER MINI PROJECT.")
print("HERE WE CHECK SPELLING OF SOME WORDS  WITH THE HELP OF  SOME INPUTED VALUE")
print("The inputed value is apple. Is the spelling are correct? :",check_spelling("apple"))  # True
print("The inputed value is appl. Is the spelling are correct? :",check_spelling("appl"))   # False
print("The inputed value is grepe. Is the spelling are correct? :",check_spelling("grepe") ) #False
print("The inputed value is grape. Is the spelling are correct? :",check_spelling("grape") ) #True
print("The inputed value is nor. Is the spelling are correct? :",check_spelling("nor")) #False
print("The inputed value is ammar. Is the spelling are correct? :",check_spelling("ammar")) #True