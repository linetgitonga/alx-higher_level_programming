#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @numb: The number to insert.
 * Author - Linet Gitonga
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int numb)
{
        listint_t *node = *head, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = numb;

        if (node == NULL || node->n >= numb)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        while (node && node->next && node->next->n < numb)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}
