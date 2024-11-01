# Pseduo
function ReverseList(head)
    prev = NULL
    curr = head

    While curr is not NULL

        // Save the next node
        next = curr.next

        // Reverse the link
        curr.next = prev

        // Move prev and curr forward
        prev = curr
        curr = next
    return prev
