#include <iostream>

using namespace std;


class BinaryTree{

    class Node{
    public:
        int value; 
        Node* left;
        Node* right; 
        
        Node(int value): value(value), left(nullptr), right(nullptr) {}
    };

    private:
        Node* root; 
        unsigned int _size = 0;
    
    public:
        int size(){
            return _size;
        }

        void append(int item){
            if(!(root)){
                root = new Node(item);
                _size ++;
                return;
            }
            
            Node* pointer = root;
            while(pointer){
                if((pointer->value > item) && pointer->left){
                    pointer = pointer->left;
                }
                else if((pointer->value < item) && pointer->right){
                    pointer = pointer->right;
                }
                else{
                    break;
                }
            }
            if(pointer->value < item){
                pointer->right = new Node(item);
            }
            else{
                pointer->left = new Node(item);
            }
            _size++;
        }

        void remove(int item){
            Node* pointer = root; 
            Node* parent;

            if(!(pointer->value)){
                throw runtime_error("Empty Tree");
            }
            else if(pointer->value == item){
                ;
            }
            else{
                while(pointer){
                    if(pointer->value < item){
                        parent = pointer;
                        pointer = pointer->right;
                    }
                    else if(pointer->value > item){
                        parent = pointer;
                        pointer = pointer->left;
                    }
                    else{
                        break;
                    }
                }
            }

            if(pointer->right){
                Node* replace = pointer->right;
                while(replace->left){
                    parent = replace;
                    replace = replace->left;
                }
                pointer->value = replace->value;
                parent->left = nullptr;
            }
            else if(pointer->left){
                Node* replace = pointer->left;
                while(replace->right){
                    parent = replace;
                    replace = replace->right;
                }
                pointer->value = replace->value;
                parent->right = nullptr;
            }
            else{
                if(parent->left->value == item){
                    parent->left = nullptr;
                }
                else{
                    parent->right = nullptr;
                }
            }
            _size--;
        }

};
