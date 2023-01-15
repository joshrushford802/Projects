#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int n = 0; n < candidate_count; n++)
    {
        candidates[n].name = argv[n + 1];
        candidates[n].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int n = 0; n < voter_count; n++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int n = 0; n < candidate_count; n++)
    {
        if (strcmp(name, candidates[n]. name) == 0)
        {
            candidates[n].votes++;
            return true;
        }
    }

    return false;

}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int total_votes = 0;

    for (int n = 0; n < candidate_count; n++)
    {
        if (candidates[n].votes > total_votes)
        {
            total_votes = candidates[n].votes;
        }
    }

    for (int n = 0; n < candidate_count; n++)
    {
        if (candidates[n].votes == total_votes)
        {
            printf("%s\n", candidates[n].name);
        }
    }
    return;
}