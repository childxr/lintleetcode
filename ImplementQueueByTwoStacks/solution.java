public class MyQueue {
    private Stack<Integer> instack = null;
    private Stack<Integer> outstack = null;
    
    public MyQueue() {
        // do intialization if necessary
        instack = new Stack<> ();
        outstack = new Stack<> ();
    }

    /*
     * @param element: An integer
     * @return: nothing
     */
    public void push(int element) {
        // write your code here
        instack.push(element);
    }
    
    private void moveStack() {
        if(outstack.empty()) {
            while(!instack.empty()) {
                outstack.push(instack.pop());
            }
        }
    }
    /*
     * @return: An integer
     */
    public int pop() {
        // write your code here
        moveStack();
        return outstack.pop();
    }

    /*
     * @return: An integer
     */
    public int top() {
        // write your code here
        moveStack();
        return outstack.peek();
    }

}
