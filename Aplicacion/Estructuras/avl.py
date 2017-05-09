# -*- coding: utf-8 -*-
#  Implementation of AVL tree
#
#   Author: Joseph
import subprocess
class avlnode(object):
    """
    A node in an avl tree.
    """

    def __init__(self, key, nombre, descripcion):
        "Construct"

        # The node's key
        self.key = key
        self.nombre=nombre
        self.descripcion=descripcion
        # The node's left child
        self.left = None
        # The node's right child
        self.right = None

    def __str__(self):
        "String representation."
        return str(self.key)

    def __repr__(self):
        "String representation."
        return str(self.key)


class avltree(object):
    """
    An avl tree.
    """

    def __init__(self):
        "Construct."

        # Root node of the tree.
        self.node = None
        # Height of the tree.
        self.height = -1
        # Balance factor of the tree.
        self.balance = 0

    def insert(self, key, nombre, descripcion):
        """
        Insert new key into node
        """
        # Create new node
        n = avlnode(key, nombre, descripcion)

        # Initial tree
        if not self.node:
            self.node = n
            self.node.left = avltree()
            self.node.right = avltree()
        # Insert key to the left subtree
        elif key < self.node.key:
            self.node.left.insert(key, nombre, descripcion)
        # Insert key to the right subtree
        elif key > self.node.key:
            self.node.right.insert(key, nombre, descripcion)

        # Rebalance tree if needed
        self.rebalance()

    def rebalance(self):
        """
        Rebalance tree. After inserting or deleting a node,
        it is necessary to check each of the node's ancestors for consistency
        with the rules of AVL
        """

        # Check if we need to rebalance the tree
        #   update height
        #   balance tree
        self.update_heights(recursive=False)
        self.update_balances(False)

        # For each node checked,
        # if the balance factor remains −1, 0, or +1 then no
        # rotations are necessary.
        while self.balance < -1 or self.balance > 1:
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Case -> rotate y,z to the left
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                    
                # A   B
                self.rotate_right()
                self.update_heights()
                self.update_balances()
                
            # Right subtree is larger than left subtree
            if self.balance < -1:

                # Right Left Case -> rotate x,z to the right
                if self.node.right.balance > 0:
                    
                    self.node.right.rotate_right()  #we're in case III
                    self.update_heights()
                    self.update_balances()

                #         C   D
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height

        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor

        The balance factor is calculated as follows:
            balance = height(left subtree) - height(right subtree).
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        """
        Right rotation
            set self as the right subtree of left subree
        """
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        """
        Left rotation
            set self as the left subtree of right subree
        """
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, key):
        if self.node != None:
            if self.node.key == key:
                # Key found in leaf node, just erase it
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                # Node has only one subtree (right), replace root with that one
                elif not self.node.left.node:
                    self.node = self.node.right.node
                # Node has only one subtree (left), replace root with that one
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    # Find  successor as smallest node in right subtree or
                    #       predecessor as largest node in left subtree
                    successor = self.node.right.node
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.key = successor.key

                        # Delete successor from the replaced node right subree
                        self.node.right.delete(successor.key)

            elif key < self.node.key:
                self.node.left.delete(key)

            elif key > self.node.key:
                self.node.right.delete(key)

            # Rebalance tree
            self.rebalance()


    def inorder_traverse(self):
        """
        Inorder traversal of the tree
            Left subree + root + Right subtree
        """
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse())

        return result

    def display(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.display(node.right.node, level + 1)
            print ('\t' * level), ('    /')

        print ('\t' * level), node

        if node.left.node:
            print ('\t' * level), ('    \\')
            self.display(node.left.node, level + 1)
    def graficar(self):
        cadena = "digraph arbol {\n"
    	if(self.node != None):
    		cadena = self.__listar(self.node, cadena)
    		cadena += "\n"
    		cadena = self.__enlazar(self.node, cadena)
		cadena += "}"
		Archivo = open('/home/joseph/Documentos/Avl.dot', 'w') 
		Archivo.write(cadena) 
		Archivo.close() 
		subprocess.call(['dot', '/home/joseph/Documentos/Avl.dot', '-o', '/home/joseph/Documentos/Avl.png', '-Tpng', '-Gcharset=utf8']) 

    def __listar(self, raiz, cadena):
    	if(raiz != None):
    		cadena += "n" + str(raiz.key) + " [label = \"" + str(raiz.key) + "\"];\n"
    		if(raiz.left != None and raiz.right != None):
    			cadena = self.__listar(raiz.left.node, cadena)
    			cadena = self.__listar(raiz.right.node, cadena)
    		elif(raiz.node.left != None):
    			cadena = self.__listar(raiz.left.node, cadena)
    		elif(raiz.node.right != None):
    			cadena = self.__listar(raiz.right.node, cadena)
    	return cadena;

    def __enlazar(self, raiz, cadena):
    	if(raiz != None):
    		if(raiz.right.node != None):
    			cadena += "n" + str(raiz.key) + " -> n" + str(raiz.right.node.key) + ";\n"
    			cadena = self.__enlazar(raiz.right.node, cadena)
    		if(raiz.left.node != None):
    			cadena += "n" + str(raiz.key) + " -> n" + str(raiz.left.node.key) + ";\n"
    			cadena = self.__enlazar(raiz.left.node, cadena)
    	return cadena
# Demo
#if __name__ == "__main__":
  #  tree = avltree()
   # data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

  #  from random import randrange
  #  for key in data:
   #     tree.insert(key)

 #   for key in [4, 3]:
  #      tree.delete(key)

   # print tree.inorder_traverse()
   # tree.display()
avl=avltree()
