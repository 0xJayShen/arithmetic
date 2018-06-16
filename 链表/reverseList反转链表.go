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