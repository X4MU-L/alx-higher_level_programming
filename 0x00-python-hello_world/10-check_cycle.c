#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (!list || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast->next != NULL && fast->next->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
