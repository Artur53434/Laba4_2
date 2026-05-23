#pragma once
#include <stdbool.h>

#ifdef DLL_EXPORT
#define DECLSPEC __declspec(dllexport)
#else
#define DECLSPEC __declspec(dllimport)
#endif

typedef struct CyclicQueue CyclicQueue;

DECLSPEC CyclicQueue* create_queue(int max_size);
DECLSPEC void delete_queue(CyclicQueue* queue);
DECLSPEC bool push(CyclicQueue* queue, int value);
DECLSPEC bool pop(CyclicQueue* queue, int* output);
DECLSPEC void clear(CyclicQueue* queue);
DECLSPEC int find(CyclicQueue* queue, int value);
DECLSPEC bool is_empty(CyclicQueue* queue);