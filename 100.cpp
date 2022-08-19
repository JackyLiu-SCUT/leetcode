/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool res = true;
        traverse(p, q, res);
        return res;
    }

    void traverse(TreeNode* p, TreeNode* q, bool res){
        if(!p && !q){ //
            return;
        }
        if(!p && q || p && !q){
            res = false;
            return;
        }
        if(p->val != q->val){
            res = false;
            return;
        }
        traverse(p->left, q->left, res);
        traverse(p->right, q->right, res);
        return;
    }
};