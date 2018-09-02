// For the sake of simplicity of the program all the array indices starts from 1. (Algorithm B)
#include <iostream>
using namespace std;

class tree{
	public:
		int j,k,y;
		// To print the left and the right array of the tree.
		void print_tree(int left[],int right[],int n){
			for(int i=1;i<=n;i++)
				cout<<left[i]<<" ";
			cout<<endl;
			
			for(int j=1;j<=n;j++)
				cout<<right[j]<<" ";
			cout<<endl;
			cout<<endl;
		}
		// To get all the binary tree representaion.
		void create_tree(int l[],int r[],int n){
			// Step 1 - Algorithm.
			for(int m=1;m<n;m++){
				l[m] = m+1;
				r[m] = 0;
			}
			l[n] = 0;
			r[n] = 0;
			l[n+1] = 1;
			
			while(1){
				// To visit the tree.
				print_tree(l,r,n);
				// Step B3 implementation.
				j = 1;
				while(l[j] == 0){
					r[j] = 0;
					l[j] = j+1;
					j = j+1;	
				}
				// To break out of the main loop.
				if(j>n)
					break;
				// Step B3 -- Implementation
				y = l[j];
				k = 0;
				while(r[y]>0){
					k = y;
					y = r[y];
				}
				// Step B4 implemetation.
				if(k>0)
					r[k] = 0;
				else
					l[j] = 0;
				r[y] = r[j];
				r[j] = y;
			}
			
		}
};

int main(){
	int n;
	int* left;
	int* right;
	// To get the number of internal nodes from the user 
	cout<<"Enter the number of internal nodes"<<endl;
	cin>>n;
	// To dynamically allocate memory for the left and right pointers.
	left = new int[n+2];
	right = new int[n+2];
	// Assigning the first element of the array to 0.
	left[0] = 0;
	right[0] = 0;
	
	tree t;
	t.create_tree(left,right,n);
	
	return 0;
}
