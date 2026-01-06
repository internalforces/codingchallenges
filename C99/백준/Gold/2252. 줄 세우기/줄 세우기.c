#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

Node** graph;
int* indegree;
int* queue_arr;
int* result;
int front = 0, rear = 0;

void addEdge(int from, int to) {
    Node* newNode = (Node*)malloc(sizeof(Node));

    newNode->vertex = to;
    newNode->next = graph[from];
    graph[from] = newNode;
    indegree[to]++;
}

void enqueue(int v) {
    queue_arr[rear++] = v;
}

int dequeue() {
    return queue_arr[front++];
}

int isEmpty() {
    return front == rear;
}

int topologicalSort(int n) {
    int count = 0;
    front = rear = 0;

    for (int i = 1; i <= n; i++) {
        if (indegree[i] == 0) {
            enqueue(i);
        }
    }

    while (!isEmpty()) {
        int current = dequeue();
        result[count++] = current;

        Node* temp = graph[current];
        while (temp != NULL) {
            indegree[temp->vertex]--;
            if (indegree[temp->vertex] == 0) {
                enqueue(temp->vertex);
            }
            temp = temp->next;
        }
    }

    return count;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    graph    = (Node**)malloc((n + 1) * sizeof(Node*));

    indegree = (int*)calloc(n + 1, sizeof(int));

    queue_arr= (int*)malloc((n + 1) * sizeof(int));
    result   = (int*)malloc((n + 1) * sizeof(int));

    for (int i = 1; i <= n; i++) {
        graph[i] = NULL;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        addEdge(a, b);
    }

    int count = topologicalSort(n);

    for (int i = 0; i < count; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    for (int i = 1; i <= n; i++) {
        Node* cur = graph[i];
        while (cur != NULL) {
            Node* next = cur->next;
            free(cur);
            cur = next;
        }
    }
    free(graph);
    free(indegree);
    free(queue_arr);
    free(result);

    return 0;
}