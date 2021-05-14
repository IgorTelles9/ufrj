class HeapManager2 {
	static private final int NULL = -1; // null link
	public int[] memory; // the memory we manage
	private int freeStart; // start of the free list

	/**
	 * HeapManager constructor.
	 * @param initialMemory int[] of memory to manage
	 */
	public HeapManager2(int[] initialMemory) {
		memory = initialMemory;
		memory[0] = memory.length; // one big free block
		memory[1] = NULL; // free list ends with it
		freeStart = 0; // free list starts with it
	}

	/**
	 * Allocate a block and return its address.
	 * @param requestSize int size of block, > 0
	 * @return block address
	 * @throws OutOfMemoryError if no block big enough
	 */
	public int allocate(int requestSize) {
		int size = requestSize + 1; // size with header 
		// Do best-fit search.
		int p = freeStart; // head of free list 
		int lag = NULL; 
		int []  freeStartOptions = new int [memory.length/2]; // an array with possible values for p

		if (memory[p] >= size){

			freeStartOptions[0] = p; 
			int i = p;
			int j = 1;
			// this while goes through empty blocks
			// and creates an array with the sizes of empty blocks
			// and also fills the array with '-1' when there's no more empty blocks

			while(j < freeStartOptions.length){
				if (memory[i+1] != NULL){ // checks if there's a link to another block
					i = memory[i+1];
					freeStartOptions[j] = i;
				}
				else{ // if there isn't, so there isn't any new empty block
					freeStartOptions[j] = -1;
				}
				j++;
			}

			// we make sure that this variables will always be changed in the for 
			int menorModulo = -1; 
			int newP = -1;

			for (int k = 0; k < freeStartOptions.length; k++){
				if (freeStartOptions[k] == NULL){ // there is no more empty blocks
					break;
				}
				
				// we wanna check which empty block has the minimum size
				// to do the allocation 
				int modulo = memory[freeStartOptions[k]] - size; 
				if (k == 0){
					menorModulo = modulo;
					newP = freeStartOptions[k];

				}
				else if (modulo == 0) { 
				// if we found an empty block with the exact size
				// we just assign it, no need to look more. 
					newP = freeStartOptions[k];
					break;
				}
				else if (modulo < menorModulo){
					menorModulo = modulo;
					newP = freeStartOptions[k];
				}
			}
			if (newP != NULL){
				if (newP != freeStart) lag = p;
				p = newP;
			}
	
		}
		else
		{

		// if block doesn't have enough space, 
		// go to next block
		while (p!=NULL && memory[p]<size) { 
			lag = p; // lag is previous p 
			p = memory[p+1]; // link to next block 
			//System.out.println(p);
		}
		if (p==NULL) // no block large enough
			throw new OutOfMemoryError();

		}
		
		int nextFree = memory[p+1]; // block after p

		// Now p is the index of a block of sufficient size
		// lag is null or the index of p's predecessor
		// nextFree is the index of p's successor or null.
		
		// If the block has more space than we need, carve out what we need from 
		// the front and return the unused end part to the free list.
		int unused = memory[p]-size; // extra space 

		// if more than a header's worth
		// we will create a new block with the free space
		if (unused>1) { 
			nextFree = p+size; // index of the unused piece
			memory[nextFree] = unused; // the space avaiable
			memory[nextFree+1] = memory[p+1]; // fill in link
			memory[p] = size; // reduce p's size accordingly
		}

		// Link out the block we are allocating and done.
		if (lag==NULL) freeStart = nextFree;
		else memory[lag+1] = nextFree;
		
		return p+1; // index of useable word (after header)
	}

	/**
	 * Deallocate an allocated block.  This works only if the block address is one that was returned by
	 * allocate and has not yet been deallocated.
	 * @param address int address of the block
	 */
	public void deallocate(int address) {
		int addr = address-1; // real start of the block

		// Find the insertion point in the sorted free list for this block.

		int p = freeStart;
		int lag = NULL;
		while (p!=NULL && p<addr) {
			lag = p;
			p = memory[p+1];
		}

		// Now p is the index of the block to come after ours in the free list, or NULL, and lag is the
		// index of the block to come before ours in the free list, or NULL.

		// If the one to come after ours is adjacent to it, merge it into ours and restore the property
		// described above.

		if (addr+memory[addr]==p) {
			memory[addr] += memory[p]; // add its size to ours
			p = memory[p+1]; 
		}
		if (lag==NULL) { // ours will be first free
			freeStart = addr;
			memory[addr+1] = p;
		}
		else 
			if (lag+memory[lag]==addr) { // block before is adjacent to ours
				memory[lag] += memory[addr]; // merge ours into it
				memory[lag+1] = p;
			}
			else { // neither: just a simple insertion
				memory[lag+1] = addr;
				memory[addr+1] = p;
			}
	}

	/**
	 * Prints memory configuration.
	 */
	public void echo() {
		System.out.printf("Memory configuration\n");
		for(int i=memory.length-1; i >=0 ; i--)
			System.out.printf("\t[%d] = %d\n",i,memory[i]);
		System.out.printf("\tfreeStart: %d\n",freeStart);

	}	
}
