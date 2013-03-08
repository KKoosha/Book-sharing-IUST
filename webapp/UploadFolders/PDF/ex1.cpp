#include<iostream>
#include<cmath>

#include<string>
using namespace std;
int main(){
int rad;
cout<<"enter radius:";
cin>>rad;
int xy[2];

for (int i=0;i<2;i++)
    if(i==0){
        cout<<"x:";
        cin>>xy[i];
    }
    else{
        cout<<"y:";
        cin>>xy[i];}
    if(sqrt(pow(xy[0],2)+pow(xy[1],2))==rad)
        cout<<"on the circle";
    else if(sqrt(pow(xy[0],2)+pow(xy[1],2))<rad)
    cout<<"in circle";
    else
        cout<<"out of circle";

    return 0;
}
