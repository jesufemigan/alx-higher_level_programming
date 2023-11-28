#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 *
 * @head: head of list
 * @number: number to insert
 *
 * Return: address of new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *temp;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	current = *head;
	if (current->n > number)
	{
		new_node->next = *head;
	}
	while (current)
	{
		if (current->n < number)
		{
			temp = current;
			current = current->next;
		}
		else
		{
			new_node->next = current;
			temp->next = new_node;
			break;
		}
	}
	return (new_node);
}
