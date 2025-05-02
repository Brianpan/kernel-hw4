CC = gcc
CFLAGS = -O1 -g -Wall -Werror

q1: q1.o
	$(CC) $(CFLAGS) -o $@ $^
