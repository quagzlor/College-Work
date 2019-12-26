	.text
	.globl	sort


	# Function sort
	# Arguments:
	#   %rdi -- base address of the array
	#   %rsi -- number of elements in the array
	# 
	# sort the elements of the array

sort:


	# ====================
	# WRITE YOUR CODE HERE
	mov %rdi,%r12
	mov 0,%r13
	mov 0,%r14
	
outloop:
	
	mov %r12,%r15
	INCQ %r13
	
	
	JMP control
inloop:	

	COMQ %r15,%r12
	JL xchg %r15,%r12

	INCQ %r13
	COMQ %r13,%rsi
	JL inloop
	
	JMP control
control:
	add 8,%r12
	JB outloop
	
	CMPQ %r13,%rsi
	JE done
	
	# ====================
	
	
	
	ret %rdi
