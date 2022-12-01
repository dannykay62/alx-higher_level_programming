#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contain a cycle
 * @list: singly linked list
 * Return: 0 if no cycle or -1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *here;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	here = list->next->next;

	while (turtle && here && here->next)
	{
		if (turtle == here)
			return (1);

		turtle = turtle->next;
		here = here->next->next;
	}

	return (0);
}
