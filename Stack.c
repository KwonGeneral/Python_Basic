#include<stdio.h>
#include<stdlib.h>

#define STACK_SIZE 5 // õ�� ���� å�� ���� �� �ִ� ����.

char stack[STACK_SIZE];  // å�� �����Ŷ�� �缭���� ����.
int stack_last_data = -1;   // �������� ���� å. ���� ���� �ִ� å.

// å�� õ�忡 ��Ҵ��� Ȯ��. 
int check_stack() { 
	if(stack_last_data >= STACK_SIZE - 1) {   // �������� ���� å�� õ�忡 ����� ���.
		printf("\nå�� õ�忡 ��ҽ��ϴ�. \n�� �̻� å�� ���� ���մϴ�.\n");
		return 1;
	}
	return 0;
}

// å �ֱ�.
void push(char data) { 
    printf("\nå ���� [ %c ]�� �ױ� ���� �õ��մϴ�.\n", data);
	if(!check_stack()) { // å�� õ�忡 ���� �ʾ��� ���, å�� �ִ´�.
		stack_last_data++; 
		stack[stack_last_data] = data; 
	}
 }
 
 // å ����.
 void pop() {
    if(stack_last_data == -1) { // �� �� �ִ� å�� ����.
        printf("\nå�� ������ [ 0 ]���̱� ������\n�� �� �ִ� å�� �����ϴ�.\n");
    } else { // å�� ����.
        char temp_stack = stack[stack_last_data]; 
		stack_last_data--; 
        printf("\nå ���� [ %c ]�� �����ϴ�.\n", temp_stack);
    }
}

// ���� å ��� �ľ�.
void stack_count() { 
	if(stack_last_data == -1) { // �� �� �ִ� å�� ���� ���.
		printf("\n���� å�� ������ [ 0 ]�� �Դϴ�.\n");
	} else {
        int temp_stack_data = stack_last_data;
        printf("\n���� å�� ������ [ %d ]�� �Դϴ�.\n", temp_stack_data + 1); 
        for(int k = 0; k <= stack_last_data; k++) { 
			printf("\nå ���� [ %c ] ", stack[k]); 
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
