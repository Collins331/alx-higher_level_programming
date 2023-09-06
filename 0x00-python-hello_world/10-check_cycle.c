#include "lists.h"
/**
 * check_cycle - checks for cycles in a single-linked list
 * @list: the single-linked list
 * Return: 1(if present) else (0)
 */
int check_cycle(listint_t *list)
{
	listint_t *old = list;
	listint_t *new = list;

	while (new->next != NULL && new->next->next != NULL)
	{
		old = old->next;
		new = new->next->next;

		if (old == new)
		{
			return (1);
		}
	}
	return (0);
}
