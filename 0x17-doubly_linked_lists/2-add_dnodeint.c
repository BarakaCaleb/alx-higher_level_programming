#include<stdio.h>
#include<stdlib.h>


/**
 *
 *
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n);
{
	dlistint_t **head temp = malloc(sizeof(dlistint_t));
	temp->prev = NULL;
	temp->data = data;
	temp->next = NULL;
	head = temp;
	return head;
}
