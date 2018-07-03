public class MinStack {
    Stack<Integer> stack = null;
    Stack<Integer> minStack = null;
    public MinStack() {
        // do intialization if necessary
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    /*
     * @param number: An integer
     * @return: nothing
     */
    public void push(int number) {
        // write your code here
        stack.push(number);
        if(minStack.empty() || minStack.peek() >= number) minStack.push(number);
    }

    /*
     * @return: An integer
     */
    public int pop() {
        // write your code here
        int res = stack.pop();
        if(minStack.peek() == res) minStack.pop();
        return res;
    }

    /*
     * @return: An integer
     */
    public int min() {
        // write your code here
        return minStack.peek();
    }
}
