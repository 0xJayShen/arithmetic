package main
//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func reverseList(head *ListNode) *ListNode{
	var newHead *ListNode

	//head 是下一个被逆转的节点
	for head != nil{
		// 让nextNode指向head.Next, 免得head.Next不见了.
		nextNode := head.Next
		// head称为已经逆转的节点的新head
		head.Next = newHead
		// 让newHead重新称为所有已被逆转节点的head
		newHead = head
		// 让head指向下一个被逆转的节点
		head = nextNode
	}
	return newHead
}
//https://www.cnblogs.com/TimLiuDream/p/9932494.html
pre是cur的最前面那位（pre = cur）
cur就是当前位的后面链表元素（cur = cur.Next）
cur.Next肯定是接pre（cur.Next = pre）
func reversrList(head *ListNode) *ListNode {
    cur := head
    var pre *ListNode = nil
    for cur != nil {
        pre, cur, cur.Next = cur, cur.Next, pre //这句话最重要
    }
    return pre
}