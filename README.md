# S4-2025 MakeMeStrong

# makemestrong homework

## Repo content

- `login_makeMeStrong.py`: the file to fill-in
- `strong_connectivity.py`: usefull functions
- `files\`: digraphs for your tests (see the readme...)
- `images\`: condensations of `files/digraph20_for_scc.gra` and `files/digraph34_for_scc.gra` 

## Your work

- Write one or several functions with the following specifications:
    - take a digraph G as parameter 
    - make the digraph G strongly connected (add to G the edges to make it strongly connected)
    - return the number of added edges (0 if the digraph is already strongly connected!)
- In your code, only functions not prefixed by `__` will be tested.

### How many edges?

- You cannot add more edges than the number of strongly connected components! (if you want points...)
- Your grade will increase if you can add less edges
- **Advices:**
    - Have a look at the condensation
    - Maybe finding the _sources_ (vertices without predecessors) and _sinks_ (vertices without successors) in the condensation might help...


## Handout

You can deposit your "contribution": the single file `login_makeMeStrong.py` (do not forget to replace `login`...) on Moodle (will be oppened soon...)
- As usual your `login_makeMeStrong.py` does not contain tests, but only function definitions
- You can import anything from `algopy` except `timing` (do not forget to delete the potential `@timing.timing`...)
- You can also import any built-in module
 

## Deadlines

- Tuesday, March the 15th, 10PM: tests with the digraphs in `files`
- Sunday, March the 20th, 10PM: more tests...
