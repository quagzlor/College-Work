	.text
	.globl	max


	# Function max
	# Arguments:
	#   %rdi -- base address of the array
	#   %rsi -- number of elements in the array
	# Return:
	#   %rax -- max of the elements of the array

max:
	

	# ====================
	# WRITE YOUR CODE HERE
	mov 1,%r12
	mov %rdi,%rax
	mov 0,%r13
	
	loop:
		
		add 8,%rdi
		mov %r13,%rdi
		
		COMQ %rax,%r13
		JL lesser
		
		INCQ %r12
		COMQ %r12,%rsi
		JL loop

	
	lesser:
		
		mov %r13,%rax
		INCQ %r12
		COMQ %r12,%rsi
		JL loop
		
	

	

	# ====================
	
	
	
	ret %rax
