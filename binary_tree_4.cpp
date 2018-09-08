#include <iostream>
#include <vector>

using namespace std;

struct Node{
	int data;
	struct Node* left;
	struct Node* right;
};

int count = 1;
int counter = 0;

struct Node* create_node(int n){
	Node* node = new Node;
	node->data = n;
	node->left = NULL;
	node->right= NULL;
	return node;
}
	
void print_preorder(struct Node* root){
	if(root == NULL)
		return;
	cout<<root->data;
	print_preorder(root->left);
	print_preorder(root->right);
}

void preserve(struct Node* root, vector<int>& check){
	if(root == NULL)
		return;
	check.push_back(root->data);
	preserve(root->left,check);
	preserve(root->right,check);
}

int preserve_order(vector<int>& check){
	while(!check.empty()){
		if(check.back() != check.size()){
			check.clear();
			return 0;
		}
		check.pop_back();
	}
	return 1;
}


void print_trees(struct Node* root, int *larray, int *rarray){
	if(root == NULL)
		return;
	if(root->left != NULL)
		larray[root->data -1] = root->left->data;
	if(root->right != NULL)
		rarray[root->data -1] = root->right->data;
	print_trees(root->left,larray,rarray);
	print_trees(root->right,larray,rarray);
}

void final_print(int larray[],int rarray[],int n){
	for(int i =0; i<n;i++)
		cout<<larray[i]<<" ";
	cout<<endl;
	for(int j =0; j<n;j++)
		cout<<rarray[j]<<" ";
	cout<<endl;
}
Node* copy_tree(Node* root){
	if (root == NULL) 
	 	return root;

   Node *temp = new Node;
   temp->data = root-> data;  
   temp->left = copy_tree(root -> left);    
   temp->right = copy_tree(root -> right);  
   return temp;
}


void tree_preorder(Node* tree, vector<Node*> &trees,Node* root,int max){
	if(tree == NULL)
		return;
		
	if(tree->left == NULL && tree->right == NULL){
		vector<int> check;
		if(tree->data > max){
			Node* lptr = create_node(count);
			Node* rptr = create_node(count);
			tree->left = lptr;
			Node* temp = copy_tree(root);
			//cout<<endl;
			//print_preorder(temp);
			preserve(root,check);
			if(preserve_order(check)!=0)
				trees.insert(trees.begin(),temp);
			tree->left = NULL;
			tree->right = rptr;
			temp = copy_tree(root);
			//cout<<endl;
			//print_preorder(temp);
			preserve(root,check);
			if(preserve_order(check)!=0)
				trees.insert(trees.begin(),temp);
			tree->right = NULL;
			max = tree->data;
		}
	}
	
	else if(tree->right == NULL){
		vector<int> check;
		Node* rptr = create_node(count);
		tree->right = rptr;
		Node* temp = copy_tree(root);
		//cout<<endl;
		preserve(root,check);
		if(preserve_order(check)!=0)
			trees.insert(trees.begin(),temp);
		tree->right = NULL;
		max = tree->data;
	}	
	tree_preorder(tree->left,trees,root,max);
	tree_preorder(tree->right,trees,root,max);
	
}
void binary_tree(int n,vector<struct Node*> &trees){
	int max;
	if(count > n){
		//cout<<"second";
		//cout<<trees.size()<<endl;
		return;
	}
	else{
		if(trees.empty()){
			Node* node = create_node(count);
			trees.push_back(node);
			count++;
			//cout<<"first:";
			//cout<<trees.size()<<endl;
			//cout<<node->left;
			binary_tree(n,trees);
		}
			
		else{
			int tree_size = trees.size();
			for(int i=0;i<tree_size;i++){
				//cout<<"entered loop 1"<<endl;
				Node* popped_value = trees.back();
				trees.pop_back();
				//cout<<"data"<<popped_value->left<<endl;
				max = 0;
				//cout<<"size"<<trees.size()<<endl;
				tree_preorder(popped_value,trees,popped_value,max);	
				//cout<<"size 2"<<trees.size()<<endl;	
			}
			count++;
			binary_tree(n,trees);
		}
	}
}
		
	
int main(){
	int n;
	
	cout<<"Enter the number of internal nodes"<<endl;
	cin>>n;
	
	int* larray = new int[n];
	int* rarray = new int[n];
	
	vector<struct Node*> trees;
    binary_tree(n,trees);
	//cout <<"third"<< trees.size();
	for(int i=0;i<trees.size();i++){
		for(int k=0;k<n;k++){
			larray[k] = 0;
			rarray[k] = 0;
		}
		counter++;
	 	//print_preorder(trees[i]);
	 	//cout<<endl;
		print_trees(trees[i],larray,rarray);
		final_print(larray,rarray,n);
		cout<<endl;
	}
	cout<<counter;
	return 0;
}
