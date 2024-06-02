#include <iostream>

using namespace std; 


class Node{
    public:
        int data; 
        Node* next; 
        
        Node(int data): data(data), next(nullptr) {}
};



class LinkedList{
    private:
        Node* head = nullptr; 
        int _size = 0; 

    public:
        void append(int item){
            _size++; 
            if(!(head)){
                head = new Node(item); 
            }
            else{
                Node* pointer = head; 
                while(pointer->next){
                    pointer = pointer->next; 
                }
                pointer->next = new Node(item);
            }
        }
        
        void remove(int index){
            if(index == 0){
                head = head->next;
                _size--;
            }
            else if(_size > index){
                Node* childNode = head; 
                Node* parentNode = nullptr;
                for(int i=0; i<index; i++){
                    parentNode = childNode;
                    childNode = childNode->next;
                }
                parentNode->next = childNode->next;
                _size--;
            }
            else{
                throw out_of_range("Index out of range");
            }
        }

        int index(int item){
            Node* pointer = head; 
            int curr_index = 0; 

            while(pointer){
                if(pointer->data == item){
                    return curr_index; 
                }
                else{
                    curr_index++; 
                    pointer = pointer->next; 
                }
            }
            throw runtime_error("Item not found"); 
        }

        int size(){
            return _size; 
        }

        int operator[](int index) {
            if(_size > index){
                Node* pointer = head;  
                for(int i=0; i<index; i++){
                    pointer = pointer->next; 
                }
                return pointer->data;
            }
            throw out_of_range("Index out of range"); 
        }

        void setItem(int index, int value){
            if(_size > index){
                Node* pointer = head;
                for(int i=0; i<index; i++){
                    pointer = pointer->next;
                }
                pointer->data = value;
            }
            throw out_of_range("Index out of range");
        }

        string toString(){
            Node* pointer = head; 
            string txt = ""; 
            while(pointer){
                txt = txt + to_string(pointer->data) + ", "; 
                pointer = pointer->next; 
            }
            txt.pop_back();
            txt.pop_back(); 
            return txt; 
        }
}; 
