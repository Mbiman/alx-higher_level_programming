#include <stdio.h>

/**
 * print_python_list_info - a C function that prints python list
 * @p: a python object
 *
 * Return:nothing
 */

void print_python_list_info(PyObject *p)
{
	while (p != 0)
	{
		printf(p);
	}
}
