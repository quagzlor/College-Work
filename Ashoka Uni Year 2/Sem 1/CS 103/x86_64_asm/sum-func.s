	.text
	.globl	sum


	# Function sum
	# Arguments:
	#   %rdi -- base address of the array
	#   %rsi -- number of elements in the array
	# Return:
	#   %rax -- sum of the elements of the array

sum:
	movq $0, %rax # sum = 0
	movq $0, %r12 # i = 0
loop:	
	cmp %rsi, %r12 # i ? n
	je done

	# compute a[i] = value at a + 8*i
	movq %r12, %r14  # r14 = i
	imulq $8, %r14   # r14 = 8*i
	addq %rdi, %r14  # r14 = 8*i + a
	addq (%r14), %rax  # sum = sum + a[i]

	addq $1, %r12
	jmp loop

done:		
	ret
