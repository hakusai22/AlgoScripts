function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var mergeNodes = function (head) {
    let tail = head;
    for (let cur = head.next; cur.next; cur = cur.next) {
        if (cur.val) {
            tail.val += cur.val;
        } else {
            tail = tail.next;
            tail.val = 0;
        }
    }
    tail.next = null;
    return head;
};