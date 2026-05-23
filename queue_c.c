#define DLL_EXPORT

#include "queue_c.h"
#include <stdlib.h>

typedef struct CyclicQueue {
    int* buffer;
    int head;
    int tail;
    int count;
    int max_size;
} CyclicQueue;

CyclicQueue* create_queue(int max_size) {
    CyclicQueue* q = (CyclicQueue*)malloc(sizeof(CyclicQueue));
    q->buffer = (int*)malloc(sizeof(int) * max_size);
    q->head = 0;
    q->tail = 0;
    q->count = 0;
    q->max_size = max_size;
    return q;
}

void delete_queue(CyclicQueue* queue) {
    if (queue) {
        free(queue->buffer);
        free(queue);
    }
}

bool push(CyclicQueue* queue, int value) {
    if (queue->count >= queue->max_size) return false;
    queue->buffer[queue->tail] = value;
    queue->tail = (queue->tail + 1) % queue->max_size;
    queue->count++;
    return true;
}
bool pop(CyclicQueue* queue, int* output) {
    if (queue->count <= 0) return false;
    *output = queue->buffer[queue->head];
    queue->head = (queue->head + 1) % queue->max_size;
    queue->count--;
    return true;
}

void clear(CyclicQueue* queue) {
    queue->head = 0;
    queue->tail = 0;
    queue->count = 0;
}

int find(CyclicQueue* queue, int value) {
    for (int i = 0; i < queue->count; i++) {
        int idx = (queue->head + i) % queue->max_size;
        if (queue->buffer[idx] == value) return i;
    }
    return -1;
}

bool is_empty(CyclicQueue* queue) {
    return queue->count == 0;
}