#include "lists.h"
#include <stdio.h>

/**
 * insert_node - insert a node to a sorted linked list
 * @head: pointer to listint_t struct
 * @number: data to add to node
 * Return: return the new node address
 */


listint_t *insert_node(listint_t **head, int number)
{
	void sort_list(listint_t **head);
	listint_t *new;

	if (!head)
		return (NULL);
	if (!*head)
		return (add_nodeint_end(head, number));

	new = add_nodeint_end(head, number);
	sort_list(head);
	return (new);
}

/**
 * sort_list -> sort the data in a linked list
 * @head: pointer to listInt_t
 * Return: void
 */

void sort_list(listint_t **head)
{
	listint_t *current, *inner;
	int temp, swapped;

	current = *head;
	while (current)
	{
		swapped = 0;
		inner = current;
		while (inner->next)
		{
			if (inner->n > inner->next->n)
			{
				temp = inner->n;
				inner->n = inner->next->n;
				inner->next->n = temp;
				swapped = 1;
			}
			inner = inner->next;
		}
		if (!swapped)
			break;
	}
}
