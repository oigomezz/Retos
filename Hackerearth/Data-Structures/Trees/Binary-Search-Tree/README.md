# TUTORIAL

For a binary tree to be a binary search tree, the data of all the nodes in the left sub-tree of the root node should be <= the data of the root. The data of all the nodes in the right subtree of the root node should be > the data of the root.

The tree is known as a Binary Search Tree or BST.

## Traversing the tree

There are mainly three types of tree traversals.

**Pre-order traversal :** In this traversal technique the traversal order is root-left-right.

```C
    void perorder(struct node*root)
    {
        if(root)
        {
            printf("%d ",root->data);    //Printf root->data
            preorder(root->left);    //Go to left subtree
            preorder(root->right);     //Go to right subtree
        }
    }
```

**Post-order traversal:** In this traversal technique the traversal order is left-right-root.

```C
    void postorder(struct node*root)
    {
        if(root)
        {
            postorder(root->left);    //Go to left sub tree
            postorder(root->right);     //Go to right sub tree
            printf("%d ",root->data);    //Printf root->data
        }
    }
```

**In-order traversal:** In in-order traversal, do the following:

- First process left subtree (before processing root node)
- Then, process current root node
- Process right subtree

```C
    void inorder(struct node*root)
    {
        if(root)
        {
            inorder(root->left);    //Go to left subtree
            printf("%d ",root->data);    //Printf root->data
            inorder(root->right);     //Go to right subtree
        }
    }
```

## Insertion in BST

**Algorithm:** Compare data of the root node and element to be inserted.

1. If the data of the root node is greater, and if a left subtree exists, then repeat step 1 with root = root of left subtree. Else, insert element as left child of current root.
2. If the data of the root node is greater, and if a right subtree exists, then repeat step 2 with root = root of right subtree. Else, insert element as right child of current root.

```C
    struct node* insert(struct node* root, int data)
    {
        if (root == NULL)    //If the tree is empty, return a new,single node
            return newNode(data);
        else
        {
            //Otherwise, recur down the tree
            if (data <= root->data)
                root->left  = insert(root->left, data);
            else
                root->right = insert(root->right, data);
            //return the (unchanged) root pointer
            return root;
        }
    }
```
