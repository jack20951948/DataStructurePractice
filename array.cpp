#include <iostream>
#include <stdlib.h>

using namespace std;

template<typename T>
class Vector {
T* val;
int endIndex;
public:
    int size(){
        return *(&val + 1) - val;
    }
    int capacity(){
        return size() - endIndex;
    }
    bool is_empty(){
        return endIndex == 0;
    }
    T indexof(int index){
        if (endIndex < index){
            cout << "input error" << endl;
        } else {
            return *(val + (index - 1));
        }
    }
    void resize(int new_capacity){
        T* t_Vec = new T[new_capacity];
        for(int i=0; i<=size()-capacity(); i++){
            *(t_Vec + i) = *(val + i);
        }
        delete [] val;
        val = t_Vec;
        t_Vec = NULL;
    }
    void push(int item){
        if(capacity() == 0){
            resize(size()*2);
        }
        endIndex++;
        *(val + (endIndex - 1)) = item;
    }

    void insert(int index, int item){
        if(capacity() == 0){
            resize(size()*2);
        }
        endIndex++;
        for(int i=size()-capacity()-1; i>=index; i--){
            *(t_Vec + i) = *(val + i);
        }
    }
};