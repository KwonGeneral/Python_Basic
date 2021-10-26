#include<stdio.h>
#include<stdlib.h>

#define STACK_SIZE 5 // 천장 까지 책을 쌓을 수 있는 개수.

char stack[STACK_SIZE];  // 책을 쌓을거라고 사서한테 말함.
int stack_last_data = -1;   // 마지막에 쌓은 책. 가장 위에 있는 책.

// 책이 천장에 닿았는지 확인. 
int check_stack() { 
	if(stack_last_data >= STACK_SIZE - 1) {   // 마지막에 쌓은 책이 천장에 닿았을 경우.
		printf("\n책이 천장에 닿았습니다. \n더 이상 책을 쌓지 못합니다.\n");
		return 1;
	}
	return 0;
}

// 책 넣기.
void push(char data) { 
    printf("\n책 제목 [ %c ]를 쌓기 위해 시도합니다.\n", data);
	if(!check_stack()) { // 책이 천장에 닿지 않았을 경우, 책을 넣는다.
		stack_last_data++; 
		stack[stack_last_data] = data; 
	}
 }
 
 // 책 빼기.
 void pop() {
    if(stack_last_data == -1) { // 뺄 수 있는 책이 없다.
        printf("\n책의 개수가 [ 0 ]개이기 때문에\n뺄 수 있는 책이 없습니다.\n");
    } else { // 책을 뺀다.
        char temp_stack = stack[stack_last_data]; 
		stack_last_data--; 
        printf("\n책 제목 [ %c ]를 뺐습니다.\n", temp_stack);
    }
}

// 현재 책 목록 파악.
void stack_count() { 
	if(stack_last_data == -1) { // 뺄 수 있는 책이 없는 경우.
		printf("\n현재 책의 개수는 [ 0 ]개 입니다.\n");
	} else {
        int temp_stack_data = stack_last_data;
        printf("\n현재 책의 개수는 [ %d ]개 입니다.\n", temp_stack_data + 1); 
        for(int k = 0; k <= stack_last_data; k++) { 
			printf("\n책 제목 [ %c ] ", stack[k]); 
		}
		printf("\n");
    }
 }

int main() {
    printf("\n ========== ========== ==========\n");
	stack_count();
    pop();

    printf("\n ========== ========== ==========\n");
    push('A');
	push('B');
	push('C');
    stack_count();
    
    printf("\n ========== ========== ==========\n");
	push('D');
	push('E');
    stack_count();
    
    printf("\n ========== ========== ==========\n");
	push('F');
	push('G');
    stack_count();
	
    printf("\n ========== ========== ==========\n");
    pop();
	pop();
    stack_count();
}
