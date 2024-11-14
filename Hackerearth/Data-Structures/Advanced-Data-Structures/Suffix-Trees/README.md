# TUTORIAL Suffix Trees

Suffix tree is a compressed trie of all the suffixes of a given string. Suffix trees help in solving a lot of string related problems like pattern matching, finding distinct substrings in a given string, finding longest palindrome etc. In this tutorial following points will be covered:

- Compressed Trie
- Suffix Tree Construction (Brute Force)
- Brief description of Ukkonen's Algorithm

Before going to suffix tree, let's first try to understand what a compressed trie is.

As it might be clear from the images show above, in a compressed trie, edges that direct to a node having single child are combined together to form a single edge and their edge labels are concatenated. So this means that each internal node in a compressed trie has atleast two children. Also it has atmost N leaves, where N is the number of strings inserted in the compressed trie. Now both the facts: Each internal node having atleast two children, and that there are N leaves, implies that there are atmost 2N-1 nodes in the trie. So the space complexity of a compressed trie is O(N) as compared to the O(N²) of a normal trie.

So that is one reason why to use compressed tries over normal tries.

Before going to construction of suffix trees, there is one more thing that should be understood, Implicit Suffix Tree. In Implicit suffix trees, there are atmost N leaves, while in normal one there should be exactly N leaves. The reason for atmost N leaves is one suffix being prefix of another suffix.

Now let's go to the construction of the suffix trees.

Suffix tree as mentioned previously is a compressed trie of all the suffixes of a given string, so the brute force approach will be to consider all the suffixes of the given string as separate strings and insert them in the trie one by one. But time complexity of the brute force approach is O(N²), and that is of no use for large values of N.

The pseudo code for the brute force approach is given below:

```bash
function insert(T, string, start_index, length){
    i = start_index
    while(i < length)
        if T.arr[string[i]]) is NULL
            T.arr[string[i]] = new node()
            T = T.arr[string[i]]
            while(i < length)
                T.label = T.label+string[i]
                i = i+1
            endwhile
            return
        endif

        j=0, x=i
        temp = T.arr[string[i]]
        while j < temp.label.length and i < length && temp.label[j] = string[i]
            i = i+1
            j = j+1
        endwhile

        if i = length
            return
        endif

        if j = temp.label.length
            cnt = 0
            for k = 'a' to 'z'
                if temp.arr[k] = NULL
                    cnt = cnt+1
                endif
            endfor
            if cnt = 27
                while i < length
                    temp.label = temp.label + string[i]
                    i = i+1
                endwhile
            else
                T = temp
            endifelse
        else
            newInternalNode = new node()
            k=0
            while k < j
                newInternalNode.label = newInternalNode.label + temp.label[k]
                k = k+1
            endwhile
            newInternalNode.arr[string[j]] = new node()
            while k < temp.label.length
                newInternalNode.arr[string[j]].label+=temp.label[k]
                k = k+1
            endwhile
            for k = 'a' to 'z'
                newInternalNode.arr[string[j]].arr[k] = temp.arr[k]
            endfor
            T.arr[string[x]] = newInternalNode
            T = T.arr[string[x]]
        endifelse
    endwhile
}

function makeSuffixTree(string, length){
    Trie T
        string = concatenate(string, "{")
    for i = 0 to length
        insertInTrie(T, string, i, length)
}
```
