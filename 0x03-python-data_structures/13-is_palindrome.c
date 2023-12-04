#include "lists.h"

/**
 * reverse_list - reverses a linked list
 *
 * @llist: the lined list
 *
 * Return: the reversed list
 */

listint_t *reverse_list(listint_t *llist)
{
	listint_t *prev = NULL, *current = llist, *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly lined list is a palindrome
 *
 * @head: the linked link
 *
 * Return: 0 if it is not a palindrome and 1 if otherwise
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head;
	listint_t *second_part, *first_part;

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	second_part = reverse_list(slow->next);
	first_part = *head;

	while (second_part)
	{
		if (first_part->n != second_part->n)
			return (0);
		first_part = first_part->next;
		second_part = second_part->next;
	}
	return (1);
}
