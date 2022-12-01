#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: pointer to the next node
 * Description: singly linked list structure for the project
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_modeint(listint_t **head, const int n);
void free_listint_t(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
