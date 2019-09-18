#include "lists.h"
/**
 * is_palindrome - function that checks if a linked list is palindrom
 * @head: dbpointer to the linked list
 * Return: 1 if isn't a palindrom and 0 if it is
 */
int is_palindrome(listint_t **head)
{
	int list_len = 0;
	listint_t  *href = malloc(sizeof(listint_t));

	href = *head;

	char list_values[100], /**elements,*/ *rev_elements;

	while (href != NULL)
	{
		list_values[list_len] = href->n;
		list_len++;
		href = href->next;
	}
	if (list_len == 0)
		return (1);
	rev_elements = rev_str(list_values);
	if (strcmp(rev_elements, list_values) == 0)
		return (1);
	else
		return (0);
}
	/*
	*if (list_len % 2 == 0)
	*{
		*list_len = list_len / 2;
		*for (a = 0; a <= list_len; a++)
			*elements[a] = list_values[a];
		*for (; a <= (list_len * 2); a++)
			*rev_elements[a] = list_values[a];
		*rev = rev_str(rev_elements);
		*if (_strcmp(elements, rev) == 1)
			*return (1);
		*else
			*return (0);
	*}
	*return (0);
	*/
/**
 * rev_str - Function that reverse a string
 * @string: pointer to the string that will be reversed
 * Return: pointer to the reversed string
 */
char *rev_str(char *string)
{
	int n = 0, a = 0;
	char *rev = malloc((sizeof(char) * (_strlen(string) + 1)));

	while (string[n] != 0)
		n++;
	n--;
	while (string[a] != 0)
	{
		rev[a] = string[n];
		a++;
		n--;
	}
	rev[a] = '\0';
	return (rev);
}
/**
 * _strlen - check the code for Holberton School students.
 * @s: pointer to holberton
 * Return: Always n.
 */
int _strlen(char *s)
{
	int n;

	n = 0;

	while (*s != '\0')
	{
		n++;
		s++;
	}
	return (n);
}
/**
 * _strcmp - check the code for Holberton School students.
 * @s1: hello
 * @s2: world!
 * Return: Always dest.
 */
int _strcmp(char *s1, char *s2)
{
int a = 0;

	while (s1[a] != '\0')
	{
		if (s1[a] < s2[a])
		{
			return (s1[a] - s2[a]);
		}
		if (s1[a] > s2[a])
		{
			return (s1[a] - s2[a]);
		}
		a++;
	}
	return (0);
}
