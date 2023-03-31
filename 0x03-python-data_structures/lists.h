#ifndef LISTS_H
#define LISTS_H


#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct dobint_s - doubly linked list
 * @n: integer
 * @next: points to the next node
 * @prev: points to the previous bode
 *
 * Description: doubly linked list node structure
 * for project
 */

typedef struct dobint_s
{
	int n;
	struct dobint_s *next;
	struct dobint_s *prev;
} doubleint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
void create_doubly_list(listint_t **head, doubleint_t **h);
#endif /* LISTS_H */
