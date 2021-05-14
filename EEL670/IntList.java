/**
* An IntList is a list of ints.
*/
public class IntList {
    private ConsCell start; // list head, or null
    /**
    * Construct a new IntList given its first ConsCell.
    * @param s the first ConsCell in the list, or null
    */
    public IntList(ConsCell s) {
        start = s;
    }

    /**
    * Cons the given element h onto us and return the
    * resulting IntList.
    * @param h the head int for the new list
    * @return the IntList with head h, and us as tail
    */
    public IntList cons (int h) {
        return new IntList(new ConsCell(h,start));
    }

    /**
    * Get our length.
    * @return our int length
    */
    public int length() {
        int len = 0;
        ConsCell cell = start;
        while (cell != null) { // while not at end of list
            len++;
            cell = cell.getTail();
        }
        return len;
    }

    /**
    * Concatenates two IntLists.
    * @return a new IntList x concatened with y
    */
    public IntList append (IntList y){
        IntList w = new IntList(y.start); 
        // first, we create a new IntList with y.start

        int len = this.length();
        int [] heads = new int[len]; // this array will get all heads of x 

        ConsCell cell = this.start;
        int i = len - 1;
        while ( i >= 0) {  // 
            heads[i] = cell.getHead();
            cell = cell.getTail();
            i--;  
        }

        int j = 0;
        while(j < len){
            w = w.cons(heads[j]);
            j++;
        }
        
        return w;
    }

     /**
    * Concatenates two IntLists, using recursion.
    * @return a new IntList x concatened with y
    */
    public IntList appendR (IntList y){
        ConsCell cell = new ConsCell(this.start.getHead(), this.start.getTail());
        if (cell.getTail() == null){
            return y.cons(cell.getHead());
        }
        IntList x = new IntList(this.start.getTail());
        return x.appendR(y).cons(this.start.getHead());

    }

    /**
    * Print ourself to System.out.
    */
    public void print() {
        System.out.print("[");
        ConsCell a = start;
        while (a != null) {
            System.out.print(a.getHead());
            a = a.getTail();
            if (a != null) System.out.print(",");
        }
        System.out.println("]");
    }

}