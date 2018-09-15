#include <iostream>
#include <string>
#include <vector>

using namespace std;

int start = 0;

class Node{
	public:
	char data;
	Node* left;
	Node* right;
};


Node* create_node(char data){
	Node* node = new Node;	
	node->data = data;
	node->left = NULL;
	node->right = NULL;
	return node;
}
	

Node* construct_tree(string s){
	int n = s.length();	
	vector<Node*> roots;
	for(int i=0;i<n;i++){
		Node* temp = create_node(s[i]);
		if(s[i]=='H'||s[i]=='h'||s[i]=='V'||s[i]=='v'){
			temp->right = roots.back();
			roots.pop_back();
			temp->left = roots.back();
			roots.pop_back();
			roots.push_back(temp);
		}
		else
			roots.push_back(temp);
	}
	return roots.back();
}

void create_array(Node* root, char* l_i_array,char* r_i_array,char* larray, char* rarray){
	if(root == NULL)
		return;
		
	if(root->data == 'V' ||root->data == 'v'|| root->data == 'H'|| root->data == 'h'){
		//cout<<root->data<<" "<<start<<endl;
		if(root->left->data == 'V' ||root->left->data == 'v'|| root->left->data == 'H'|| root->left->data == 'h')
			l_i_array[start] = root->left->data;
		else
			larray[start] = root->left->data;
			
		if(root->right->data == 'V' ||root->right->data == 'v'|| root->right->data == 'H'|| root->right->data == 'h')
			r_i_array[start] = root->right->data;
		else
			rarray[start] = root->right->data;
		
		start++;
		root->data = 'S';
	}
	
	create_array(root->left,l_i_array,r_i_array,larray,rarray);
	create_array(root->right,l_i_array,r_i_array,larray,rarray);
}

void final_print(char larray[],char rarray[],char l_i_array[], char r_i_array[],int n){
	for(int i =0; i<n;i++)
		cout<<"("<<l_i_array[i]<<","<<larray[i]<<")"<<" ";
	cout<<endl;
	for(int j =0; j<n;j++)
		cout<<"("<<r_i_array[j]<<","<<rarray[j]<<")"<<" ";
	cout<<endl;
}

int main(){
	string s;
	cout<<"Enter the post order expression string"<<endl;
	cin>>s;
	vector<Node*> roots;
	Node* temp = construct_tree(s);
	
	int n;
	n = (s.length()-1)/2;
	char* l_i_array = new char[n];
	char* r_i_array = new char[n];
	char* larray = new char[n];
	char* rarray = new char[n];
	
	for(int i=0;i<n;i++){
		larray[i] = '0';
		rarray[i] = '0';
		l_i_array[i] = '0';
		r_i_array[i] = '0';
	}
	
	cout<<"The root is "<<temp->data<<endl;
	create_array(temp,l_i_array,r_i_array,larray,rarray);
	final_print(larray,rarray,l_i_array,r_i_array,n);
	
	return 0;
}
