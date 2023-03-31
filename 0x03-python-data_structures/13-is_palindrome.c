#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to a listint_t
 * Return: return 0 if not a palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	doubleint_t *top, *bottom, *double_ = NULL;

	if (!*head)
		return (1);

	create_doubly_list(head, &double_);

	top = bottom = double_;
	while (bottom->next)
		bottom = bottom->next;
	while (top && bottom)
	{
		if (top->n == bottom->n)
		{
			bottom = bottom->prev;
			top = top->next;
		}
		else
			return (0);
	}
	return (1);
}

/**
 * create_doubly_list - creates a doubly linked list from a singly linked list
 * @head: pointer to a single linked list
 * @temp_h: pointer to a doubly linked list
 * Return: void
 */

void create_doubly_list(listint_t **head, doubleint_t **temp_h)
{
	listint_t *temp;
	doubleint_t *new, *h;

	temp = *head;
	while (temp)
	{
		h = *temp_h;
		new = malloc(sizeof(doubleint_t));
		if (new == NULL)
			return;
		new->next = NULL;
		new->n = temp->n;
		if (!h)
		{
			new->prev = NULL;
			*temp_h = new;
			temp = temp->next;
			continue;
		}
		while (h->next)
			h = h->next;

		h->next = new;
		new->prev = h;

		temp = temp->next;
	}

}
