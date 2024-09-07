class Solution {
public:
   
    bool isSubPath(ListNode* head, TreeNode* root) {

        if (!root) {
            return false;
        }

        return depthFirstSearch(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }


    bool depthFirstSearch(ListNode* head, TreeNode* node) {

        if (!head) {
            return true;
        }
        if (!node || head->val != node->val) {
            return false;
        }
        return depthFirstSearch(head->next, node->left) || depthFirstSearch(head->next, node->right);
    }
};