#include <iostream>
#include <stdlib.h>

class Node{
	public:
	int data;
	Node* left;
	Node* right;
};

class binary_tree{
	public:
	Node* create_node(int data){
		Node* node = (Node*) malloc(sizeof(Node));	
		node->data = data;
		node->left = NULL;
		node->right = NULL;
		return node;
	}
	
	void preorder(Node* root, int left[], int right[]){
		//std::cout<<"Entered loop"<<"\n";
		if(root == NULL || (left[root->data - 1] == 0 && right[root->data -1] == 0))
			return;
		
		if(left[root->data -1] !=0){
			//std::cout<<"Entered loop"<<"\n";
			root->left = create_node(left[root->data - 1]);
			//left[root->data - 1] = 0;
			//preorder(root->left,left,right);
		}
		if(right[root->data -1] !=0){
			//std::cout<<"Entered loop"<<"\n";
			root->right = create_node(right[root->data - 1]);
			//right[root->data - 1] = 0;
			//preorder(root->right,left,right);
		}
		
		//std::cout<<"left"<<"\n";
		preorder(root->left,left,right);
		//std::cout<<"right"<<"\n";
		preorder(root->right,left,right);
		
	}
	
	Node* create_binary_tree(int left[],int right[]){
		Node* root = create_node(1);
		Node* temp = root;
		preorder(temp,left,right);
		return root;
	}
	
	void print_preorder(Node* root){
		if(root == NULL)
			return;
		std::cout<<root->data;
		print_preorder(root->left);
		print_preorder(root->right);
	}
	
};

int main(){
	int left[3];
	left[0] = 2;
	left[1] = 3;
	left[2] = 0;
	//left[3] = 0;
	
	int right[3];
	right[0] = 0;
	right[1] = 0;
	right[2] = 0;
	//right[3] = 0;
	
	binary_tree bt;
	Node* root = bt.create_binary_tree(left,right);
	bt.print_preorder(root);
	return 0;
}
