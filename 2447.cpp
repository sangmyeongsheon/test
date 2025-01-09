#include <iostream>
using namespace std;

char** star(int n){
    char** starlist=new char*[n];
    for (int j=0;j<n;j++){
        char* starlist_in_list= new char[n+1];
        if ((j>=n/3)&&(j<n*2/3)){
            for (int i=0;i<n;i++){
                if ((i>=n/3)&&(i<n*2/3)){
                    starlist_in_list[i]=' ';
                }
                else{
                    starlist_in_list[i]='*';
                }
            
            } 
        }
        else{
            for (int i=0;i<n;i++){
            
                starlist_in_list[i]='*';
            }
        }
    starlist_in_list[n]='\0';
    starlist[j]=starlist_in_list;
    }
    return starlist;
}
int main(){
    int number;
    cin>>number;
    char** star_result=star(number);
    for (int i=0;i<number;i++){
        cout<<star_result[i]<<endl;
    }
}