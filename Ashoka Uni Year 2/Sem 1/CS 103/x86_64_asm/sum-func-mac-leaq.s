	.section	__TEXT,__text,regular,pure_instructions
	.globl	_sum


	# Function sum
	# Arguments:
	#   %rdi -- base address of the array
	#   %rsi -- number of elements in the array
	# Return:
	#   %rax -- sum of the elements of the array

_sum:
	movq $0, %rax # sum = 0
	movq $0, %r12 # i = 0
loop:	
	cmp %rsi, %r12 # i ? n
	je done

	# compute a[i] = value at a + 8*i
	leaq (%rdi, %r12, 8), %r15
	addq (%r15), %rax # sum = sum + a[i]

	addq $1, %r12
	jmp loop

done:		
	retq


