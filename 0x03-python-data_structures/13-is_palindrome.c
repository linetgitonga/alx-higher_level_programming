#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, n;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (n = 0; n < (size / 2) - 1; n++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
