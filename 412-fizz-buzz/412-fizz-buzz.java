class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<String>();
        for(int index = 1; index <= n; index++) {
            if(index % 3 == 0 &&  index % 5 == 0) {
                result.add("FizzBuzz");
            } else if(index % 3 == 0) {
                result.add("Fizz");
            } else if(index % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(Integer.toString(index));
            }
        }
        return result;
    }
}