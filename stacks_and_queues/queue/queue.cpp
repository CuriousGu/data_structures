#include <iostream>
#include <sstream>

using namespace std;


class Queue{

    private:
        class Node{
            public:
                int value; 
                Node* next; 
                
                Node(int value): value(value), next(nullptr) {}
        };

        Node* root = nullptr;
        unsigned int _size = 0;

    public:
        void append(int item){
            if(!(root)){
                root = new Node(item);
            }
            else{
                Node* pointer = root;
                while(pointer->next){
                    pointer = pointer->next;
                }
                pointer->next = new Node(item);
            }
            _size++;
        }

        int remove(){
            if(!(root)){
                throw runtime_error("Empty Queue");
            }
            int temp = root->value;
            root = root->next;
            _size--;
            return temp;
        }
    
        unsigned int size() const{
            return _size;
        }

        string toString() const {
            Node* pointer = root;
            stringstream ss;
            while (pointer) {
                ss << pointer->value;
                if (pointer->next) {
                    ss << " -> ";
                }
                pointer = pointer->next;
            }
            return ss.str();
    }
};
