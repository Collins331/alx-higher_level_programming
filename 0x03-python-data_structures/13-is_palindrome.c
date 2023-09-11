#include "lists.h"

listint_t *reverse(listint_t **head);

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to the single-linked list
 * Return: 1 (present) or 0 (none)
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *mid, *rev;
	size_t len = 0, i;

	if ((*head) == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	temp = *head;
	while (temp)
	{
		len++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		temp = temp->next;

	if ((len % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	rev = reverse(&temp);
	mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse(&mid);

	return (1);
}
/**
 * reverse - reverses the linked list
 * @head: pointer to the head of the list
 * Return: a pointer to the reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *new, *temp;

	temp = NULL;
	new = NULL;

	while (*head != NULL)
	{
		new = (*head)->next;
		(*head)->next = temp;
		temp = (*head);
		*head = new;
	}
	(*head) = temp;
	return (*head);
}
