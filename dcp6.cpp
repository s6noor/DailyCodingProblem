/* 
    NOT COMPLETE - pending get function
    An XOR linked list is a more memory efficient doubly linked list. 
   Instead of each node holding next and prev fields, it holds a field named both, 
   which is an XOR of the next node and the previous node. Implement an XOR linked list; 
   it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
   
   Good explanation of a XOR linked list: https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/
   
   */

#include <iostream>
#include <vector>

using namespace std;

    
    // create a new type of data called node. This holds one value and also has a pointer to the linking with the previous and next values
    struct Node{
        int value;
        Node* link;    
    };

// the node pointer has a funxtion called xor, that does the xor of the previous and next nodes and thus performs the linking for the list
    Node* XOR(Node *x, Node *y){
        return (Node *)((uintptr_t)(x) ^ (uintptr_t)(y));    
    };
    
    int Add(Node* &prevnode, int newdata){
    
    //make the data a new node and set the value
    Node *newnode = new Node();
    newnode->value = newdata;
    
    // now we need to set the link of this node to point to the previous node
    newnode->link = XOR(prevnode,NULL);
    
    //now we need to update the previous node's link to include this one
    if(prevnode){
    prevnode->link = XOR(newnode,XOR(prevnode->link,nullptr));
    }
    //now make sure your pointer points to the updated node.
    prevnode = newnode;
    
    };


int main(){

//use a vector

    //Bonus Goal at end: I want to try and see if i can build a double linked list by just passing a vector
    //int arr[5] = {2,76,5,4,3};
    
    // First lets try to build a XOR linked list by passing one number at a time
    // for this ill need a defined class or structure for this type of number (that has a tracking method for a previous and a next number
    // and an adding function
    Node *mynode = nullptr;
    Add(mynode,10);
    Add(mynode,2);
    cout << mynode->value;
    

    return 0;

}
