#include <bits/stdc++.h>
using namespace std;

int main(){
	int digit[]={0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8};
	//twenty thirty forty fifty sixty seventy eighty ninety 
	int ten[]={0,0,6,6,5,5,5,7,6,6};
	int Ans=0;
	for(int i=1;i<1000;i++){
			int ii=i;
			int f=ii/100;
			Ans+=(digit[f]);
			if(f>0) Ans+=7;
			int s=ii%100;
			if(s>0 && f>0) Ans+=3;
			if(s>=20){
				int t=s/10;
				Ans+=ten[t];
				Ans+=digit[s%10];
			}
			else Ans+=digit[s];
	}
	Ans+=(3+8);
	cout<<Ans<<endl;
			
	return 0;
}
