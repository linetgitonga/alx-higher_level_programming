#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @no: integer
 * @next: points to the next node
 *Author:LinetGitonga
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int no;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int no);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int numb);

#endif
