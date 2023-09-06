#include "lists.h"
/**
 * insert_node - inserts a node in a sorted list
 * @head: a pointer to a pointer
 * @number: the number to insert
 * Return: a pointer to the inerted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current, *prev;


	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}
	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	prev->next = newnode;
	newnode->next = current;

	return (newnode);
}
