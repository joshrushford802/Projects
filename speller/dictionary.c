// Implements a dictionary's functionality
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

unsigned int tally;
unsigned int hist;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    hist = hash(word);
    node *p = table[hist];
    while (p > 0 || p < 0)
    {
        if (strcasecmp(word, p->word) == 0)
        {
            return true;
        }
        p = p->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long sum = 0;
    for (int j = 0; j < strlen(word); j++)
    {
        sum = tolower(word[j]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *r = fopen(dictionary, "r");
    if (r == NULL)
    {
        printf("Critical Failure");
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(r, "%s", word) != EOF)
    {
        node *j = malloc(sizeof(node));
        if (j == NULL)
        {
            return false;
        }
        strcpy(j->word, word);
        hist = hash(word);
        j->next = table[hist];
        table[hist] = j;
        tally = tally + 1;
    }
    fclose(r);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (tally > 0)
    {
        return tally;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int j = 0; j < N; j++)
    {
        node *p = table[j];
        while (p)
        {
            node *x = p;
            p = p->next;
            free(x);
        }
        if (p == NULL)
        {
            return true;
        }
    }
    return false;
}
