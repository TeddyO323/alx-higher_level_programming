#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - Insert a node
 *@head: Header of the list
 *@number: Number
 *Return: the address of the new node  null on failure
 */
listint_t *insert_node(listint_t **head, int number)

{
	listint_t *node, *aux, *tmp;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	aux = *head;
	tmp = aux;
	aux = tmp->next;
	if (number <= tmp->n)
	{
		node->next = tmp;
		*head = node;
		return (node);
	}
	while (aux != NULL)
	{
		if (number <= aux->n)
		{
			node->next = aux;
			tmp->next = node;
			return (node);
		}
		tmp = aux;
		aux = aux->next;
	}
	tmp->next = node;
	return (node);
}