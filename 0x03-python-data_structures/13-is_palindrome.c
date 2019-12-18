#include "lists.h"

/**
 * is_palindrome - tests if linked lists is palindrome
 * @head: address of pointer to list
 * Return: 1 is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *a = *head, *b = *head, *node, *prev;
	int fail = 0;

	while (b != NULL && b->next != NULL)
	{
		b = b->next->next;
		a = a->next;
	}
	node = a;
	prev = NULL;
	while (node)
	{
		b = node->next;
		node->next = prev;
		prev = node;
		node = b;
	}
	b = *head;
	node = prev;
	while (prev)
	{
		if (b->n != prev->n)
		{
			fail = 1;
			break;
		}
		b = b->next;
		prev = prev->next;
	}
	prev = NULL;
	while (node)
	{
		b = node->next;
		node->next = prev;
		prev = node;
		node = b;
	}
	return (!fail);
}
