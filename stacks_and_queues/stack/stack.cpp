#include <iostream>

using namespace std; 


class Node{
    public:
        int data; 
        Node* next; 
        
        Node(int data): data(data), next(nullptr) {}
};


class Stack{
    private:
        Node* top; 
        int _size = 0;

    public:
        void push(int item){
            Node* node = new Node(item);
            node->next = top;
            top = node; 
            _size ++; 
        }

        int pop(){
            Node* node = top; 
            top = top->next;

            if(_size > 0){
                _size --; 
                return node->data; 
            }
            else{
                cerr << "stack has 0 items" << endl;
                return 0; 
            }
        }

        int peek(){
            if(_size > 0){
                return top->data; 
            }
            else{
                cerr << "stack has 0 items" << endl; 
                return 0; 
            }
        }

        int size(){
            return _size; 
        } 

        string repr() const{
            string txt; 
            int counter = 0; 
            Node* pointer = top; 

            while(_size > counter){
                txt += to_string(pointer->data) + " "; 
                pointer = pointer->next; 
                counter++; 
            }
            return txt;
        }

        bool operator==(const Stack& other_stack) const{
            if(_size != other_stack._size){
                return false; 
            }
            
            Node* pointer_a = top;
            Node* pointer_b = other_stack.top; 
            int counter = 0; 

            while(counter < _size && pointer_a->data == pointer_b->data){
                counter++; 
                pointer_a = pointer_a->next; 
                pointer_b = pointer_b->next; 
            }

            return (counter == _size);
        }
};
