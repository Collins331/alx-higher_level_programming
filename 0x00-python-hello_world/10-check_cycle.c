#include "lists.h"
/**
 * check_cycle - checks for cycles in a single-linked list
 * @list: the single-linked list
 * Return: 1(if present) else (0)
 */
int check_cycle(listint_t *list)
{
	listint_t *new;

	new = list;

	while (list != NULL)
	{
		if (list->next == NULL)
		{
			return (0);
		}
		list = list->next;

		if (list == new)
		{
			return (1);
		}
	}
	return (0);
}
