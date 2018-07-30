// Implements a dictionary's functionality
#include <strings.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include "dictionary.h"

#define HASH_MAX 25000
// hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

node *hashtable[HASH_MAX];

// define counter
int counter = 0;

// hash function is djb by Dan Bernstein
unsigned int Hash(const char *str)
{
    unsigned int hash = 5381;
    int n = strlen(str);

    for (unsigned int i = 0; i < n; i++)
    {
        hash = ((hash << 5) + hash) + tolower(str[i]);
    }

    return (hash & 0x7FFFFFFF) % HASH_MAX;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *cursor = hashtable[Hash(word)];
    while (cursor != NULL)
    {
        // compare strings regardless of case
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    // open dictionary and set to file
    FILE *file = fopen(dictionary, "r");
    char word[LENGTH + 1];
    // Hash table
    // While scanning through the dictionary file
    while (fscanf(file, "%s", word) != EOF)
    {
        // create new node, and check for error
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return false;
        }
        // copy the word into the new_node
        strcpy(new_node->word, word);
        // figure out hash key
        const char *tmpword = new_node->word;
        unsigned key = Hash(tmpword);
        // set the head of new_node to the array spot's linked list's head
        new_node->next = hashtable[key];
        // and then reassign the array spot's linked list's head
        hashtable[key] = new_node;
        // increment counter
        counter++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < HASH_MAX; i++)
    {
        node *cursor = hashtable[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
