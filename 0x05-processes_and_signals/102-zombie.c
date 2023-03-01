#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
* main - A C program that creates 5 zombie processes.
*
* Return: 0 (Success)
*/
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			exit(0);
		} else if (child_pid < 0)
		{
			perror("fork error");
			exit(1);
		} else
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
	}
	return (0);
}
