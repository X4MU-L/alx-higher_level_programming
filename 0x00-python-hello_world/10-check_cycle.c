#include "lists.h"

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
