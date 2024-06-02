#include <vector>
#include <iostream>
#include <cmath>

using namespace std; 


class MaxHeap{
    private:
        vector<int> heap; 

        void reorder_insertion(unsigned int item_index){
            while(item_index > 0){
                unsigned int parent_index = (item_index - 1) * .5; 

                if(heap[parent_index] < heap[item_index]){
                    int temp = heap[parent_index]; 
                    heap[parent_index] = heap[item_index]; 
                    heap[item_index] = temp; 

                    item_index = parent_index;
                }
                else{
                    break;
                }
            }
        }

        void reorder_removal(){
            unsigned int index = 0; 
            heap[index] = heap[heap.size() - 1]; 
            heap.pop_back(); 
            const int SIZE = heap.size(); 

            while(2 * index + 1 < SIZE){
                unsigned int l_child = 2 * index + 1; 
                unsigned int r_child = 2 * index + 2;
                unsigned largest = index; 

                if(l_child < SIZE && heap[l_child] > heap[largest]){
                    largest = l_child; 
                }
                if(r_child < SIZE && heap[r_child] > heap[largest]){
                    largest = r_child;
                }
                if(largest != index){
                    int temp = heap[index];
                    heap[index] = heap[largest]; 
                    heap[largest] = temp;

                    index = largest; 
                }
                else{
                    break; 
                }
            }
        }

    public:
        int size(){
            return heap.size();
        }

        void insert(int item){
            heap.push_back(item); 
            reorder_insertion(heap.size() - 1); 
        }

        int remove_max(){
            if(heap.size() > 0){
                int item = heap[0];
                reorder_removal(); 
                return item; 
            }
            else{
                throw out_of_range("EMPTY HEAP");
                return 0; 
            }
        }

        string print_tree(){
            if(heap.size() == 0){
                return "EMPTY HEAP";
            }
            
            int leaves = 1; 
            string txt = to_string(heap[0]) + "\n"; 
            unsigned int SIZE = heap.size(); 

            while(pow(2, leaves+1) - 1 < SIZE){
                unsigned int b = pow(2, leaves) - 1; 
                unsigned int e = pow(2, leaves + 1) - 1; 

                for(int i = b; i < e; i++){
                    txt += to_string(heap[i]) + " - "; 
                }

                txt += "\n"; 
                leaves++;
            }
            for(int i = pow(2, leaves) - 1; i < SIZE; i++){
                txt += to_string(heap[i]) + " - "; 
            }

            return txt;
        }
             

};
